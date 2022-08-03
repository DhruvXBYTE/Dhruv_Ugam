# import datetime
# from ugam_copple_mx.pipelines import *
# from ugam_copple_mx.config import *
# import scrapy
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from lxml import html
# import os
# import time
# import hashlib
# from mymodules._common_ import *
# import re
#
#
# class ugam_copple(scrapy.Spider):
#
#     name="ugam_prj"
#     headers={
#              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
#              'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
#              'sec-ch-ua-platform': '"Windows"'
#              }
#
#
#     def start_requests(self):
#
#         self.cursor=UgamCoppleMxPipeline.cursor
#         self.con=UgamCoppleMxPipeline.con
#
#         sql_query = f"select Id,Partner_ID,Partner_Name,Country,Scraping_Vendor_Name,Product_URL,Brand,`MPN/Model_Input`,Product_Line,Category,Subcategory,Scrape_Frequency,Additional_Header_2,Detailed_Partner_ID,`Feature Keywords_Indoor Air Quality`,Lookup_Keyword,Scrape_frequency,screenshotpath,`Feature Keywords_Security`,`Feature Keywords_Sustainability`,`Scrape_Phase`,`Feature Keywords_Quality`,`Product_specifications` from {product_data_table}"
#         print(sql_query)
#         self.cursor.execute(sql_query)
#
#         core_list=[clm for clm in self.cursor.fetchall()]
#
#         for itm in core_list:
#
#             try:
#                 time.sleep(1)
#
#                 row_id = itm[0]
#                 Partner_ID = itm[1]
#                 Partner_Name = itm[2]
#                 Country = itm[3]
#                 Scraping_Vendor_Name = itm[4]
#                 Product_URL = itm[5]
#                 Brand = itm[6]
#                 MPN = itm[7]
#                 Product_Line = itm[8]
#                 Category = itm[9]
#                 Subcategory = itm[10]
#                 Scrape_Frequency = itm[11]
#                 Additional_Header_2 = itm[12]
#                 Detailed_Partner_ID = itm[13]
#                 Feature_Keywords_Indoor_Air_Quality = itm[14]
#                 Lookup_Keyword = itm[15]
#                 Scrape_frequency = itm[16]
#                 screenshotpath = itm[17]
#                 Feature_Keywords_Security = itm[18]
#                 Feature_Keywords_Sustainability = itm[19]
#                 Scrape_Phase = itm[20]
#                 Feature_Keywords_Quality = itm[21]
#                 Product_specifications=itm[22]
#
#                 print(screenshotpath, "*****")
#                 sspathfrmtab=screenshotpath
#
#                 hash_utf8 = (str(Product_URL).encode('utf8'))
#                 prod_id = int(hashlib.md5(hash_utf8).hexdigest(), 16)
#
#                 if screenshotpath:
#                     # image_name = screenshotpath.split('/')[-1]
#                     # image_full_path=screenshotpath
#                     image_name = Additional_Header_2
#                     image_full_path = SCREENSHOT_FOLDER_PATH + "\\" + image_name
#
#                 else:
#                     image_name = ''
#                     partner_id = Partner_ID
#                     mpn = MPN
#                     current_time = datetime.now().strftime('%HH%MM')
#                     now_date = datetime.now().strftime('%m-%d-%Y')
#                     detailed_partner_id = Detailed_Partner_ID
#                     # detailed_partner_id = detailed_partner_id.replace("/", "")
#                     image_name = f'\\{partner_id}_na_{mpn}_{current_time}_{now_date}.jpg'
#                     image_path = SCREENSHOT_FOLDER_PATH
#                     image_full_path = image_path + image_name
#                     screenshotpath = image_full_path
#
#                 filename = f'/{prod_id}.html'
#                 pagepath = HTML_FOLDER_PATH + filename
#                 pagepath = pagepath.replace("\\", "/")
#
#                 infer_dict = {
#                     "htmlpath": pagepath,
#                     "Feature_Keywords_Quality": Feature_Keywords_Quality,
#                     "image_full_path": image_full_path,
#                     "Scrape_Phase": Scrape_Phase,
#                     "Feature_Keywords_Security": Feature_Keywords_Security,
#                     "Feature_Keywords_Sustainability": Feature_Keywords_Sustainability,
#                     "screenshotpath": image_full_path,
#                     # "screenshotpath":screenshotpath,
#                     "image_name": image_name,
#                     "prod_id": prod_id,
#                     "row_id": row_id,
#                     "Partner_ID": Partner_ID,
#                     "Partner_Name": Partner_Name,
#                     "Country": Country,
#                     "Scraping_Vendor_Name": Scraping_Vendor_Name,
#                     "Product_URL": Product_URL,
#                     "Brand": Brand,
#                     "MPN": MPN,
#                     "Product_Line": Product_Line,
#                     "Category": Category,
#                     "Subcategory": Subcategory,
#                     "Scrape_Frequency": Scrape_Frequency,
#                     "Additional_Header_2": Additional_Header_2,
#                     "Detailed_Partner_ID": Detailed_Partner_ID,
#                     "Feature_Keywords_Indoor_Air_Quality": Feature_Keywords_Indoor_Air_Quality,
#                     "Lookup_Keyword": Lookup_Keyword,
#                     "Scrape_frequency": Scrape_frequency,
#                     "Product_specifications":Product_specifications
#                 }
#
#                 if os.path.exists(pagepath) and sspathfrmtab is not None and sspathfrmtab != "None":
#                     yield scrapy.FormRequest(url=f'file:///{pagepath}', callback=self.parse, dont_filter=True,
#                                              meta={"infer_dict": infer_dict})
#                 else:
#
#                     ch = webdriver.ChromeOptions()
#                     ch.headless = True
#
#                     dd = webdriver.Chrome(ChromeDriverManager().install(), options=ch)
#                     dd.implicitly_wait(10)
#
#                     dd.get(Product_URL)
#                     dd.maximize_window()
#
#                     if "Logo coppel" in dd.page_source:
#                         prod_id = infer_dict.get('prod_id')
#
#                         if infer_dict.get("Additional_Header_2") == "n/a" or infer_dict.get(
#                                         "Additional_Header_2") == None or infer_dict.get(
#                                         "Additional_Header_2") == "":
#                             try:
#                                 # status_checkc = screenshotwithselenium(product_url, image_path, image_name[1:])
#
#                                 if 'We’re sorry. The Web address you entered is not a functioning page on our site' not in dd.page_source:
#                                         S = lambda X: dd.execute_script('return document.body.parentNode.scroll' + X)
#                                         dd.set_window_size(1250, S('Height'))
#                                 dd.find_element_by_tag_name('body').screenshot(screenshotpath)
#
#                                 if os.path.exists(image_path+image_name):
#                                     filename = f'/{prod_id}.html'
#                                     pagepath = HTML_FOLDER_PATH + filename
#                                     pagepath = pagepath.replace("\\", "/")
#                                     time.sleep(1)
#                                     with open(pagepath, 'w', encoding='utf-8') as f:
#                                         f.write(dd.page_source)
#                                     dd.quit()
#
#                                 else:
#                                     # init(convert=True)
#                                     # print(Fore.RED, Style.BRIGHT,"Screenshot issue found so Retun None-----")
#                                     # print(Fore.WHITE, "Going.....")
#                                     dd.quit()
#                                     return None
#
#                             except Exception as e:
#                                 print(e)
#
#                     yield scrapy.FormRequest(url=f'file:///{pagepath}', callback=self.parse,
#                                              meta={"infer_dict": infer_dict})
#
#                 screenshotpath11 = (image_path + image_name).replace("\\", '//')
#                 row_id = infer_dict.get("row_id")
#                 image_update = image_name.replace("\\", '')
#                 update_img = f"update {product_data_table} set screenshotpath='{screenshotpath11}',Additional_Header_2='{image_update}' where id='{row_id}'"
#                 self.cursor.execute(update_img)
#                 self.con.commit()
#
#
#             except Exception as e:
#                 print(e)
#
#     def parse(self, response, **kwargs):
#
#         try:
#             if "</html>" in str(response.body) and "/errors/validateCaptcha" not in response.text:
#                 # all object assing to blank intialize_variable() method in dll
#                 dllobj.intialize_variable()
#                 infer_dict = response.meta.get("infer_dict")
#
#                 print("#-------------------------------------------------------------------------------------------#")
#                 print("Product row id is : ", infer_dict.get("row_id"))
#
#                 dllobj.strHtml = str(response.body)
#
#                 """
#                         here save screenshot of product page and screenshot is exit or not, check here.....
#                         here also image name objects and image path with image name
#                 """
#
#                 prod_id = infer_dict.get('prod_id')
#
#                 filename = f'/{prod_id}.html'
#                 path = HTML_FOLDER_PATH + filename
#                 path = path.replace("\\", "/")
#
#                 if os.path.exists(path):
#                     pass
#                 else:
#                     with open(path, 'wb') as f:
#                         f.write(response.body)
#                 """
#                     here scrape all headers
#                 """
#                 respotex = response.text
#                 if "The Web address you entered is not a functioning page on our site" not in response.text:
#                     print(infer_dict)
#
#                     dllobj.status='Done'
#                     dllobj.id1 = c_replace(str(prod_id))
#                     image_name = infer_dict.get('image_name')
#                     dllobj.Additional_Header_2 = image_name.replace("\\", '')
#                     dllobj.Scrape_Completion = "n/a"
#                     dllobj.row_id = infer_dict.get("row_id")
#                     dllobj.htmlpath = path
#                     dllobj.Partner_ID = infer_dict.get("Partner_ID")
#                     dllobj.Partner_Name = infer_dict.get("Partner_Name")
#                     dllobj.Country = infer_dict.get("Country")
#                     dllobj.Scraping_Vendor_Name = infer_dict.get("Scraping_Vendor_Name")
#                     dllobj.Product_URL = infer_dict.get("Product_URL")
#                     dllobj.Brand = infer_dict.get("Brand")
#                     dllobj.MPN_backslash_Model_Input = c_replace(str(infer_dict.get("MPN")))
#                     dllobj.Product_Line = infer_dict.get("Product_Line")
#                     dllobj.Category = infer_dict.get("Category")
#                     dllobj.Subcategory = infer_dict.get("Subcategory")
#                     dllobj.Scrape_Frequency = infer_dict.get("Scrape_Frequency")
#                     dllobj.Scrape_Phase = infer_dict.get("Scrape_Phase")
#                     dllobj.Scrape_Date = datetime.today().strftime("%m/%d/%Y")
#                     dllobj.Product_specifications=infer_dict.get("Product_specifications")
#                     # dllobj.Manufacturer_content = "No"
#                     # dllobj.Availability_space_of_space_why_space__singlequote__hash_Brand_singlequote__space_message = "No"
#                     detailed_partner_id = infer_dict.get("Detailed_Partner_ID")
#                     dllobj.Detailed_Partner_ID = detailed_partner_id
#                     dllobj.Availability_intrusive_Pop_dash_up_banners = "No"
#                     dllobj.Additional_Header_3 = "N"
#                     finalsspath = infer_dict.get("image_full_path").replace('\\', '/')
#                     dllobj.screenshotpath = finalsspath
#                     # dllobj.screenshotpath=infer_dict.get("image_full_path")
#                     # dllobj.Availability_preferred_product__doublequote_badge_doublequote_ = "No"
#                     # dllobj.Availability_Video = "No"
#                     dllobj.FAQs_and_avoid_using_click_dash_to_dash_expand_content_blocks = "No"
#                     dllobj.Availability_space_of_space_SEO_space_friendly_space_URL = "No"
#                     dllobj.Keyword_backslash_s_space_included_space_in_space_product_space_name = "No"
#                     dllobj.Availability_e_dash_Tail_headliner = "No"
#                     dllobj.Content_space_visibility_space__openingparentheses_No_space_blocks_closingparentheses_ = "No"
#                     dllobj.Feature_space_Keywords_Indoor_space_Air_space_Quality = infer_dict.get("Feature_Keywords_Indoor_Air_Quality")
#                     dllobj.Lookup_Keyword = infer_dict.get("Lookup_Keyword")
#                     dllobj.Scrape_frequency = infer_dict.get("Scrape_frequency")
#                     dllobj.Feature_space_Keywords_Quality = infer_dict.get('Feature_Keywords_Quality')
#                     dllobj.Feature_space_Keywords_Security = infer_dict.get("Feature_Keywords_Security")
#                     dllobj.Feature_space_Keywords_Sustainability = infer_dict.get("Feature_Keywords_Sustainability")
#
#
#                     lookup_keyword_ = infer_dict.get("Lookup_Keyword").replace(" ", "-")
#                     if lookup_keyword_.lower() in dllobj.Product_URL.lower():
#                         dllobj.Availability_space_of_space_SEO_space_friendly_space_URL = "Yes"
#                     else:
#                         dllobj.Availability_space_of_space_SEO_space_friendly_space_URL = "No"
#
#                     dllobj.htmlpath = infer_dict.get('htmlpath')
#
#                     # id1 = "";
#
#                     dllobj.Scrape_Date = time.strftime('%m/%d/%Y')
#                     dllobj.Broken_URL = "n/a"
#
#                     # ====================== Product_ID ======================#
#                     try:
#                         # item['Product_ID'] = ''.join(re.findall('/dp/(.*?)/', response.meta['input_data']['Product_URL']))
#                         Product_ID = infer_dict.get('Product_URL').split('-')[-1]
#                         dllobj.Product_ID = c_replace(Product_ID)
#                         # print(dllobj.update_table())
#                     except Exception as e:
#                         Product_ID = ''.join(re.findall('var asin = "(.*?)";', response.text))
#                         dllobj.Product_ID = c_replace(Product_ID)
#                         print(e, "Error in product id Consider 2nd xpath")
#                         if not dllobj.Product_ID:
#                             Product_ID = response.xpath('//span[@class="sku"]//text()').get().split(":")[-1]
#                             dllobj.Product_ID = c_replace(Product_ID)
#
#                     dllobj.Product_URL = infer_dict.get('Product_URL')
#                     try:
#                         prod_id = re.findall('/dp/(.*?)/', dllobj.Product_URL)[0]
#                     except:
#                         prod_id = dllobj.Product_URL.split('-')[-1]
#
#                     # ====================== Product_Name ======================#
#                     try:
#                         Product_Name = response.xpath('//h1[@class="main_header"]//text()').get()
#                     except Exception as e:
#                         print("prodct name Error Please check", e)
#                         Product_Name = 'n/a'
#
#                     dllobj.Product_Name = c_replace(Product_Name)
#
#                     if dllobj.Product_Name in Product_Name:
#                         dllobj.Availability_Product_Name = "Yes"
#                     else:
#                         dllobj.Availability_Product_Name = "No"
#                     # if dllobj.Product_Name == "n/a" or dllobj.Product_Name == "":
#                     #     Product_Name2 = response.xpath('//h1//span//text()').get()
#                     #     dllobj.Product_Name = c_replace(Product_Name2)
#
#                     print('dllobj.Product_Name ==', dllobj.Product_Name)
#
#                     # ====================== Availability_Product_Name ======================#
#
#
#                     if dllobj.Lookup_Keyword.replace(" ", "-") in Product_Name:
#                         dllobj.Keyword_backslash_s_space_included_space_in_space_product_space_name = "Yes"
#                     else:
#                         dllobj.Keyword_backslash_s_space_included_space_in_space_product_space_name = "No"
#
#                     # ====================== Product_specifications ======================#
#                     try:
#                         key=[]
#                         value=[]
#                         for i in range(1,10):
#                             keys = response.xpath(f'//span[@id="descAttributeName_{i}_7_-3018_2471"]//text()').get()
#                             values = response.xpath(f'//span[@id="descAttributeValue_{i}_7_-3018_2471"]//text()').get()
#                             key.append(keys)
#                             value.append(values)
#                         # print("Key",key)
#                         # print("Value",value)
#                         descp=' #||# '.join([str(x) + str(y) for x, y in zip(key, value)])
#                         # print("Produ Desc",descp)
#                         # print(descp)
#                         dllobj.Product_specifications = c_replace(descp)
#
#                     except Exception as e:
#                         print(e)
#
#                     if dllobj.Product_specifications == descp:
#                         dllobj.Availability_specifications = "YES"
#                     else:
#                         dllobj.Availability_specifications = "No"
#
#
#
#                     # ====================== Product_Image_URL ======================#
#                     # print("ImgUrl",img)
#                     # prd_img=""
#                     img_list=[]
#                     for i in range(1,7):
#                         img=response.xpath(f'//img[@id="WC_CachedProductOnlyDisplay_prod_images_1_{i}"]/@src').getall()
#                         # print(img)
#                         img_j="".join(img)
#                         # print(img_j)
#                         img_list.append(img_j)
#                     img_list=" #||# ".join(img_list)
#                     # print(img_list)
#                     dllobj.Image_URLs=c_replace(img_list)
#                     # print(prd_img)
#                     # alt_img='#||#'.join(str(x) for x in prd_img)
#                     # print(prd_img)
#
#
#
#
#                 # ====================== UPDATE ======================#
#                 db = pymysql.connect(host=db_host, user=db_user, password=db_passwd, database=db_name)
#                 cursor = db.cursor()
#                 update_table_query = dllobj.update_table().encode('utf-8', 'replace').decode()
#                 print(update_table_query)
#                 cursor.execute(update_table_query)
#                 db.commit()
#
#         except Exception as e:
#             print(e)
#
#
# from scrapy.cmdline import execute
# execute('scrapy crawl ugam_prj'.split())
#
#
#
#
