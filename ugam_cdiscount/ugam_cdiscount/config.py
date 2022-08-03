print('config file open................')
import os
from datetime import date, datetime

datenow = datetime.now().strftime('%Y_%m_%d')
today = date.today()
# datenow = today.now().strftime("%d_%m_%Y")
db_host = 'localhost'
db_user = 'root'
db_pass = 'xbyte'
db_category_table = f'input_sku'
db_name = 'ugam_cdiscount_mpn'
db_data_table = f'productdata_{datenow}'
# db_data_table = f'productdata_2021_07_30'

drive = 'D'
store_name = 'Cdiscount_mpn'
current_directory = os.path.dirname(__file__)
#"E:\\Dhruv\\Ugam_category\\HTMLs\\IN\\lenovo\\lenovo_In_category\\HTMLs"
HTMLs = "D:\\DC\\HTMLs\\Fr\\Cdiscount\\Cdiscount_fr_mpn\\HTMLs"
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

# clr.AddReference("E:\\Twinkal Prajapati\\UGAM_PROJECTS\\FR\\ldlc_fr_category\\common_code_100_site_project.dll")
clr.AddReference(r"D:\Ugam_File_Upload_App\UGAM_Cdiscount_MPN_dll\common_code_100_site_project.dll")

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
file_handler = logging.FileHandler(Log+f'\\ugam_harvey_norman_{date}.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)