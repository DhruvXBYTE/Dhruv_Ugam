# print('config file open................')

from datetime import datetime
import os
from datetime import datetime

import os
from datetime import datetime

""" import dll in project """
import clr

# clr.AddReference("common_code_100_site_project")

# from common_code_100_site_project import common_code_100_site

clr.AddReference(r"D:\Ugam_File_Upload_App\common_code_100_site_project.dll")
from common_code_100_site_project import common_code_100_site
dllobj = common_code_100_site()


# DB info
today_date = datetime.now().strftime('%Y_%m_%d')
db_host = 'localhost'   #51.222.154.83
db_user = 'root'
db_passwd = 'xbyte'
db_name = 'ugam_coppel_nw' #ugam_copple_mx

date = datetime.today().strftime("%d_%m_%Y")
# Tables Name

product_data_table = f'productdata_{today_date}'

f_version = "0"
feedid =""


""" Now we are use the dll object for create folders for tsv and htmls and screenshot """


dllobj.create_folder("D","coppel_uk","daily")
TSV_FILE_PATH = dllobj.tsv_filepath
HTML_FOLDER_PATH = dllobj.html_folder_path
SCREENSHOT_FOLDER_PATH = dllobj.screenshot_folder_path
SCHEDULAR_PATH = dllobj.Scheduler_path
Log = f"{SCREENSHOT_FOLDER_PATH.replace('Screenshot','Log')}"
if not os.path.exists(Log):
    os.makedirs(Log)

import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.setLevel(logging.ERROR)
logger.setLevel(logging.WARNING)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')
file_handler = logging.FileHandler(Log + f'\\copple_{date}.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


# lum_proxy_ser_list = [
#     "lum-customer-xbyte-zone-zone_us:0gi0pioy3oey",
#     "lum-customer-xbyte-zone-zone_germany:germany@2018",
#     "lum-customer-xbyte-zone-zone_uk:bqa3iap0g4nr",
#     "lum-customer-xbyte-zone-zone_france:france@2018",
#     "lum-customer-xbyte-zone-zone_spain:k4vt6e2v53v9",
#     "lum-customer-xbyte-zone-zone_italy:et2g17oqw1nm",
#     "lum-customer-xbyte-zone-zone_australia:rjbsuy1tzgco",
#     "lum-customer-xbyte-zone-zone_japan:5v9sl7ilbppn",
#     "lum-customer-xbyte-zone-zone_taiwan:b2kqeq76cxi6",
#     "lum-customer-xbyte-zone-zone_netherland:zvptczvd2ahq",
#     "lum-customer-xbyte-zone-zone_russia:plpsy85v8pu6",
#     "lum-customer-xbyte-zone-zone_india:w6zj0g4ikjy3"
# ]

#
# import random
# proxy_auth = random.choice(lum_proxy_ser_list)
# proxy_host = "zproxy.lum-superproxy.io"
# proxy_port = "22225"
# proxies = {"https": "https://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port),
#        "http": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port)}

#
# """ Screenshot capture setting here... """
# from GrabzIt import GrabzItImageOptions
# from GrabzIt import GrabzItClient
#
# grabzIt = GrabzItClient.GrabzItClient("NDg5Yzg2ZDAxYWRmNDkzYjhhMWJhNzkwYTgwYTdiYTU=",
#                                       "WxZyPz8/MD8VPz8tLD9eTz8ePz8/Pz89YCs/P152PxI=")

# options = GrabzItImageOptions.GrabzItImageOptions()
# options.browserHeight = -1
# options.width = -1
# options.height = -1
# options.format = "jpg"
# options.noCookieNotifications = True
# options.noAds = True
# options.delay = 10000
# options.proxy = proxies
