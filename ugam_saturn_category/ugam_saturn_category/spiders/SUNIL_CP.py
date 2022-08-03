

# TODO ------------------------------ MY SELF CODE ------------------




# import requests
# import random
# import scrapy
# from ugam_saturn_category.config import *
# from ugam_saturn_category.pipelines import *
# import pymysql
# import json
# import requests
# from random_user_agent.params import SoftwareName, OperatingSystem
# from random_user_agent.user_agent import UserAgent
# from random import choice
# import time
#
# def get_useragent():
#     l1 = [SoftwareName.CHROME.value, SoftwareName.FIREFOX.value, SoftwareName.OPERA.value]
#     software_names = [choice(l1)]
#     operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value, OperatingSystem.SUNOS.value]
#     user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=1000)
#     return user_agent_rotator.get_random_user_agent()
#
# class Ugame_saturn_de(scrapy.Spider):
#     name = 'santurn_de_category'
#     F_PATH = HTML
#
#
#     # 'x-operation':'SearchV4',
#
#     header = {
#         'authority': 'www.saturn.de',
#         'method': 'GET',
#         # 'path': '/api/v1/graphql?operationName=CategoryV4&variables=%7B%22hasMarketplace%22%3Atrue%2C%22maxNumberOfAds%22%3A2%2C%22isRequestSponsoredSearch%22%3Atrue%2C%22isDemonstrationModelAvailabilityActive%22%3Afalse%2C%22withMarketingInfos%22%3Afalse%2C%22filters%22%3A%5B%5D%2C%22pimCode%22%3A%22CAT_DE_SAT_66%22%2C%22page%22%3A1%2C%22experiment%22%3A%22mp%22%2C%22sessionId%22%3A%22639b70cf-d794-475c-8297-dba226e2f1b7%22%2C%22customerId%22%3A%22639b70cf-d794-475c-8297-dba226e2f1b7%22%2C%22pageType%22%3A%22Category%22%2C%22productFilters%22%3A%5B%5D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%226d8e4ac5962c0673f5df27e5e8939e2fcd4270227dffc0ff2772c5337a149192%22%7D%2C%22pwa%22%3A%7B%22salesLine%22%3A%22Saturn%22%2C%22country%22%3A%22DE%22%2C%22language%22%3A%22de%22%7D%7D',
#         'scheme': 'https',
#         'accept': '*/*',
#         # 'accept-encoding': 'gzip, deflate, br',
#         'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
#         'apollographql-client-name': 'pwa-client',
#         'apollographql-client-version': '1.79.0',
#         'content-type': 'application/json',
#         # 'cookie': 'optid=3d8c3824-eb71-4464-86e3-06285ac19494; a=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im8yc2lnbiJ9.eyJzdWIiOiI2MjM0ZDc5MS00ODBiLTQ1OWQtYmZmYi01ZDdkOTJhMzkxZmIiLCJpc3MiOiJtbXNlIiwiaWF0IjoxNjUzOTE0OTU2LCJleHAiOjE2NTUxMjQ1NTYsImF1ZCI6IndlYm1vYmlsZSIsInQiOiJ1IiwibyI6MTAxNX0.Be1A4HOFRAUp550_K4KL-PZSeh7hQkz_xVsATBqCM7Lm2800tDuOrIPflLW1I-88Kt_VD-VnizK_xVN1Mb4gAojpTVGqSQFhB9_E8gSYdgr97IJ8JPAx6OoMdIa2K4Qrg_IU64fYw4O06eZXlW8WOtqX-WAWggQrOEMyWACmq21nvFwawYM1Jrp6MB2MupKQZ9wCEPiTAa-rjq6ggVSAHr3OSEQGbXlLvMCCRkLp4AvT3JRWOcEBEeq35XDnOdqMLaZPPuFf5yy6nQwPZT8jwTzQi0qOdWPARjIAKcnEXLgpBQqokQFjc13YKIYpaXzXCVcRMl5HSSy01AJ7MqOv1Q; r=yDpWJidQZ+sAySIePPU7VppmdgMRCG8SqQ+xHQgAgcWZ0LDtS1taxiCf7EDV9E1d; pwaconsent=v:1.0~required:1&clf:1,cli:1,gfb:1,gtm:1,jot:1,ocx:1|comfort:1&baz:1,cne:1,fix:1,gfa:1,gfc:1,goa:1,gom:1,grc:1,grv:1,lob:1,opt:1,orc:1,ore:1,prd:1,sen:1,sis:1,spe:1,sst:1,swo:1,twi:1,usw:1,usz:1,yte:1|marketing:1&asm:1,cad:1,cma:1,eam:1,fab:1,fbn:1,gad:1,gam:1,gcm:1,gdv:1,gos:1,gse:1,gst:1,kru:1,msb:1,omp:1,pin:1,ttd:1,twt:1|; _gcl_au=1.1.774652435.1653914961; _gid=GA1.2.541576144.1653914961; _pin_unauth=dWlkPU56azJZVGs0WXpjdFpqVXhOaTAwTlRVekxXRmhZbUl0TVRGa04yRXpOamxsTW1WbA; __cf_bm=nC.KeDREtIq0CxYIHSInxhV_84MbsvUsXXQaXUqDqPA-1653970033-0-AW06xZCbiIVaU7ZgDC36R1Eu6qBzkcZRZR260zxWeYe1HtKIO/pkwiNWuggvTA7MUVqC+zmCxCb5qsQlRvQ7OwmIvY4L/aPSTAtpZyPPAOAG; ts_id=68be962d-2906-47b4-82c1-13903b48064b; abhomeab=B; s_id=58ba4561-c122-48f4-b3d5-a0e2ea87dc7d; MC_PS_SESSION_ID=58ba4561-c122-48f4-b3d5-a0e2ea87dc7d; p_id=58ba4561-c122-48f4-b3d5-a0e2ea87dc7d; MC_PS_USER_ID=58ba4561-c122-48f4-b3d5-a0e2ea87dc7d; t_fpd=true; __cfruid=1a5cda8ed42dc9c35762d5646377d4bd0c7fd7ae-1653970038; lux_uid=165397003906229078; NoCookie=true; BVBRANDID=4273feeb-df0a-4fe1-ab57-884a32c2add2; BVBRANDSID=4524fb21-3e50-4ee4-8920-0ae933a45fb7; _clck=16zo6gw|1|f1x|0; _msbps=98; _ga=GA1.2.639b70cf-d794-475c-8297-dba226e2f1b7; _uetsid=ecea1860e01611ec90c8b763030d21d4; _uetvid=ecea33f0e01611ec901847a194851ed5; _clsk=1cxfqbu|1653970107569|1|0|e.clarity.ms/collect; _ga_9ZJL7DLSGD=GS1.1.1653970040.9.1.1653970115.60',
#         # 'referer': 'https://www.saturn.de/de/category/laptops-66.html?ga_query=laptop&ga_queryHash=5eec0dc419aa8337bf725f026fda9c78c1cb1c642eeaff9d6e1112f37783e942&ga_queryRequestId=5eec0dc419aa8337bf725f026fda9c78c1cb1c642eeaff9d6e1112f37783e942',
#         'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
#         'sec-ch-ua-mobile': '?0',
#         'ec-ch-ua-platform': '"Windows"',
#         'sec-fetch-dest': 'empty',
#         'ec-fetch-mode': 'cors',
#         'sec-fetch-site': 'same-origin',
#         'user-agent': get_useragent(),
#         'x-cacheable': 'true',
#         # 'x-flow-id': '84091fd5-796c-45dd-9b51-c7708d79caa2',
#         'x-mms-country': 'DE',
#         'x-mms-language': 'de',
#         'x-mms-salesline': 'Saturn',
#         # 'x-operation': 'CategoryV4'
#     }
#
#     proxy_host = "proxy.zyte.com"
#     proxy_port = "8011"
#     proxy_auth = "6500c987aae7435a90c249b35b1c9376:"
#
#     proxies = {"https": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port),
#                "http": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port)}
#
#     handle_httpstatus_list=[503,429]
#     RETRY_HTTP_CODES = [429,403]
#
#     def start_requests(self):
#
#         cursor = UgamSaturnCategoryPipeline.cursor
#         con = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name)
#
#         try:
#             # brand_select = f"-- select Id,Category_url from {db_category_table} where Status = 'Pending' AND ID BETWEEN {self.start} AND {self.end}"
#             brand_select = f"select Id,Category_url from {db_category_table} where Status = 'Pending'"
#             cursor.execute(brand_select)
#             category_list=cursor.fetchall()
#             # category_list = [column for column in cursor.fetchall()]
#
#             for cat_item in category_list:
#                 cat_row_id = cat_item[0]
#                 cat_url = cat_item[1]
#
#                 # TODO  -----delete duplicate data in link data table with brand id----- """
#                 delete_duplicate_row = f"delete from {db_data_table} where cat_id like {cat_row_id}"
#                 cursor.execute(delete_duplicate_row)
#                 con.commit()
#
#                 page_no = 1
#                 meta_dict = {
#
#                     'cat_url': cat_url,
#                     'cat_row_id': cat_row_id,
#                     'page_no': page_no,
#                     'counter': 0,
#                 }
#                 if cat_row_id == 1:
#                     url='https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_2582","page":1,"experiment":"mp","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"be8d5bf908c10bee725d49531ef357bd55c44ff67d0eb9b8412b54b29f033919"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
#                 elif cat_row_id==2:
#                     url = 'https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_5197","page":1,"experiment":"mp","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"be8d5bf908c10bee725d49531ef357bd55c44ff67d0eb9b8412b54b29f033919"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
#                 elif cat_row_id==3:
#                     url = 'https://www.saturn.de/api/v1/graphql?operationName=SearchV4&variables={"hasMarketplace":true,"isRequestSponsoredSearch":true,"maxNumberOfAds":2,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"categoryIds":"CAT_DE_SAT_1","experiment":"mp","filters":["brand:APPLE"],"page":1,"query":"Mac","sessionId":"aa0c43f3-eefe-44ec-a270-852dae0dde21","customerId":"aa0c43f3-eefe-44ec-a270-852dae0dde21","pageType":"Search","productFilters":[["brand:APPLE"]]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"9fb05c43e35132d1652195e729b67ea5bffe51ed3f87338aeaceafd29004b150"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
#                 elif cat_row_id==4:
#                     url = 'https://www.saturn.de/api/v1/graphql?operationName=SearchV4&variables={"hasMarketplace":true,"isRequestSponsoredSearch":true,"maxNumberOfAds":2,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"categoryIds":"CAT_DE_SAT_66","experiment":"mp","filters":["brand:APPLE"],"page":1,"query":"MacBook+Pro -maus","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Search","productFilters":[["brand:APPLE"]]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"83b9064b116df6b3005cf26e456e99151aa2dc76533cfe4396fb919597eaeadf"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
#                 elif cat_row_id==5:
#                     url = 'https://www.saturn.de/api/v1/graphql?operationName=SearchV4&variables={"hasMarketplace":true,"isRequestSponsoredSearch":true,"maxNumberOfAds":2,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"categoryIds":"CAT_DE_SAT_66","experiment":"mp","filters":["brand:APPLE"],"page":1,"query":"MacBook+Air -maus","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Search","productFilters":[["brand:APPLE"]]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"83b9064b116df6b3005cf26e456e99151aa2dc76533cfe4396fb919597eaeadf"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
#                 elif cat_row_id==6:
#                     url = 'https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_106","page":1,"experiment":"mp","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"be8d5bf908c10bee725d49531ef357bd55c44ff67d0eb9b8412b54b29f033919"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
#                 elif cat_row_id==7:
#                     url = 'https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_83","page":1,"experiment":"mp","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"be8d5bf908c10bee725d49531ef357bd55c44ff67d0eb9b8412b54b29f033919"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
#                 elif cat_row_id==8:
#                     url = 'https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_66","page":1,"experiment":"mp","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"be8d5bf908c10bee725d49531ef357bd55c44ff67d0eb9b8412b54b29f033919"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
#                 elif cat_row_id==9:
#                     url = 'https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_105","page":1,"experiment":"mp","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"be8d5bf908c10bee725d49531ef357bd55c44ff67d0eb9b8412b54b29f033919"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
#
#                 else:
#                     print('id is not matching.....')
#                     logger.error('id is not matching.....')
#                     return None
#
#                 filename = f'/Cat_{cat_row_id}_Page_{page_no}.html'
#                 path = self.F_PATH + filename
#                 path = path.replace("\\", "/")
#
#                 if os.path.exists(path):
#                     with open(path, "r", encoding="utf-8")as f:
#                         reviewbody = f.read()
#                         re_text1 = reviewbody
#                 else:
#                     # print(url_zipcode)
#                     re = requests.get(url=url, headers=self.header, verify=False, proxies=self.proxies)
#                     re_text1 = re.text
#                     while re.status_code != 200:
#                         print("Review Response issue re-request ")
#                         re = requests.get(url=url, headers=self.header, verify=False, proxies=self.proxies)
#                         re_text1 = re.text
#                         with open(path, 'w', encoding="utf-8") as f:
#                             f.write(re_text1)
#                         time.sleep(3)
#                     else:
#                         if os.path.exists(path):
#                             pass
#                         else:
#                             with open(path, 'w', encoding="utf-8") as f:
#                                 f.write(re_text1)
#
#                 if os.path.exists(path):
#                     yield scrapy.FormRequest(url=f'file:///{path}', callback=self.parse,headers=self.header,meta={'meta_dict': meta_dict},dont_filter=True)
#
#         except Exception as e:
#             print(e)
#             logger.error('exception in start requests method main: {}'.format(e))
#
#
#     def parse(self, response, **kwargs):
#         meta_d=response.meta.get('meta_dict')
#         cat_rw_id=meta_d['cat_row_id']
#
#         print(cat_rw_id)
#         print("Status",response.status)
#
#         try:
#             meta_dict = response.meta.get('meta_dict')
#             cat_row_id = meta_dict.get('cat_row_id')
#             category_url = meta_dict.get('cat_url')
#             page_no = meta_dict.get('page_no')
#             counter = meta_dict.get('counter')
#
#             if '{' in response.text and '}' in response.text:
#                 page_data = json.loads(response.text)
#
#                 """ Count """
#                 if 'searchV4' in response.text:
#                     count = page_data['data']['searchV4']['totalProducts']
#                 else:
#                     count= page_data['data']['categoryV4']['totalProducts']
#
#                 filename = f'/Cat_{cat_row_id}_Page_{page_no}.html'
#                 path = self.F_PATH + filename
#                 path = path.replace("\\", "/")
#                 if os.path.exists(path):
#                     pass
#                 else:
#                     with open(path, 'wb') as f:
#                         f.write(response.body)
#
#
#                 Status_Flag = True
#
#                 # TODO -----check condition for search page or pagination page data is or not ----- """
#                 if 'data' in response.text:
#
#                     Exit_Flag = True
#
#                     # TODO -------get product link below for loop---------
#                     if 'categoryV4' in response.text:
#                         results = page_data['data']['categoryV4']['products']
#                     else:
#                         results = page_data['data']['searchV4']['products']
#
#                     if 'categoryV4' or 'searchV4' in response.text:
#                         for i in results:
#                             counter += 1
#                             product_url = 'https://www.saturn.de'+i['details']['url']
#
#                             # product_name=i['details']['title']
#                             # brand=i['details']['manufacturer']
#                             # product_id=i['productId']
#                             # ean=i['details']['ean']
#                             # markdownprice=i['price']['price']
#                             # lead_time=i['availability']['delivery']['latest']
#                             # product_description=i['details']['description']
#
#
#                             HtmlPath_search = str(path)
#                             cursor = UgamSaturnCategoryPipeline.cursor
#                             con = UgamSaturnCategoryPipeline.con
#                             sql = f'INSERT INTO {db_data_table}(`Product URL`,`Category_URL`,`HtmlPath_search`,`cat_id`,`cat_rank`) values("{product_url}","{category_url}","{HtmlPath_search}","{cat_row_id}","{counter}")'
#                             cursor.execute(sql)
#                             con.commit()
#                             print("inserted ..............", counter)
#                     else:
#                         Exit_Flag = False
#
#
#                     # TODO ...pagination here.... """
#
#                     try:
#                         if  counter <= count:
#                             page_no += 1
#                             if cat_row_id == 1:
#                                 page_link = 'https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_2582","page":pageno,"experiment":"mp","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"be8d5bf908c10bee725d49531ef357bd55c44ff67d0eb9b8412b54b29f033919"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
#                                 url = page_link.replace('pageno', str(page_no))
#                             elif cat_row_id == 2:
#                                 page_link = 'https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_5197","page":pageno,"experiment":"mp","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"be8d5bf908c10bee725d49531ef357bd55c44ff67d0eb9b8412b54b29f033919"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
#                                 url = page_link.replace('pageno', str(page_no))
#                             elif cat_row_id == 3:
#                                 page_link = 'https://www.saturn.de/api/v1/graphql?operationName=SearchV4&variables={"hasMarketplace":true,"isRequestSponsoredSearch":true,"maxNumberOfAds":2,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"categoryIds":"CAT_DE_SAT_1","experiment":"mp","filters":["brand:APPLE"],"page":pageno,"query":"Mac","sessionId":"aa0c43f3-eefe-44ec-a270-852dae0dde21","customerId":"aa0c43f3-eefe-44ec-a270-852dae0dde21","pageType":"Search","productFilters":[["brand:APPLE"]]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"9fb05c43e35132d1652195e729b67ea5bffe51ed3f87338aeaceafd29004b150"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
#                                 url = page_link.replace('pageno', str(page_no))
#                             elif cat_row_id == 4:
#                                 page_link = 'https://www.saturn.de/api/v1/graphql?operationName=SearchV4&variables={"hasMarketplace":true,"isRequestSponsoredSearch":true,"maxNumberOfAds":2,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"categoryIds":"CAT_DE_SAT_66","experiment":"mp","filters":["brand:APPLE"],"page":pageno,"query":"MacBook+Pro -maus","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Search","productFilters":[["brand:APPLE"]]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"83b9064b116df6b3005cf26e456e99151aa2dc76533cfe4396fb919597eaeadf"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
#                                 url = page_link.replace('pageno', str(page_no))
#                             elif cat_row_id == 5:
#                                 page_link = 'https://www.saturn.de/api/v1/graphql?operationName=SearchV4&variables={"hasMarketplace":true,"isRequestSponsoredSearch":true,"maxNumberOfAds":2,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"categoryIds":"CAT_DE_SAT_66","experiment":"mp","filters":["brand:APPLE"],"page":pageno,"query":"MacBook+Air -maus","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Search","productFilters":[["brand:APPLE"]]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"83b9064b116df6b3005cf26e456e99151aa2dc76533cfe4396fb919597eaeadf"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
#                                 url = page_link.replace('pageno', str(page_no))
#                             elif cat_row_id == 6:
#                                 page_link = 'https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_106","page":pageno,"experiment":"mp","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"be8d5bf908c10bee725d49531ef357bd55c44ff67d0eb9b8412b54b29f033919"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
#                                 url = page_link.replace('pageno', str(page_no))
#                             elif cat_row_id == 7:
#                                 page_link = 'https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_83","page":pageno,"experiment":"mp","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"be8d5bf908c10bee725d49531ef357bd55c44ff67d0eb9b8412b54b29f033919"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
#                                 url = page_link.replace('pageno', str(page_no))
#                             elif cat_row_id == 8:
#                                 page_link = 'https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_66","page":pageno,"experiment":"mp","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"be8d5bf908c10bee725d49531ef357bd55c44ff67d0eb9b8412b54b29f033919"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
#                                 url = page_link.replace('pageno', str(page_no))
#                             elif cat_row_id == 9:
#                                 page_link = 'https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_105","page":pageno,"experiment":"mp","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"be8d5bf908c10bee725d49531ef357bd55c44ff67d0eb9b8412b54b29f033919"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
#                                 url = page_link.replace('pageno', str(page_no))
#                             else:
#                                 print('id is not matching.....')
#                                 logger.error('id is not matching.....')
#                                 return None
#
#                             filename = f'/Cat_{cat_row_id}_Page_{page_no}.html'
#                             path = self.F_PATH + filename
#                             path = path.replace("\\", "/")
#
#                             meta_dict = {
#                                          'cat_row_id': cat_row_id,
#                                          'page_no': page_no,
#                                          'cat_url': category_url,
#                                          'counter': counter,
#                                          }
#
#                             proxy_host = "proxy.zyte.com"
#                             proxy_port = "8011"
#                             proxy_auth = "6500c987aae7435a90c249b35b1c9376:"
#                             proxies = {"https": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port),
#                                        "http": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port)}
#
#                             if os.path.exists(path):
#                                 with open(path, "r", encoding="utf-8")as f:
#                                     reviewbody = f.read()
#                                     re_text1 = reviewbody
#                             else:
#                                 # print(url_zipcode)
#                                 re = requests.get(url=url, headers=self.header, verify=False, proxies=proxies)
#                                 re_text1 = re.text
#                                 while re.status_code != 200:
#                                     print("Review Response issue re-request ")
#                                     re = requests.get(url=url, headers=self.header, verify=False, proxies=proxies)
#                                     re_text1 = re.text
#                                     with open(path, 'w', encoding="utf-8") as f:
#                                         f.write(re_text1)
#                                     time.sleep(3)
#                                 else:
#                                     if os.path.exists(path):
#                                         pass
#                                     else:
#                                         with open(path, 'w', encoding="utf-8") as f:
#                                             f.write(re_text1)
#
#                             if os.path.exists(path):
#                                 yield scrapy.FormRequest(url=f"file:///{path}", callback=self.parse,headers=self.header,
#                                                          meta={'meta_dict': meta_dict},dont_filter=True)
#                         else:
#                             Status_Flag = True
#                     except Exception as e:
#                         logger.error('exception in parse method for pagination:{}'.format(e))
#                 else:
#                     Status_Flag = False
#
#
#                 # statas flag for brands "Done or Not found"
#                 cursor = UgamSaturnCategoryPipeline.cursor
#                 con = UgamSaturnCategoryPipeline.con
#                 if Status_Flag:
#                     branch_sql = f'update {db_category_table} set Status = "Done", Count={counter} where id ="{cat_row_id}"'
#                     cursor.execute(branch_sql)
#                     con.commit()
#                 else:
#                     branch_sql = f'update {db_category_table} set Status = "Not found", Count={counter} where id ="{cat_row_id}"'
#                     cursor.execute(branch_sql)
#                     con.commit()
#             else:
#                 print("Wrong page response ..........")
#                 logger.info("Wrong page response..........")
#                 return None
#         except Exception as e:
#             print(e)
#             logger.error('exception in parse method main: {}'.format(e))
#
#     # def close(spider, reason):
#     #     cursor = UgamSaturnDePipeline.cursor
#     #     try:
#     #         print('spider is close,...................')
#     #         # print('going on QA and make csv..............')
#     #         cursor.execute('select * from category where status="Pending"')
#     #         rows = cursor.fetchall()
#     #         if rows == ():
#     #             print("Done with category..")
#     #         else:
#     #             print("Some remaining..")
#     #             return None
#
#     #     except Exception as e:
#     #         print('close spider error:{}'.format(e))
#
# if __name__ == '__main__':
#     from scrapy.cmdline import execute
#     execute('scrapy crawl santurn_de_category'.split())
