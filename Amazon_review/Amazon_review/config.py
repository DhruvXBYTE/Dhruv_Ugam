print('config file open................')
from datetime import datetime
import os
from datetime import datetime

today_date = datetime.now().strftime('%d_%m_%Y')
db_host = 'localhost'
db_user = 'root'
db_passwd = 'xbyte'
db_name = 'Amazon_Review'
# sub_category_table=f'subcategory_{today_date}'
# db_brand_table = f'searchterms'
db_input_sku="input_sku"
product_table = f"review_data_{today_date}"

# make directory in bellow and check directory is exists or not
date = datetime.today().strftime("%d_%m_%Y")

current_directory = os.path.dirname(__file__)
HTMLs = "D:\\DC\\HTMLs\\LEARN\\Amazon_Review\\HTMLs"
HTML = HTMLs + f'\\HTML_{today_date}'
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
file_handler = logging.FileHandler(Log + f'\\Amazon_Reviwe_{date}.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
