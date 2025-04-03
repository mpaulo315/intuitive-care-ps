from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import platform

BASE_URL = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
DEFAULT_TIMEOUT = 30

def get_driver() -> WebDriver:
    """ Retrieves the driver for the browse considering the OS """

    if platform.system() == "Windows":
        from selenium.webdriver.edge.service import Service as EdgeService
        from webdriver_manager.microsoft import EdgeChromiumDriverManager
        from selenium.webdriver.edge.options import Options as EdgeOptions

        service = EdgeService(EdgeChromiumDriverManager().install())

        options = EdgeOptions()

        options.add_argument("--headless=new")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")   

        options.add_experimental_option("prefs", {
        "download.default_directory": os.getcwd(),
        "download.prompt_for_download" : False,
        "plugins.always_open_pdf_externally" : True
        })

        return webdriver.Edge(service=service, options=options)

    if platform.system() == "Linux":
        from selenium.webdriver.firefox.service import Service
        from webdriver_manager.firefox import GeckoDriverManager
        from selenium.webdriver.firefox.options import Options as FirefoxOptions

        service = Service(GeckoDriverManager().install())

        options = FirefoxOptions()

        options.add_argument("--headless=new")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")   

        # options.add_experimental_option("prefs", {
        # "download.default_directory": os.getcwd(),
        # "download.prompt_for_download" : False,
        # "plugins.always_open_pdf_externally" : True
        # })
        
        return webdriver.Firefox(service=service, options=options)
    
    if platform.system() == "Darwin":
        from selenium.webdriver.safari.options import Options as SafariOptions
        
        options = SafariOptions()
        
        options.add_argument("--headless=new")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")   

        return webdriver.Safari(options=options)

    raise ValueError(f"System platform not avaiable: {platform.system()}") 

def download_pdf_file(url: str,  filename: str | None = None) -> None:
    """Downloads the PDF file from url and saves it to the current directory,
        if the file already exists, it will not download it again. 
        
        :param url: The URL-like string of the PDF file to download
        :param filename: The name of the file to save, if None, the filename will be extracted from the URL
        """
    from typing import Callable
    from re import search
    from requests import get
    
    response = get(url)
    if response.status_code != 200:
        raise ValueError(f"Error downloading file: {response.status_code}")
    
    filename_extractor: Callable[[str], str] = lambda url: search(r"(?P<name>[^/]+)\.pdf$", url).group("name") 
    if filename is None:
        filename = filename_extractor(url)

    file_path = f"{filename}.pdf"
    if os.path.exists(file_path):
        return
    
    with open(f"{file_path}", "wb") as file:
        file.write(response.content)

driver : WebDriver = get_driver()

try :
    driver.get(BASE_URL)
    attachs_xpath = './/a[@class="internal-link"][contains(text(), "Anexo")]'

    attachments = driver.find_elements(By.XPATH, attachs_xpath)

    # Wait for the attachments to be present
    WebDriverWait(driver, DEFAULT_TIMEOUT).until(EC.presence_of_all_elements_located((By.XPATH, attachs_xpath)))

    # Get only the elements that have the href attribute ending with .pdf
    attach_1_el, attach_2_el = list(filter(lambda x: x.get_attribute("href").endswith("pdf"), attachments))

    download_pdf_file(url=attach_1_el.get_attribute("href"))
    download_pdf_file(url=attach_2_el.get_attribute("href"))
finally:
    driver.quit()
