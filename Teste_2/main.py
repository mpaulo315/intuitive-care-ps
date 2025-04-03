import tkinter as tk
from tkinter import filedialog
import pdfplumber
from tqdm.auto import tqdm
import pandas as pd
import re

root = tk.Tk()
root.withdraw()

pdf_file_path = filedialog.askopenfilename(title="Selecione o arquivo correspondente ao anexo 'Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf'", defaultextension=".pdf")

if not pdf_file_path:
    raise ValueError("Select a proper PDF file.")

pdf = pdfplumber.open(pdf_file_path)
main_df = pd.DataFrame()

# Iterate over the pages of the PDF, ignoring the first two pages
for page in tqdm(pdf.pages[2:], desc="Processing pages"):
    # Extract the table in the page
    table = page.extract_table()
    df = pd.DataFrame(columns=table[0], data=table[1:])

    # Adjusting the data
    df = df.replace(r"\n", " ", regex=True)
    df.columns = df.columns.str.replace("\n", " ")
    
    # Concatenating the temporary DataFrame to the main one
    main_df = pd.concat([main_df, df], ignore_index=True)

# Building the legend DataFrame
table_first_page = pdf.pages[3]

legend_text_header = "Legenda:"
legend_index = table_first_page.extract_text().find(legend_text_header)

# Extracting the legend keys and value in one single string and "cleaning" it
raw_legend = table_first_page.extract_text()[(legend_index + len(legend_text_header)):]
legend = raw_legend.replace("\n", "").strip()

# \w replaced for [a-zA-Z\u00C0-\u00FF] for matching latin characters
key_value_regex = r"(?P<key>[A-Z]{2,3}):\s(?P<value>[a-zA-Z\u00C0-\u00FF]+(?:\.?\s[a-zA-Z\u00C0-\u00FF]+)*)(?:\s|$)"
legend_dict = {key : value for key, value in re.findall(key_value_regex, legend)}

# Lambda functions that maps the arg to the value in the legend dictionary
legend_mapper = lambda x: legend_dict[x] if isinstance(x, str) and x in legend_dict else x
main_df["OD"] = main_df["OD"].map(legend_mapper)
main_df["AMB"] = main_df["AMB"].map(legend_mapper)


# Saving the DataFrame as a CSV file
csv_filename = "Rol de Procedimentos e Eventos em Saúde"
zip_filename = "Teste_Marcos_Paulo_de_Souza_Pereira"

main_df.to_csv(f"{zip_filename}.zip", index=False, 
               compression={"method": "zip", "compresslevel": 1, "archive_name": f"{csv_filename}.csv"})