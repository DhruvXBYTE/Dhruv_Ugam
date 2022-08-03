import os
from datetime import date, datetime



datenow = datetime.now().strftime('%Y_%m_%d')
today = date.today()
# datenow = today.now().strftime("%d_%m_%Y")
db_host = 'localhost'
db_user = 'root'
db_pass = 'xbyte'
db_category_table = f'category_weekly'
db_name = 'ugam_saturn_category'
db_data_table = f'productdata_{datenow}'
# db_data_table = f'productdata_2021_07_30'



drive = 'D'
store_name = 'Saturn_de'
current_directory = os.path.dirname(__file__)
HTMLs = "D:\\Daily Scheduler\\0. UGAM\\UGAM_Saturn_de_category\\HTML_SS\\HTML"
HTML = HTMLs + f'\\HTML_{datenow}'
# HTML = HTMLs + f'\\HTML_2021_07_30'
Log = HTMLs + f'\\Log'



try:

    if not os.path.exists(HTMLs):
        os.makedirs(HTMLs)
    if not os.path.exists(HTML):
        os.makedirs(HTML)
    # if not os.path.exists(SEARCH_TERM_HTML):
    #     os.makedirs(SEARCH_TERM_HTML)
    if not os.path.exists(Log):
        os.makedirs(Log)

except Exception as e:
    print('exception in makedir config file error: ', e)

""" --dll-- """
import clr

clr.AddReference(r"D:\Ugam_File_Upload_App\UGAM_Category_dll\common_code_100_site_project.dll")

from common_code_100_site_project import ugam_3_Category_PDP
catpdp = ugam_3_Category_PDP()
createtable = catpdp.create_table()
updatecategory = catpdp.Update_category_Query()
insert = catpdp.InsertResultsQuery()
delete = catpdp.delete_category_Query()
updateproduct = catpdp.Update_productdata_Query()
tsv = catpdp.export_csv_query()


""" ---make log file using logging module--- """
date = datetime.today().strftime("%d_%m_%Y")


import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.setLevel(logging.ERROR)
logger.setLevel(logging.WARNING)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler(Log+f'\\ugam_saturn_category_{date}.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


# def pagesavewithselenium(product_url):
#
#     try:
#         from selenium import webdriver
#         import time
#         from Screenshot import Screenshot_Clipping
#         from selenium import webdriver
#         from webdriver_manager.chrome import ChromeDriverManager
#
#         options = webdriver.ChromeOptions()
#         options.headless = False
#         driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
#         driver.maximize_window()
#         driver.get(product_url)
#         # driver.quit()
#         # pageSource = driver.page_source
#
#         # create file name
#         nw_product_id =driver.current_url.split('-')[-1]
#         product_id = nw_product_id.split('.')[0]
#         # print(nw_product_id)
#         filename = f'/{product_id}.html'
#
#         # WRITE A FILE
#         path = HTML + filename
#         path = path.replace("\\", "/")
#         if not os.path.exists(path):
#             with open(path, "w", encoding='utf-8') as f:
#                 f.write(driver.page_source)
#
#     except Exception as e:
#         print(e)


# pagesavewithselenium('https://www.saturn.de/de/product/arzopa-a1-gamut-4k-156-zoll-fhd-156-zoll-full-91929436.html')