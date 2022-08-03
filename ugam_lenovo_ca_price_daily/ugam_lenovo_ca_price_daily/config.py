import os
from datetime import date, datetime

datenow = datetime.now().strftime('%Y_%m_%d')
today = date.today()
# datenow = today.now().strftime("%d_%m_%Y")
db_host = '142.4.216.131'
# db_host='192.168.1.133'
db_user = 'root'
db_pass = 'xbyte'
db_category_table = f'input_sku'
db_name = 'ugam_dailyprice_ca_lenovo'
db_data_table = f'productdata_{datenow}'

drive = 'D'
store_name = 'LENOVO_CA'
current_directory = os.path.dirname(__file__)

HTMLs = "D:\\DC\\HTMLs\\CA\\lenovo\\lenovo_ca_price_daily\\HTMLs"
HTML = HTMLs + f'\\HTML_{datenow}'
# HTML = HTMLs + f'\\HTML_2021_03_25'
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
clr.AddReference(r"D:\Ugam_File_Upload_App\price_dll\common_code_100_site_project.dll")

from common_code_100_site_project import ugam_3_Category_Daily_PDP
catpdp = ugam_3_Category_Daily_PDP()

""" ---make log file using logging module--- """
date = datetime.today().strftime("%Y_%m_%d")

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.setLevel(logging.ERROR)
logger.setLevel(logging.WARNING)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler(Log+f'\\ugam_lenovo_{date}.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
