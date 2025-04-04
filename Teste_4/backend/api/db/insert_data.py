import csv
from tqdm.auto import tqdm
from .connection import get_connection
import os

def insert_csv_data(file_path_list: list[str], table_name: str, newline: str = "\n", delimiter: str = ","):
    conn = get_connection()
    cursor = conn.cursor()

    row_count = cursor.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()

    if row_count[0] > 0:
        print("Data already exists in the table. Skipping insertion.")
        return

    with open(os.path.join(*file_path_list), 'r', newline=newline, encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=delimiter)
        next(reader)

        columns = cursor.execute(f"PRAGMA table_info({table_name})").fetchall()
        columns = [description["name"] for description in columns]

        placeholders = ", ".join(["?"] * len(columns))
        sql = f"INSERT INTO {table_name} ({",".join(columns)}) VALUES ({placeholders})"

        for row in tqdm(reader, desc="Inserting data", unit=" rows"):
            cursor.execute(sql, row)
    
    conn.commit()
    conn.close()