# # -*- coding: utf-8 -*-
# import hashlib
# import json
# import scrapy
# from mymodules._common_ import c_replace
# import re
# import json
# from scrapy import Selector
# from pymysql import OperationalError
#
# from ugam_lenovo_ca_price_daily.items import UgamLenovoCaPriceDailyItem
# from ugam_lenovo_ca_price_daily.pipelines import UgamLenovoCaPriceDailyPipeline
# from ugam_lenovo_ca_price_daily.config import *
# import time
# import requests
#
# headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
# 'cookie': 's_ecid=MCMID%7C15898899919205004223810527332888129364; aam_uuid=16048364323353588723797762463263119882; BVBRANDID=ea939c34-7761-41c4-a3f5-799ef3133ca0; split10=control; split=control; MSART_inen=PC%20%26%20TABLETS%7C%2Fin%2Fen%2Fpc; _fbp=fb.1.1626500304186.51578466; _mkto_trk=id:026-ENO-001&token:_mch-lenovo.com-1626500305347-83106; _gcl_au=1.1.1544956528.1626500306; QuantumMetricUserID=9bbc39a63e7bb533117aa506897589d4; _uetvid=34d06ca0e6c111eb8ec817c8f6d7cedf; _ga_EYNZYSHSG4=GS1.1.1626502831.2.1.1626504272.59; MSART_auen=PC%20%26%20TABLETS%7C%2Fau%2Fen%2Fpc; _caid=58d312ae-9b15-4e06-8a9c-d911669e39d3; _ga=GA1.2.1915923925.1626500306; _gid=GA1.2.870382769.1627560453; ki_r=; sn.vi=6b2ab0d3-0c13-45f2-8c85-ec3470f54875; sn.tpc=1; LOSAD=1; p3094257258_done=1; cto_bundle=KY0VYl9odElETWpxQmNDOGRpOTZSSFBwalliJTJCcjJzT3l5c25UcDFjekE5bHdDd0FrTDYzM0N5UUdXeEIwVSUyQjZBSWQlMkJVOTRJUk5wUjN4blRiaHdGcUYlMkJSTzklMkJQYkJMQm8lMkZ5N0tzbVBOTGZHVW9FTXZESWJVaDRhJTJCQnIza1NQWkJNVUczc09XJTJCQmMzdE53TXBqMGRqWlVpbExRJTNEJTNE; LSESSION=CC8D5525-9A43-44CF-8C0C-22E30002FDF4; at_check=true; AMCVS_F6171253512D2B8C0A490D45%40AdobeOrg=1; s_eng_rfd=0.00; s_cc=true; ki_t=1627560453132%3B1627618041581%3B1627618041581%3B2%3B16; inside-au=939712676-9dfefa9c79e9da14e01b630d5f4e35e654337fdeb1a1414be2c60cbae93854ae-0-0; _abck=F8FAB10D4992DFC7E46A7EFAD060EC8E~0~YAAQp13SF+X+P516AQAA/Hp99gZY1LqmDE2Pu2dUik7X2V8+kum1aNpKN3bol6qWSD0IMrJXpelS8cibP+AM8FGlee3VB2zJV5owF1qOrfzW1VBXZ8LeRxWZQX6C5FlfBazmNDQC9N3SGLfW1AuGlFLbscXft5xuf/UYirCvxqTm67Vh/0nB3YmZg3zZathX6IwG0p2z9gD20BbFur85/0pKKLwnogybeeL8h80vSQkdnfqchQ2csvWLpxo/0MsEQf3h0ZChZC6HFtCni1zsRTfBvQRcQ2auqt0FXCSjyRUUawj9J9F6vD4u6febRIqLFx6Q+M5BtxZbVSbmzMOmamdp1I0Xj4tuZw6SnjGx0zCb4tiDhIVrDMa4016jtfM90ZN9uzc6YAlr8aJ4LrNU4IxzMKp9lacY~-1~-1~-1; bm_sz=2F7D04E875DCADEE633F1018AC2AAB1F~YAAQp13SF+f+P516AQAA/Hp99gwFOxhW6OB+Qs+ACwv3Rv0I5LeHH9kS21ePhEtH/ofyCGpEvbrFTW/A4ty6JEWaPXYn38SNVma7WWdovS+AZALJSMVJgUIfyRF/ObWpclO9atbGzRhpuBFavmjZcLfszQ/QhlgJuGD7gc4AuQs9S4et2nPoi0L2Fy6zmRxWlXoPxXKVyE0vxauUcR9bA28QdMJq6jj7cSyGGvdJR7AShi7HUgZXyuZau2F63O9z4vTF4pqX9mvc6vQIX7FaDNAdgAowJF8piC0k7+9bvjj5xnU=~3749176~4339763; s_dfa=lenovomypub%2Clenovoglobal; s_inv=14963; s_ivc=true; s_vnc365=1659169000085%26vn%3D5; s_dur=1627633000087; AMCV_F6171253512D2B8C0A490D45%40AdobeOrg=-1124106680%7CMCIDTS%7C18838%7CMCMID%7C15898899919205004223810527332888129364%7CMCAAMLH-1628237800%7C12%7CMCAAMB-1628237800%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1627640200s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.2.0; ak_bmsc=B0428A59C349429AE2094075F52DEB0D~000000000000000000000000000000~YAAQp13SFwP/P516AQAAUIR99gzu/Ms57NbQyx+Isr3ypwPxVRRwGHM4npKf1gf6xGXPQo0wRHgYo+9jk0fOKKypNUaPVzdAaWFSYjfoPk7JEIbQuq0nijAb/Q8Jn64Qp3WPwYuvAM68GTtRa/eYFtHzk+ceYriFRPjIrAJf8BR73SPzM/66i0XLRKiqaSURWvpficMN5Dxe+aU65KiaH3h++W7YffcRLEinCWKfd8UKTNHLkjeYMyW+2sOG3dJabUckgyE2JmVZrmNMTqyZai5H7U72dxI353I0XLkZtwJ3L1vAEGISb7fouY3aAtR6pWYpTe5A/SrqcKlZZSdpxHZ+Bu0LjJp7zh07hw9s2GBSpnAYSDOtZLnJ03sXgiAQ4StIIlxhPc3RbkmLlNgnlrduCIwtPr+iWY7ApU3++qqb/2FSch/6Fg9gZRWtjLZbfQPx5KWpp8+RC/zMBTVCIwGWwNZuTwiylbIjgsI2pqOXoltIbkUsuscrThI=; BVBRANDSID=edc9a981-fd47-4421-ad71-e8d72b3893d8; MSART=PC%20%26%20Tablets%7C%2Fmy%2Fen%2Fpc; MSART_myen=PC%20%26%20Tablets%7C%2Fmy%2Fen%2Fpc; QuantumMetricSessionID=1b1946714d40353984ec5011be18fa30; AKA_A2=A; MSESSIONID=C1C1FDC4AEC50CA24836AA6CA0DC630D; JSESSIONID=17E397382F784EE637133F19A6044122.app6; s_eVar57=%3B82C10000MA; s_gpv=my_en%3Alaptops%3Alenovo%3Astudent-chromebooks%3Aideapad-3-cb-14igl05%3Ap%3A82c10000ma; s_sq=%5B%5BB%5D%5D; aam_sc=aamsc%3D11169887; s_tot_rfd=1.72; s_tslv=1627633355398; akavpau_WaitingRoomController=1627633713~id=2b7a5ab32cb542ad13057eb40051ae9f; bm_sv=15AD5B64C1BE28AECE821F603A261FDA~vnr/M/52AibNbA/HskXL7u4/XOnsDLI+eqE8XJ0A4xlRJpZx2RJBFKlU5M50egt8Sj8vU9SlZYaHJtKbbdw0935ALnYr+4aru/3Eo65sQWDawL35Yj1I3nMzvLQyWYz8GGpKEZ1kSz3VmubfNTqRdrSEb6KIGpkzG+Gp6yUGjGA=; aamtest1=seg%3Dabc%2Cseg%3Ddef%2Cseg%3Dghi; s_tp=7081; s_ppv=my_en%253Alaptops%253Alenovo%253Astudent-chromebooks%253Aideapad-3-cb-14igl05%253Ap%253A82c10000ma%2C3%2C3%2C184; utag_main=v_id:017ab2f9099600100d19f5abb3ed03073006d06b009dc$_sn:5$_se:6$_ss:0$_st:1627635157024$dc_visit:5$ses_id:1627633001802%3Bexp-session$_pn:6%3Bexp-session$criteo_sync:1%3Bexp-session$dc_event:6%3Bexp-session$dc_region:ap-east-1%3Bexp-session; inside-asia=584642970-fc40efe0ce27f17dfc361ff167ef4125a635cbaf37cbd8ee8647edcbd1b3523b-0-0; mbox=PC#7305ccfb39174bc6a179f89a388e80b6.38_0#1690877867|session#89c0e51c3a8e404a83472eeb2e20b90c#1627635219; RT="z=1&dm=lenovo.com&si=df4569b1-1e78-46f3-8cd2-67af4bff7039&ss=krq2nv4q&sl=5&tt=5pc&bcn=%2F%2F6852bd0a.akstat.io%2F&ld=7omz&ul=7tuv"',
# 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}
#
# class ProductSpider(scrapy.Spider):
#     handle_httpstatus_list = [404]
#
#     name = 'lenovo_ca_product'
#
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
#         try:
#             self.cursor = UgamLenovoCaPriceDailyPipeline.cursor
#             self.con = UgamLenovoCaPriceDailyPipeline.con
#
#             sql_query = f"select `id`,`Product ID`,`Product URL` from {db_data_table} where Status = 'Pending' AND ID BETWEEN {self.start} AND {self.end}"
#             # sql_query = f"select `id`,`Product ID`,`Product URL` from {db_data_table} where Status = 'Pending' and id between 1 and 100"
#             self.cursor.execute(sql_query)
#
#             core_list = [column for column in self.cursor.fetchall()]
#
#             for itm in core_list:
#                 try:
#                     time.sleep(1)
#                     row_id = itm[0]
#                     Product_ID = itm[1]
#                     Product_URL = itm[2]
#
#                     meta_dict = {'row_id': row_id,
#                                  'Product_ID': Product_ID,
#                                  'Product_URL': Product_URL
#                                  }
#
#                     filename = f'/{Product_ID}.html'
#                     path = self.F_PATH + filename
#
#                     if os.path.exists(path):
#                         yield scrapy.FormRequest(url=f'file:///{path}', callback=self.parse, headers=headers, dont_filter=True,
#                                                  meta={"meta_dict": meta_dict})
#                     else:
#                         yield scrapy.FormRequest(url=Product_URL, callback=self.parse, headers=headers, dont_filter=True,
#                                                  meta={"meta_dict": meta_dict})
#                 except Exception as e:
#                     logger.error('start requests method error in sku for loop: {}'.format(e))
#         except Exception as e:
#             logger.error('start requests method error in main: {}'.format(e))
#
#     def parse(self, response):
#         try:
#             if "</html>" in str(response.body) and response.xpath('//div[@class="o-mastheadModule__logo"]'):
#                 print("||----------------------------------------------------------------------------------------||")
#                 catpdp.intialize_variable()
#
#                 meta_dict = response.meta.get('meta_dict')
#                 row_id = meta_dict.get('row_id')
#                 product_url = meta_dict.get('Product_URL')
#                 Product_ID = meta_dict.get('Product_ID')
#                 catpdp.Product_space_URL = product_url.replace("\'", "\'\'")
#
#                 """ Product ID """
#                 catpdp.Product_space_ID = c_replace(Product_ID)
#
#                 filename = f'/{Product_ID}.html'
#                 path = self.F_PATH + filename
#                 path = path.replace("\\", "/")
#                 if os.path.exists(path):
#                     pass
#                 else:
#                     with open(path, 'wb') as f:
#                         f.write(response.body)
#
#                 """ HtmlPath """
#                 catpdp.htmlpath = path
#
#                 """ Date of Crawl """
#                 catpdp.Date_space_of_space_Crawl = datetime.today().strftime('%m/%d/%Y %H:%M:%S')
#
#                 """ Retailer """
#                 catpdp.Retailer = "Lenovo.CA"
#
#                 """ Product Title """
#                 try:
#                     product_title = response.xpath('//h1//text()').get()
#                     if product_title:
#                         catpdp.Product_space_Title = c_replace(product_title)
#                     else:
#                         catpdp.Product_space_Title = 'n/a'
#                 except Exception as e:
#                     logger.info("Error in scrape header Product Title : {}".format(e))
#                     return None
#
#                 """ List Price """
#                 try:
#                     list_price = response.xpath("""//dl[@id="builderPricingSummary"]//dd[contains(@data-pricetypevalue,"webPrice-WEBPRICE")]//text()""").get()
#                     if list_price:
#                         catpdp.List_space_Price = str(c_replace(list_price).replace('$', ''))
#                     elif response.xpath('//div[contains(text(),"Web Price")]//span/strike//text()'):
#                         list_price = response.xpath('//div[contains(text(),"Web Price")]//span/strike//text()').get()
#                         catpdp.List_space_Price = str(c_replace(list_price).replace('$', ''))
#                     elif response.xpath('//dd[contains(text(),"List price")]//text()'):
#                         list_price = response.xpath('//dd[contains(text(),"List price")]//text()').get()
#                         catpdp.List_space_Price = str(c_replace(list_price).replace('$', '').replace('List price: $', ''))
#                     else:
#                         catpdp.List_space_Price = 'n/a'
#                 except Exception as e:
#                     logger.info("Error in scrape header List Price : {}".format(e))
#                     return None
#
#                 """ Markdown Price """
#                 try:
#                     markdown_price = response.xpath("""//dl[@id="builderPricingSummary"]//dd[contains(@data-pricetypevalue,"potentialDiscountedPrice-SALESPRICE")]//text()""").get()
#                     if markdown_price:
#                         catpdp.Markdown_space_Price = str(c_replace(markdown_price).replace('$', ''))
#                     elif response.xpath('//dl[@id="builderPricingSummary"]//dd[contains(@data-pricetypevalue,"potentialCouponPrice-COUPONPRICE")]//text()'):
#                         markdown_price = response.xpath('//dl[@id="builderPricingSummary"]//dd[contains(@data-pricetypevalue,"potentialCouponPrice-COUPONPRICE")]//text()').get()
#                         catpdp.Markdown_space_Price = str(c_replace(markdown_price).replace('$', ''))
#                     elif response.xpath('//dt[contains(text(),"After Instant Savings")]//following-sibling::dd//text()'):
#                         markdown_price = response.xpath('//dt[contains(text(),"After Instant Savings")]//following-sibling::dd//text()').get()
#                         catpdp.Markdown_space_Price = str(c_replace(markdown_price).replace('$', ''))
#                     elif response.xpath('//dd[contains(text(),"Sale price")]//text()'):
#                         markdown_price = response.xpath('//dd[contains(text(),"Sale price")]//text()').get()
#                         catpdp.Markdown_space_Price = str(c_replace(markdown_price).replace('$', '').replace('Sale price: $', ''))
#                     else:
#                         catpdp.Markdown_space_Price = 'n/a'
#                 except Exception as e:
#                     logger.info("Error in scrape header Markdown Price : {}".format(e))
#                     return None
#
#                 if catpdp.Markdown_space_Price == 'n/a':
#                     catpdp.Markdown_space_Price = catpdp.List_space_Price
#                     catpdp.List_space_Price = 'n/a'
#
#                 if catpdp.List_space_Price == 'n/a' and catpdp.Markdown_space_Price == 'n/a':
#                     try:
#                         price_headers = {
#                             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.3'
#                         }
#
#                         price_req = 'https://www.lenovo.com/ca/en/thinkvisionM14/p/61DDUAR6US/singlev2/price/json'
#                         req = requests.get(url=price_req, headers=price_headers)
#                         # print(req.text)
#                         price_data = eval(req.text)
#                         list_price = price_data.get('price')
#                         if list_price:
#                             catpdp.List_space_Price = c_replace(list_price)
#                         else:
#                             catpdp.List_space_Price = 'n/a'
#                         markdown_price = price_data.get('potentialDiscountedPrice')
#                         if markdown_price:
#                             catpdp.Markdown_space_Price = c_replace(markdown_price)
#                         else:
#                             catpdp.Markdown_space_Price = 'n/a'
#                     except Exception as e:
#                         logger.info("Error in price req : {}".format(e))
#                         return None
#
#                 """ Seller Name """
#                 catpdp.Seller_space_Name = 'n/a'
#
#                 """ Stock Status """
#                 try:
#                     if response.xpath('//span[contains(text(),"Temporarily Unavailable")]'):
#                         catpdp.Stock_space_Status = 'Out of Stock'
#                     elif response.xpath(
#                             "//span[contains(text(),'The product you are looking for is no longer available')]"):
#                         catpdp.Stock_space_Status = 'Out of Stock'
#                     elif response.xpath('//span[@class="stock_message"]//text()'):
#                         Stock_Status = response.xpath('//span[@class="stock_message"]//text()').get()
#                         if "Out of Stock" in Stock_Status or "out of stock" in Stock_Status:
#                             catpdp.Stock_space_Status = 'Out of Stock'
#                         elif "Only few left" in Stock_Status or "only few left" in Stock_Status:
#                             catpdp.Stock_space_Status = 'In Stock'
#                         else:
#                             catpdp.Stock_space_Status = 'In Stock'
#                     elif response.xpath("//button[contains(text(),'Customize')]"):
#                         catpdp.Stock_space_Status = 'In Stock'
#                     elif response.xpath("//button[contains(text(),'Add to cart')]//text()"):
#                         Stock_Status = response.xpath("//button[contains(text(),'Add to cart')]//text()").get()
#                         if "Add to cart" in Stock_Status or "add to cart" in Stock_Status:
#                             catpdp.Stock_space_Status = 'In Stock'
#                         else:
#                             return None
#                     elif response.xpath('//button[@id="addToCartButtonTop"]//text()'):
#                         Stock_Status = response.xpath('//button[@id="addToCartButtonTop"]//text()').getall()
#                         if "add to cart" in (''.join(c_replace(Stock_Status))).lower():
#                             catpdp.Stock_space_Status = 'In Stock'
#                         else:
#                             return None
#                     else:
#                         catpdp.Stock_space_Status = 'Out of Stock'
#                 except Exception as e:
#                     logger.error("Error in scrape header Stock Status at url :{} {}".format(e, product_url))
#                     return None
#
#                 """ Lead time """
#                 try:
#                     lead_time = response.xpath('//div[contains(@id,"deliveryTimeHolder")]//text()').get()
#                     if lead_time:
#                         lead_time = c_replace(lead_time)
#                         if "call for availability" not in lead_time.lower():
#                             catpdp.Lead_space_time = c_replace(lead_time)
#                         else:
#                             catpdp.Lead_space_time = 'n/a'
#                     else:
#                         catpdp.Lead_space_time = 'n/a'
#                 except Exception as e:
#                     logger.info("Error in scrape header Lead time : {}".format(e))
#                     return None
#
#                 """ status """
#                 catpdp.status = "Done"
#
#                 """ Update_productdata_Query """
#                 updateproduct = catpdp.Update_productdata_Query()
#                 # print(updateproduct)
#                 self.cursor.execute(updateproduct)
#                 self.con.commit()
#
#             else:
#                 print("something went wrong, check properly.........")
#                 logger.info("something went wrong, check properly.........")
#                 return None
#                 # print("Product Not found, Status code:{}".format(response.status))
#                 # meta_dict = response.meta.get('meta_dict')
#                 # row_id = meta_dict.get('row_id')
#                 # product_url = meta_dict.get('product_url')
#                 # catpdp.status = "Not Found"
#                 #
#                 # catpdp.Date_space_of_space_Crawl = datetime.today().strftime('%m/%d/%Y %H:%M:%S %p')
#                 # catpdp.Product_space_URL = product_url
#                 # catpdp.Product_space_ID = 'n/a'
#                 # catpdp.cat_id = str(row_id).encode('ascii', 'ignore').decode("utf-8")
#                 # catpdp.HtmlPath_search = meta_dict.get('HtmlPath_search')
#                 # catpdp.category_url = meta_dict.get('category_url')
#                 # catpdp.cat_rank = str(meta_dict.get('cat_rank'))
#                 # catpdp.Retailer = "amazon.fr"
#                 # catpdp.Brand = 'n/a'
#                 # catpdp.Product_space_Title = 'n/a'
#                 # catpdp.Image_space_URL = 'n/a'
#                 # catpdp.MPN = 'n/a'
#                 # catpdp.List_space_Price = 'n/a'
#                 # catpdp.Markdown_space_Price = 'n/a'
#                 # catpdp.Seller_space_Name = 'n/a'
#                 # catpdp.Stock_space_Status = 'n/a'
#                 # catpdp.Product_space_Description = 'n/a'
#                 # catpdp.Product_space_Specification = 'n/a'
#                 # catpdp.Product_space_Features = 'n/a'
#                 # catpdp.Lead_space_time = 'n/a'
#                 #
#                 # filename = f'/Not_Found_id_{row_id}.html'
#                 # path = self.F_PATH + filename
#                 # path = path.replace("\\", "/")
#                 # if not os.path.exists(path):
#                 #     with open(path, 'wb') as f:
#                 #         f.write(response.body)
#                 #
#                 # catpdp.htmlpath = path
#                 # """ Update_productdata_Query """
#                 # updateproduct = catpdp.Update_productdata_Query()
#                 # # print(updateproduct)
#                 # self.cursor.execute(updateproduct)
#                 # self.con.commit()
#
#         except Exception as e:
#             import sys
#             exception_type, exception_object, exception_traceback = sys.exc_info()
#             filename = exception_traceback.tb_frame.f_code.co_filename
#             line_number = exception_traceback.tb_lineno
#             logger.error("parse main error: {}".format(e))
#             exception_type, exception_object, exception_traceback = sys.exc_info()
#             filename = exception_traceback.tb_frame.f_code.co_filename
#             line_number = exception_traceback.tb_lineno
#             logger.error('line---:{}'.format(sys.exc_info()))
#             logger.error("Exception type: {}".format(exception_type))
#             logger.error("File name: {}".format(filename))
#             logger.error("Error is:{} ".format(e))
#             logger.error("Line number: {}:".format(line_number))
#
#     def close(spider, reason):
#
#         try:
#             sql = f"SELECT id FROM {db_data_table} where status='Pending'"
#             # brand_pend = f"SELECT id FROM {db_category_table} where status='Pending'"
#             cursor = UgamLenovoCaPriceDailyPipeline.cursor
#             cursor.execute(sql)
#             linkdata_row = cursor.fetchall()
#             # cursor.execute(brand_pend)
#             # brand_row = cursor.fetchall()
#
#             if linkdata_row == ():
#                 print('spider is close,...................')
#                 print('going on QA and make csv..............')
#                 print("Going to make CSV..")
#                 from ugam_lenovo_ca_price_daily.export_csv import Export_Csv
#                 c = Export_Csv()
#                 c.export_csv()
#                 print("CSV Done..")
#             else:
#                 ...
#             # spider.start_requests()
#             # ESpiderSpider.start_requests(self='')
#             # execute('scrapy crawl emag -a start=120 -a end=120'.split())
#         except Exception as e:
#             logger.error('error in close spider method error :{}'.format(e))
#
# #
# # from scrapy.cmdline import execute
# # # execute('scrapy crawl lenovo_ca_product'.split())
# # execute('scrapy crawl lenovo_ca_product -a start=46 -a end=46'.split())
