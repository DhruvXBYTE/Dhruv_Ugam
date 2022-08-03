print('config file open................')
from datetime import datetime
import os
from datetime import datetime

today_date = datetime.now().strftime('%d_%m_%Y')
db_host = '192.168.1.133'
db_user = 'root'
db_passwd = 'xbyte'
db_name = 'ugam_amazon_multiple_geo'
# sub_category_table=f'subcategory_{today_date}'
# db_brand_table = f'searchterms'
db_input_sku_1="watert_heater_scope"
product_table = f"productdata_{today_date}_{db_input_sku_1}"

# make directory in bellow and check directory is exists or not
date = datetime.today().strftime("%d_%m_%Y")

current_directory = os.path.dirname(__file__)
HTMLs = "D:\\DC\\HTMLs\\US\\Amazon_7\\watert_heater_scope\\HTMLs"
HTML = HTMLs + f'\\HTML_{today_date}_geo'
Log = HTMLs + '\\Log'

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

# make log file using logging module

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.setLevel(logging.ERROR)
logger.setLevel(logging.WARNING)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler(Log + f'\\Amazon_Geo_Multiple_log{date}.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
