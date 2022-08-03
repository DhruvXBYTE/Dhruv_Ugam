# import hashlib
# import json
# import scrapy
# from mymodules._common_ import c_replace
# import re
# import json
# from scrapy import Selector
# from pymysql import OperationalError
#
# from ugam_saturn_de.items import *
# from ugam_saturn_de.pipelines import *
# from ugam_saturn_de.config import *
# import time
# import requests
#
# headers={
#
#     'authority': 'www.saturn.de',
#     'method':'GET',
#     'scheme': 'https',
#     'accept': 'text/html,applicatin/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'accept-language':'en-GB,en-US;q=0.9,en;q=0.8',
#     'cache-control': 'no-cache',
#     'cookie': 'optid=3d8c3824-eb71-4464-86e3-06285ac19494; a=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im8yc2lnbiJ9.eyJzdWIiOiI2MjM0ZDc5MS00ODBiLTQ1OWQtYmZmYi01ZDdkOTJhMzkxZmIiLCJpc3MiOiJtbXNlIiwiaWF0IjoxNjUzOTE0OTU2LCJleHAiOjE2NTUxMjQ1NTYsImF1ZCI6IndlYm1vYmlsZSIsInQiOiJ1IiwibyI6MTAxNX0.Be1A4HOFRAUp550_K4KL-PZSeh7hQkz_xVsATBqCM7Lm2800tDuOrIPflLW1I-88Kt_VD-VnizK_xVN1Mb4gAojpTVGqSQFhB9_E8gSYdgr97IJ8JPAx6OoMdIa2K4Qrg_IU64fYw4O06eZXlW8WOtqX-WAWggQrOEMyWACmq21nvFwawYM1Jrp6MB2MupKQZ9wCEPiTAa-rjq6ggVSAHr3OSEQGbXlLvMCCRkLp4AvT3JRWOcEBEeq35XDnOdqMLaZPPuFf5yy6nQwPZT8jwTzQi0qOdWPARjIAKcnEXLgpBQqokQFjc13YKIYpaXzXCVcRMl5HSSy01AJ7MqOv1Q; r=yDpWJidQZ+sAySIePPU7VppmdgMRCG8SqQ+xHQgAgcWZ0LDtS1taxiCf7EDV9E1d; pwaconsent=v:1.0~required:1&clf:1,cli:1,gfb:1,gtm:1,jot:1,ocx:1|comfort:1&baz:1,cne:1,fix:1,gfa:1,gfc:1,goa:1,gom:1,grc:1,grv:1,lob:1,opt:1,orc:1,ore:1,prd:1,sen:1,sis:1,spe:1,sst:1,swo:1,twi:1,usw:1,usz:1,yte:1|marketing:1&asm:1,cad:1,cma:1,eam:1,fab:1,fbn:1,gad:1,gam:1,gcm:1,gdv:1,gos:1,gse:1,gst:1,kru:1,msb:1,omp:1,pin:1,ttd:1,twt:1|; _gcl_au=1.1.774652435.1653914961; _gid=GA1.2.541576144.1653914961; _pin_unauth=dWlkPU56azJZVGs0WXpjdFpqVXhOaTAwTlRVekxXRmhZbUl0TVRGa04yRXpOamxsTW1WbA; NoCookie=true; t_fpd=true; s_id=f0751285-9373-405f-8cf5-64c3757331a6; MC_PS_SESSION_ID=f0751285-9373-405f-8cf5-64c3757331a6; p_id=f0751285-9373-405f-8cf5-64c3757331a6; MC_PS_USER_ID=f0751285-9373-405f-8cf5-64c3757331a6; __cfruid=4d814b86914410e679ff531751b35c8c4325a56d-1654148724; _clck=16zo6gw|1|f1z|0; ts_id=53ba3848-7f66-4e6e-a8ad-b6ba12b3a6c6; _msbps=95; __cf_bm=42Xg6ru12HcHIaxM_Xj7FH0VKQ6a98YVqnWOYKLXBEs-1654159670-0-ASjrpq9erEVTW3m9I2WZagTikMQjkZhZ+WtLOdcnTWf7ZJ1Dg3vlJ/o+sX1rKhS6j0f1QFhIOz/+oEk8FvR5P1CWG5Yey8DgzWquvG/qWXR1; lux_uid=165416010751407882; _dc_gtm_UA-25101917-1=1; _ga=GA1.1.639b70cf-d794-475c-8297-dba226e2f1b7; _ga_9ZJL7DLSGD=GS1.1.1654160108.25.0.1654160108.60; _uetsid=ecea1860e01611ec90c8b763030d21d4; _uetvid=ecea33f0e01611ec901847a194851ed5; BVBRANDID=edfb344a-dffd-4ba6-88ac-b3ce38a334a4; BVBRANDSID=cfa982a5-202e-49e0-8624-1d4db7e6d83c; _clsk=1q01wa|1654160114076|1|1|a.clarity.ms/collect',
#     'pragma': 'no-cache',
#     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'none',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'
#
# }
#
# class Productsmonitor(scrapy.Spider):
#
#
#     name = 'monitor_product'
#     F_PATH = HTML
#
#     def __init__(self, start='', end=''):
#         try:
#             self.start = start
#             self.end = end
#         except Exception as e:
#             logger.error('spider in __init__ method error :{}'.format(e))
#             print('__init__ error:', e)
#
#     def start_requests(self):
#
#         try:
#             self.cursor = UgamSaturnDePipeline.cursor
#             self.con = UgamSaturnDePipeline.con
#             category_status = True
#             while category_status:
#                 self.cursor.execute('select * from category_mpn where status="Pending"')
#                 rows = self.cursor.fetchall()
#                 if rows == ():
#                     print("Done with category..")
#                     category_status = False
#                 else:
#                     print("Wait Category is not done----Please category of lenovo au--")
#                     time.sleep(100)
#                     category_status = True
#             sql_query = f"select id, `Product URL`, HtmlPath, cat_id, HtmlPath_search, category_url, cat_rank from {db_data_table} where Status = 'Pending' AND ID BETWEEN {self.start} AND {self.end}"
#             # sql_query = f"-- select id, `Product URL`, HtmlPath, cat_id, HtmlPath_search, category_url, cat_rank from {db_data_table} where Status = 'Pending' and id between 1 and 100"
#             self.cursor.execute(sql_query)
#
#             core_list = [column for column in self.cursor.fetchall()]
#
#             for itm in core_list:
#                 try:
#                     time.sleep(1)
#                     row_id = itm[0]
#                     product_url = itm[1]
#                     HtmlPath = itm[2]
#                     cat_id = itm[3]
#                     HtmlPath_search = itm[4]
#                     category_url = itm[5]
#                     cat_rank = itm[6]
#
#                     nw_product_id = c_replace(product_url.split('-')[-1])
#                     product_id=nw_product_id.split('.')[0]
#                     # print(nw_product_id)
#                     filename = f'/{product_id}.html'
#                     path = self.F_PATH + filename
#                     path = path.replace("\\", "/")
#
#                     meta_dict = {'product_url': product_url,
#                                  'row_id': row_id,
#                                  'cat_id': cat_id,
#                                  'HtmlPath_search': HtmlPath_search,
#                                  'category_url': category_url,
#                                  'cat_rank': cat_rank,
#                                  'product_id': product_id}
#
#                     if os.path.exists(path):
#                         yield scrapy.FormRequest(url=f'file:///{path}', callback=self.parse, headers=headers,
#                                                  dont_filter=True,
#                                                  meta={"meta_dict": meta_dict})
#                     else:
#                         yield scrapy.FormRequest(url=product_url, callback=self.parse, headers=headers,
#                                                  dont_filter=True,
#                                                  meta={"meta_dict": meta_dict})
#
#                 except Exception as e:
#                     logger.error('start requests method error in sku for loop: {}'.format(e))
#         except Exception as e:
#             logger.error('start requests method error in main: {}'.format(e))
#
#     def parse(self, response, **kwargs):
#         print(response.status)
#
#         try:
#             if "Not Found" in response.text:
#                 print("Product Not found, Status code:{}".format(response.status))
#                 meta_dict = response.meta.get('meta_dict')
#                 row_id = meta_dict.get('row_id')
#                 product_url = meta_dict.get('product_url')
#                 catpdp.status = "Not Found"
#
#                 catpdp.Date_space_of_space_Crawl = datetime.today().strftime('%m/%d/%Y %H:%M:%S %p')
#                 catpdp.Product_space_URL = product_url.replace("'", "\\'")
#                 print(catpdp.Product_space_URL)
#                 catpdp.Product_space_ID = 'n/a'
#                 catpdp.cat_id = str(row_id)
#                 catpdp.HtmlPath_search = meta_dict.get('HtmlPath_search')
#                 catpdp.category_url = meta_dict.get('category_url')
#                 catpdp.cat_rank = str(meta_dict.get('cat_rank'))
#                 catpdp.Retailer = "Lenovo.com"
#                 catpdp.Brand = 'n/a'
#                 catpdp.Product_space_Title = 'n/a'
#                 catpdp.Image_space_URL = 'n/a'
#                 catpdp.MPN = 'n/a'
#                 catpdp.List_space_Price = 'n/a'
#                 catpdp.Markdown_space_Price = 'n/a'
#                 catpdp.Seller_space_Name = 'n/a'
#                 catpdp.Stock_space_Status = 'n/a'
#                 catpdp.Product_space_Description = 'n/a'
#                 catpdp.Product_space_Specification = 'n/a'
#                 catpdp.Product_space_Features = 'n/a'
#                 catpdp.Lead_space_time = 'n/a'
#
#                 filename = f'/Not_Found_id_{row_id}.html'
#                 path = self.F_PATH + filename
#                 path = path.replace("\\", "/")
#                 if not os.path.exists(path):
#                     with open(path, 'wb') as f:
#                         f.write(response.body)
#
#                 catpdp.htmlpath = path
#                 """ Update_productdata_Query """
#                 updateproduct = catpdp.Update_productdata_Query()
#                 # print(updateproduct)
#                 self.cursor.execute(updateproduct)
#                 self.con.commit()
#
#             elif "</html>" in str(response.body):
#
#                 print("||----------------------------------------------------------------------------------------||")
#                 catpdp.intialize_variable()
#
#                 meta_dict = response.meta.get('meta_dict')
#                 row_id = meta_dict.get('row_id')
#                 product_url = meta_dict.get('product_url')
#                 cat_id=meta_dict.get('cat_id')
#
#                 product_id = meta_dict.get('product_id')
#                 catpdp.Product_space_URL = product_url
#                 print(catpdp.Product_space_URL)
#
#                 """ Product ID """
#                 catpdp.Product_space_ID = c_replace(product_id)
#
#                 filename = f'/{product_id}.html'
#                 path = self.F_PATH + filename
#                 path = path.replace("\\", "/")
#
#                 if os.path.exists(path):
#                     pass
#                 else:
#                     with open(path, 'wb') as f:
#                         f.write(response.body)
#
#                 """ HtmlPath """
#                 catpdp.htmlpath = path
#
#                 """ cat_id """
#                 catpdp.cat_row_id = str(cat_id)
#
#                 """ HtmlPath_search """
#                 catpdp.HtmlPath_search = meta_dict.get('HtmlPath_search')
#                 """ category_url """
#                 catpdp.category_url = meta_dict.get('category_url')
#
#                 """ cat_rank """
#                 catpdp.cat_rank = str(meta_dict.get('cat_rank'))
#
#                 """ Date of Crawl """
#                 catpdp.Date_space_of_space_Crawl = datetime.today().strftime('%m/%d/%Y %H:%M:%S')
#
#                 """ Retailer """
#                 catpdp.Retailer = "Saturn.com"
#
#
#                 #TODO --------------- BRAND --------------------
#
#                 try:
#                     brand=response.xpath('//span[@class="BaseTypo-sc-1jga2g7-0 izkVco StyledInfoTypo-sc-1jga2g7-1 lTitt"]//following-sibling::a//text()').get()
#
#                     if brand:
#                         catpdp.Brand=brand
#                     else:
#                         catpdp.Brand="n/a"
#
#                 except Exception as e:
#                     print(e)
#
#                 # TODO --------------- Product_Title --------------------
#
#                 try:
#                     product_title=response.xpath('//h1[@class="BaseTypo-sc-1jga2g7-0 izkVco StyledInfoTypo-sc-1jga2g7-1 hrLodq"]//text()').get()
#
#                     if product_title:
#                         catpdp.Product_space_Title=c_replace(product_title)
#                     else:
#                         catpdp.Product_space_Title = "n/a"
#
#                 except Exception as e:
#                     print(e)
#
#                 # TODO --------------- Image_URL --------------------
#
#                 try:
#                     img_url=response.xpath('//div[@class="S-sc-1unnn6u-4 hwLaq"]//div[@class="StyledZoomImage-sc-1hbhoz7-0 diReke"]/picture/source/@srcset').get()
#                     print(img_url)
#
#                     if img_url:
#                         catpdp.Image_space_URL=c_replace(img_url)
#                     else:
#                         catpdp.Image_space_URL="n/a"
#
#                 except Exception as e:
#                     print(e)
#
#                 # TODO --------------- mpn_output --------------------
#
#                 try:
#                     mpn=response.xpath('//span[contains(text(),"Modelkennung")]//..//following-sibling::td//text()').get()
#
#                     if mpn:
#                         catpdp.MPN=c_replace(mpn)
#                     else:
#                         catpdp.MPN="n/a"
#                 except Exception as e:
#                     print(e)
#
#
#
#                 updateproduct = catpdp.Update_productdata_Query()
#                 print(updateproduct)
#                 self.cursor.execute(updateproduct)
#                 self.con.commit()
#
#         except Exception as e:
#             print(e)
#
# if __name__ == '__main__':
#     from scrapy.cmdline import execute
#     execute('scrapy crawl monitor_product -a start=1 -a end=10'.split())