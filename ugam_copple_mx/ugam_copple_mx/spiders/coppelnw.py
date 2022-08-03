import datetime
from ugam_copple_mx.pipelines import *
from ugam_copple_mx.config import *
import scrapy
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
from lxml import html
import os
import time
import hashlib
from mymodules._common_ import *
import pandas as pd
import csv
import re
from scrapy import Selector
import requests
import selectors


class ugam_copple(scrapy.Spider):

    name = "ugam_prj"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-platform': '"Windows"'
    }

    headers1 = {
        'sec-ch-ua': '" Not A;Brand";v = "99", "Chromium";v = "102", "Google Chrome";v = "102"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }

    def __init__(self, start='', end=''):

        try:
            self.start = start
            self.end = end
        except Exception as e:
            logger.error('spider in _init_ method error :{}'.format(e))
            print('__init__ error:', e)

    def start_requests(self):

        self.cursor = UgamCoppleMxPipeline.cursor
        self.con = UgamCoppleMxPipeline.con

        sql_query = f"select Id,Partner_ID,Partner_Name,Country,Scraping_Vendor_Name,Product_URL,Brand,`MPN/Model_Input`,Product_Line,Category,Subcategory,Scrape_Frequency,Additional_Header_2,Detailed_Partner_ID,`Feature Keywords_Indoor Air Quality`,Lookup_Keyword,Scrape_frequency,screenshotpath,`Feature Keywords_Security`,`Feature Keywords_Sustainability`,`Scrape_Phase`,`Feature Keywords_Quality` from {product_data_table} where Status = 'Pending' AND ID BETWEEN {self.start} AND {self.end}"
        print(sql_query)
        self.cursor.execute(sql_query)

        core_list = [clm for clm in self.cursor.fetchall()]

        for itm in core_list:
            try:
                time.sleep(1)

                row_id = itm[0]
                Partner_ID = itm[1]
                Partner_Name = itm[2]
                Country = itm[3]
                Scraping_Vendor_Name = itm[4]
                Product_URL = itm[5]
                Brand = itm[6]
                MPN = itm[7]
                Product_Line = itm[8]
                Category = itm[9]
                Subcategory = itm[10]
                Scrape_Frequency = itm[11]
                Additional_Header_2 = itm[12]
                Detailed_Partner_ID = itm[13]
                Feature_Keywords_Indoor_Air_Quality = itm[14]
                Lookup_Keyword = itm[15]
                Scrape_frequency = itm[16]
                screenshotpath = itm[17]
                Feature_Keywords_Security = itm[18]
                Feature_Keywords_Sustainability = itm[19]
                Scrape_Phase = itm[20]
                Feature_Keywords_Quality = itm[21]

                print(screenshotpath, "*****")
                sspathfrmtab = screenshotpath

                hash_utf8 = (str(Product_URL).encode('utf8'))
                prod_id = int(hashlib.md5(hash_utf8).hexdigest(), 16)

                if screenshotpath:
                    # image_name = screenshotpath.split('/')[-1]
                    # image_full_path=screenshotpath
                    image_name = Additional_Header_2
                    image_full_path = SCREENSHOT_FOLDER_PATH + "\\" + image_name

                else:

                    image_name = ''
                    partner_id = Partner_ID
                    mpn = MPN
                    current_time = datetime.now().strftime('%HH%MM')
                    now_date = datetime.now().strftime('%m-%d-%Y')
                    detailed_partner_id = Detailed_Partner_ID
                    # detailed_partner_id = detailed_partner_id.replace("/", "")
                    image_name = f'\\{partner_id}_na_{mpn}_{current_time}_{now_date}.jpg'
                    image_path = SCREENSHOT_FOLDER_PATH
                    image_full_path = image_path + image_name
                    screenshotpath = image_full_path

                filename = f'/{prod_id}.html'
                pagepath = HTML_FOLDER_PATH + filename
                pagepath = pagepath.replace("\\", "/")

                infer_dict = {
                    "xtraurl": Product_URL,
                    "htmlpath": pagepath,
                    "Feature_Keywords_Quality": Feature_Keywords_Quality,
                    "image_full_path": image_full_path,
                    "Scrape_Phase": Scrape_Phase,
                    "Feature_Keywords_Security": Feature_Keywords_Security,
                    "Feature_Keywords_Sustainability": Feature_Keywords_Sustainability,
                    "screenshotpath": image_full_path,
                    # "screenshotpath":screenshotpath,
                    "image_name": image_name,
                    "prod_id": prod_id,
                    "row_id": row_id,
                    "Partner_ID": Partner_ID,
                    "Partner_Name": Partner_Name,
                    "Country": Country,
                    "Scraping_Vendor_Name": Scraping_Vendor_Name,
                    "Product_URL": Product_URL,
                    "Brand": Brand,
                    "MPN": MPN,
                    "Product_Line": Product_Line,
                    "Category": Category,
                    "Subcategory": Subcategory,
                    "Scrape_Frequency": Scrape_Frequency,
                    "Additional_Header_2": Additional_Header_2,
                    "Detailed_Partner_ID": Detailed_Partner_ID,
                    "Feature_Keywords_Indoor_Air_Quality": Feature_Keywords_Indoor_Air_Quality,
                    "Lookup_Keyword": Lookup_Keyword,
                    "Scrape_frequency": Scrape_frequency,
                }

                if os.path.exists(pagepath) and sspathfrmtab is not None and sspathfrmtab != "None":
                    yield scrapy.FormRequest(url=f'file:///{pagepath}', callback=self.parse, dont_filter=True,
                                             meta={"infer_dict": infer_dict}, headers=self.headers1)

                else:

                    options = webdriver.ChromeOptions()
                    options.headless = True
                    options.add_argument(
                        "User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36")
                    dd = webdriver.Chrome(ChromeDriverManager().install(), options=options)
                    dd.get(Product_URL)
                    time.sleep(10)
                    dd.maximize_window()
                    dd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(2)
                    dd.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
                    time.sleep(2)

                    if "Logo coppel" in dd.page_source:
                        prod_id = infer_dict.get('prod_id')

                        if infer_dict.get("Additional_Header_2") == "n/a" or infer_dict.get(
                                "Additional_Header_2") == None or infer_dict.get(
                            "Additional_Header_2") == "":
                            try:
                                # status_checkc = screenshotwithselenium(product_url, image_path, image_name[1:])

                                if "Logo coppel" in dd.page_source:

                                    for i in range(1, 12000, 200):
                                        time.sleep(2)
                                        dd.execute_script("window.scrollTo(0, {});".format(i))

                                    # dd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                                    # dd.execute_script("window.scrollTo(document.body.scrollHeight, 0);")
                                    time.sleep(5)
                                    S = lambda X: dd.execute_script('return document.body.parentNode.scroll' + X)
                                    dd.set_window_size(1400, S('Height'))
                                    # dd.save_screenshot(screenshotpath)
                                    dd.find_element_by_tag_name('body').screenshot(screenshotpath)

                                if os.path.exists(image_path + image_name):
                                    filename = f'/{prod_id}.html'
                                    pagepath = HTML_FOLDER_PATH + filename
                                    pagepath = pagepath.replace("\\", "/")
                                    # time.sleep(8)
                                    with open(pagepath, 'w', encoding='utf-8') as f:
                                        f.write(dd.page_source)
                                    dd.quit()

                                else:
                                    # init(convert=True)
                                    # print(Fore.RED, Style.BRIGHT,"Screenshot issue found so Retun None-----")
                                    # print(Fore.WHITE, "Going.....")
                                    dd.quit()
                                    return None

                            except Exception as e:
                                print(e)

                    yield scrapy.FormRequest(url=f'file:///{pagepath}', callback=self.parse,
                                             meta={"infer_dict": infer_dict})

                screenshotpath11 = (image_path + image_name).replace("\\", '//')
                row_id = infer_dict.get("row_id")
                image_update = image_name.replace("\\", '')
                update_img = f"update {product_data_table} set screenshotpath='{screenshotpath11}',Additional_Header_2='{image_update}' where id='{row_id}'"
                self.cursor.execute(update_img)
                self.con.commit()

            except Exception as e:
                print(e)

    def parse(self, response, **kwargs):
        print("Status", response.status)
        product_url = response.meta.get('infer_dict')
        prod_id_f = product_url.get("xtraurl")
        prod_id_nw = prod_id_f.split('-')[-1]

        try:
            if "</html>" in str(response.body) and "/errors/validateCaptcha" not in response.text:
                # all object assing to blank intialize_variable() method in dll
                dllobj.intialize_variable()
                infer_dict = response.meta.get("infer_dict")

                print("#-------------------------------------------------------------------------------------------#")
                print("Product row id is : ", infer_dict.get("row_id"))
                print("URL", response.url)

                dllobj.strHtml = str(response.body)

                """
                        here save screenshot of product page and screenshot is exit or not, check here.....
                        here also image name objects and image path with image name
                """

                prod_id = infer_dict.get('prod_id')

                filename = f'/{prod_id}.html'
                path = HTML_FOLDER_PATH + filename
                path = path.replace("\\", "/")

                if os.path.exists(path):
                    pass
                else:
                    with open(path, 'wb') as f:
                        f.write(response.body)
                """
                    here scrape all headers
                """

                respotex = response.text
                if "Página no encontrada" not in response.text:
                    print(infer_dict)

                    dllobj.status = 'Done'
                    dllobj.id1 = str(infer_dict.get("row_id"))
                    image_name = infer_dict.get('image_name')
                    dllobj.Additional_Header_2 = image_name.replace("\\", '')
                    dllobj.Scrape_Completion = "n/a"
                    dllobj.row_id = infer_dict.get("row_id")
                    dllobj.htmlpath = path
                    dllobj.Partner_ID = infer_dict.get("Partner_ID")
                    dllobj.Partner_Name = infer_dict.get("Partner_Name")
                    dllobj.Country = infer_dict.get("Country")
                    dllobj.Scraping_Vendor_Name = infer_dict.get("Scraping_Vendor_Name")
                    dllobj.Product_URL = infer_dict.get("Product_URL")
                    dllobj.Brand = infer_dict.get("Brand")
                    dllobj.MPN_backslash_Model_Input = c_replace(str(infer_dict.get("MPN")))
                    dllobj.Product_Line = infer_dict.get("Product_Line")
                    dllobj.Category = infer_dict.get("Category")
                    dllobj.Subcategory = infer_dict.get("Subcategory")
                    dllobj.Scrape_Frequency = infer_dict.get("Scrape_Frequency")
                    dllobj.Scrape_Phase = infer_dict.get("Scrape_Phase")
                    dllobj.Scrape_Date = datetime.today().strftime("%m/%d/%Y")
                    # dllobj.Manufacturer_content = "No"
                    # dllobj.Availability_space_of_space_why_space__singlequote__hash_Brand_singlequote__space_message = "No"
                    detailed_partner_id = infer_dict.get("Detailed_Partner_ID")
                    dllobj.Detailed_Partner_ID = detailed_partner_id
                    dllobj.Availability_intrusive_Pop_dash_up_banners = "No"
                    # dllobj.Additional_Header_3 = "N"
                    finalsspath = infer_dict.get("image_full_path").replace('\\', '/')
                    dllobj.screenshotpath = finalsspath
                    # dllobj.screenshotpath=infer_dict.get("image_full_path")
                    # dllobj.Availability_preferred_product__doublequote_badge_doublequote_ = "No"
                    # dllobj.Availability_Video = "No"
                    dllobj.FAQs_and_avoid_using_click_dash_to_dash_expand_content_blocks = "No"
                    dllobj.Availability_space_of_space_SEO_space_friendly_space_URL = "No"
                    dllobj.Keyword_backslash_s_space_included_space_in_space_product_space_name = "No"
                    dllobj.Availability_e_dash_Tail_headliner = "No"
                    dllobj.Content_space_visibility_space__openingparentheses_No_space_blocks_closingparentheses_ = "No"
                    dllobj.Feature_space_Keywords_Indoor_space_Air_space_Quality = infer_dict.get(
                        "Feature_Keywords_Indoor_Air_Quality")
                    dllobj.Lookup_Keyword = infer_dict.get("Lookup_Keyword")
                    dllobj.Scrape_frequency = infer_dict.get("Scrape_frequency")
                    dllobj.Feature_space_Keywords_Quality = infer_dict.get('Feature_Keywords_Quality')
                    dllobj.Feature_space_Keywords_Security = infer_dict.get("Feature_Keywords_Security")
                    dllobj.Feature_space_Keywords_Sustainability = infer_dict.get("Feature_Keywords_Sustainability")
                    dllobj.Header_Tag__openingparentheses_H1_Tag_closingparentheses_ = 'n/a'
                    dllobj.Canonical_URL = "n/a"

                    try:
                        lookup_keyword_ = infer_dict.get("Lookup_Keyword").replace(" ", "-")
                        if lookup_keyword_.lower() in dllobj.Product_URL.lower():
                            dllobj.Availability_space_of_space_SEO_space_friendly_space_URL = "Yes"
                        else:
                            dllobj.Availability_space_of_space_SEO_space_friendly_space_URL = "No"
                    except Exception as e:
                        print(e)

                    dllobj.htmlpath = infer_dict.get('htmlpath')

                    # id1 = "";

                    dllobj.Scrape_Date = time.strftime('%m/%d/%Y')
                    dllobj.Broken_URL = "n/a"

                    # ====================== Status ======================#

                    if "Página no encontrada" in response.text:
                        dllobj.status = "Not Found"
                    else:
                        dllobj.status = "Done"

                    # ====================== Product_ID ======================#

                    try:
                        # item['Product_ID'] = ''.join(re.findall('/dp/(.*?)/', response.meta['input_data']['Product_URL']))
                        Product_ID = \
                            response.xpath('//span[@class="sku hidden"]//text()').extract_first(default="").split(':')[
                                -1]
                        print("PDID", Product_ID)
                        if Product_ID:
                            dllobj.Product_ID = c_replace(Product_ID)
                        else:
                            dllobj.Product_ID = "n/a"
                    except Exception as e:
                        print(e)
                        dllobj.Product_ID = "n/a"

                    # ====================== Product_Name ====================== #

                    try:
                        Product_Name = response.xpath('//h1[@class="main_header"]//text()').extract_first(
                            default='').strip()
                        if Product_Name:
                            dllobj.Product_Name = c_replace(Product_Name)
                            dllobj.Availability_Product_Name = "Yes"
                        else:
                            dllobj.Product_Name = "n/a"
                            dllobj.Availability_Product_Name = "No"
                    except Exception as e:
                        print(e)

                    # if dllobj.Product_Name == "n/a" or dllobj.Product_Name == "":
                    #     Product_Name2 = response.xpath('//h1//span//text()').get()
                    #     dllobj.Product_Name = c_replace(Product_Name2)

                    print('dllobj.Product_Name ==', dllobj.Product_Name)

                    # ====================== Availability_Product_Name ======================#

                    try:
                        if dllobj.Lookup_Keyword.replace(" ", "-") in Product_Name:
                            dllobj.Keyword_backslash_s_space_included_space_in_space_product_space_name = "Yes"
                        else:
                            dllobj.Keyword_backslash_s_space_included_space_in_space_product_space_name = "No"
                    except Exception as e:
                        print(e)

                    # ====================== Product_specifications ======================#

                    try:
                        keys = response.xpath('//div[@data-slot-id="7"]//div//ul//li//span[1]//text()').getall()
                        values = response.xpath('//div[@data-slot-id="7"]//div//ul//li//span[2]//text()').getall()
                        specification = '#||#'.join(
                            [str(key).strip() + " " + str(value).strip() for key, value in zip(keys, values)])
                        print("sp:", specification)

                        if specification:
                            dllobj.Availability_specifications = "Yes"
                            dllobj.Product_specifications = c_replace(specification)
                        else:
                            dllobj.Availability_specifications = "No"
                            dllobj.Product_specifications = "n/a"

                    except Exception as e:
                        print(e)

                    # try:
                    #     key = []
                    #     value = []
                    #     for i in range(1, 22):
                    #         keys = response.xpath('//div[@data-slot-id="7"]//div//ul//li//span[1]//text()').extract_first(default='').strip()
                    #         values = response.xpath(f'//span[@id="descAttributeValue_{i}_7_-3018_2471"]//text()').extract_first(default='').strip()
                    #         key.append(keys)
                    #         value.append(values)
                    #     # print("Key",key)
                    #     # print("Value",value)
                    #     descp = '#||#'.join([str(x) +" "+ str(y) for x, y in zip(key, value)])
                    #     # print("Produ Desc",descp)
                    #     # print(descp)
                    #     dllobj.Product_specifications = c_replace(descp)
                    #     # nw_sp=''.join(response.xpath('//div[@data-slot-id="7"]//div//ul//li//span//text()').getall()).strip()
                    #     # print("New_SP",nw_sp)
                    #
                    # except Exception as e:
                    #     print(e)
                    #
                    # if dllobj.Product_Name == "n/a":
                    #     dllobj.Availability_specifications = "No"
                    #     dllobj.Product_specifications="n/a"
                    # else:
                    #     dllobj.Availability_specifications = "Yes"
                    #     dllobj.Product_specifications=c_replace(descp)

                    # ====================== Product_Image_URL ======================#

                    try:
                        img = response.xpath('//div[@id="ProductAngleProdImagesArea"]//ul//li//a/@href').getall()
                        # print(img)
                        img_list = "#||#".join(img)
                        # print("img_l",img_list)

                        if dllobj.Product_Name == 'n/a':
                            dllobj.Image_URLs = 'n/a'
                            dllobj.Availability_Image = "No"
                        else:
                            dllobj.Image_URLs = c_replace(img_list)
                            dllobj.Availability_Image = "Yes"
                    except Exception as e:
                        print(e)

                    # ====================== Product_Description ======================#

                    try:

                        page_id = response.xpath('//meta[@name="pageId"]/@content').extract_first(default="").strip()
                        pds = ''.join(
                            response.xpath(f'//div[@id="product_longdescription_{page_id}"]//text()').getall()).strip()
                        # pds_j="".join(pds)
                        if dllobj.Product_Name == "n/a":
                            dllobj.Product_description = "n/a"
                            dllobj.Availability_product_description = "No"
                        else:
                            dllobj.Product_description = c_replace(pds)
                            dllobj.Availability_product_description = "Yes"

                    except Exception as e:
                        print(e)

                    # print("Desc",dllobj.Product_description)

                    # ====================== Meta Title ====================== #
                    try:

                        meta = response.xpath('//title//text()').extract_first(default="")

                        if meta:
                            if "Página no encontrada" not in response.text:
                                dllobj.Meta_title = c_replace(meta)
                                dllobj.Availability_meta_title = "Yes"
                            else:
                                dllobj.Meta_title = "n/a"
                                dllobj.Availability_meta_title = "No"

                    except Exception as e:
                        print(e)

                    # ====================== Breadcumbs ======================#

                    try:

                        bcm = response.xpath('//a[@id="WC_BreadCrumb_Link_1_1_-3028_2465"]//text()').extract_first(
                            default="")
                        if bcm:
                            dllobj.Breadcrumbs = c_replace(bcm)
                            dllobj.Availability_Breadcrumbs = "Yes"
                        else:
                            dllobj.Breadcrumbs = "n/a"
                            dllobj.Availability_Breadcrumbs = "No"
                    except Exception as e:
                        print(e)

                    # ====================== Image_Alt_Text ======================#

                    try:
                        dllobj.Image_Alt_Text = "n/a"
                        dllobj.Availability_alt_text_in_images = "No"

                    except Exception as e:
                        print(e)

                    # ====================== MPN_output ======================#

                    try:
                        mpn_ot = response.xpath(
                            '//*[contains(text(),"Modelo #:")]//following-sibling::span//text()').get()
                        # print("MPN", mpn_ot)
                        mpn_j = c_replace(mpn_ot).split(',')[0]
                        if len(mpn_j) > 7:
                            mpn_j = c_replace(mpn_ot).split(',')[1]
                        # print("MPN",mpn_j)

                        if mpn_ot:
                            dllobj.MPN_Output = c_replace(mpn_j)
                        else:
                            dllobj.MPN_Output = "n/a"
                    except Exception as e:
                        print(e)
                        dllobj.MPN_Output = "n/a"

                    # ====================== Header_Tag_(H1_Tag) ======================#

                    try:
                        header_tag = ''.join(
                            response.xpath('//h1[@class="main_header"]//text()').extract_first(default="")).strip()
                        if header_tag:
                            dllobj.Header_Tag__openingparentheses_H1_Tag_closingparentheses_ = c_replace(header_tag)
                        else:
                            dllobj.Header_Tag__openingparentheses_H1_Tag_closingparentheses_ = "n/a"
                        # print(dllobj.Header_Tag__openingparentheses_H1_Tag_closingparentheses_)

                    except Exception as e:
                        print(e)

                    # ====================== Canonical URL ======================#

                    try:
                        c_name = response.xpath('//link[@rel="canonical"]//@href').extract_first(default="")
                        if c_name:
                            dllobj.Canonical_URL = c_replace(c_name)
                        else:
                            dllobj.Canonical_URL = "n/a"
                    except Exception as e:
                        print(e)

                    # ====================== Meta Description ======================#

                    try:
                        meta_des = response.xpath('//meta[@name="description"]/@content').extract_first(default="")
                        if meta_des:
                            dllobj.Meta_description = c_replace(meta_des)
                            dllobj.Availability_meta_description = "Yes"
                        else:
                            dllobj.Meta_description = "n/a"
                            dllobj.Availability_meta_description = "No"

                    except Exception as e:
                        print(e)

                    # ====================== Feature_Bullets ======================#

                    try:
                        dllobj.Feature_Bullets = "n/a"
                        dllobj.Availability_Feature_Bullets = "No"
                    except Exception as e:
                        print(e)

                    # ====================== ASIN/UPC ======================#

                    try:
                        dllobj.ASIN_backslash_UPC = 'n/a'
                    except Exception as e:
                        print(e)

                    # ====================== EAN ======================#

                    try:
                        dllobj.EAN = 'n/a'
                    except Exception as e:
                        print(e)

                    # ====================== Stock_Message ======================#

                    stm = ''.join(response.xpath('//p[@id="availabilityShopAction"]//text()').getall())

                    try:
                        if stm:
                            dllobj.Stock_Message = c_replace(stm)
                        else:
                            dllobj.Stock_Message = "n/a"

                    except Exception as e:
                        print(e)
                        dllobj.Stock_Message = "n/a"

                    # ====================== Add_to_Cart ======================#

                    try:
                        if dllobj.Stock_Message == "Producto no disponible":
                            dllobj.Add_to_Cart = "No"
                        elif dllobj.Stock_Message == "n/a":
                            dllobj.Add_to_Cart = "No"
                        else:
                            dllobj.Add_to_Cart = "Yes"
                    except Exception as e:
                        print(e)
                        dllobj.Add_to_Cart = "Yes"

                    # ====================== Stock_Status ======================#

                    try:
                        if dllobj.Add_to_Cart == "No":
                            dllobj.Stock_Status = "Out of Stock"
                        elif dllobj.Add_to_Cart == "No" and dllobj.Stock_Message == "n/a":
                            dllobj.Stock_Status = "Unable to Determine"
                        else:
                            dllobj.Stock_Status = "In Stock"
                    except Exception as e:
                        print(e)

                    # ====================== Stock_Volume ======================#

                    try:
                        dllobj.Stock_Volume = "n/a"
                    except Exception as e:
                        print(e)

                    # ====================== SELLER_Name ======================#

                    try:
                        sln = ''.join(response.xpath('//span[@class="text"]//text()').getall()[-2:])
                        # sp = sln.split(" ")[-1]

                        if sln:
                            if "Coppel" in sln:
                                sp = sln.split(" ")[-1]
                                dllobj.Seller_Name = c_replace(sp)
                            else:
                                dllobj.Seller_Name = c_replace(sln)
                        else:
                            dllobj.Seller_Name = 'n/a'

                    except Exception as e:
                        print(e)

                    # ====================== Seller_Type ======================#

                    try:
                        dllobj.Seller_Type = "n/a"
                    except Exception as e:
                        print(e)

                    # ====================== Delivery_Option ======================#

                    dp = response.xpath(
                        '//*[@class="avaible_text"]//div[@id="productPageAdd2Cart"]//text()').extract_first(
                        default="").strip()
                    try:
                        if dllobj.Add_to_Cart == "Yes":
                            dllobj.Delivery_Option = c_replace(dp)
                        else:
                            dllobj.Delivery_Option = "n/a"
                    except Exception as e:
                        print(e)
                        dllobj.Delivery_Option = "n/a"

                    # ======================Thrird_party_Flag ======================#

                    try:
                        if dllobj.Seller_Name == 'Coppel' or 'n/a' in dllobj.Seller_Name:
                            dllobj.Third_Party_Flag = "False"
                        else:
                            dllobj.Third_Party_Flag = "True"

                    except Exception as e:
                        print(e)

                    # ====================== Image_ALT_TEXT ======================#

                    iat = response.xpath('//img[@id="WC_CachedProductOnlyDisplay_prod_images_1_1"]/@alt').get()
                    try:
                        if iat:
                            dllobj.Image_Alt_Text = c_replace(iat)
                            dllobj.Availability_alt_text_in_images = "Yes"
                        else:
                            dllobj.Image_Alt_Text = "n/a"
                            dllobj.Availability_alt_text_in_images = "No"

                    except Exception as e:
                        print(e)

                    # ====================== Availability_Video ======================#

                    try:
                        dllobj.Availability_Video = "No"
                    except Exception as e:
                        print(e)

                    # ====================== No_of_Customer_review AND Availability_customer_review ======================#

                    try:
                        dllobj.No_of_customer_reviews = "n/a"
                        dllobj.Availability_customer_reviews = "No"
                    except Exception as e:
                        print(e)

                    # ====================== Product_Rating ======================#

                    try:
                        dllobj.Product_Rating = "n/a"
                        dllobj.Availability_product_rating = "No"
                    except Exception as e:
                        print(e)

                    # ====================== No_of_customer-reveiew ======================#

                    try:
                        dllobj._No_of_customer_reviews_openingparentheses_21_closingparentheses__ = 'n/a'
                    except Exception as e:
                        print(e)
                        dllobj._No_of_customer_reviews_openingparentheses_21_closingparentheses__ = 'n/a'

                    # # ====================== CROSS-SELL PRODUCT ======================#

                    #
                    # try:
                    #     htp_lk = []
                    #     csp = response.xpath('//h2[contains(text(),"Complementa tu compra")]//..//following-sibling::div//*[@id="owlStage2"]//div//a/@href').getall()
                    #     csp_name = response.xpath('//h2[contains(text(),"Complementa tu compra")]//..//following-sibling::div//*[@id="owlStage2"]//div//a//div[@class="seccion-caracteristicas"]/p[@class="data-nombre"]//text()').getall()
                    #     j_csp_name = '#||#'.join(csp_name)
                    #     # print(j_csp_name)
                    #     for i in csp:
                    #         htp_lk.append("https://www.coppel.com" + i)
                    #     htp_csp = '#||#'.join(htp_lk)
                    #     # print("htp_csp",htp_csp)
                    #     if htp_csp:
                    #         dllobj.Cross_dash_sell_Product_Name = c_replace(j_csp_name)
                    #         dllobj.Cross_dash_sell_URL = c_replace(htp_csp)
                    #         dllobj.Availability_Cross_dash_sell = 'Yes'
                    #     else:
                    #         dllobj.Cross_dash_sell_Product_Name = "n/a"
                    #         dllobj.Cross_dash_sell_URL = "n/a"
                    #         dllobj.Availability_Cross_dash_sell = 'No'


                    # except Exception as e:
                    #     print(e)
                    #     dllobj.Cross_dash_sell_Product_Name = "n/a"
                    #     dllobj.Cross_dash_sell_URL = "n/a"
                    #     dllobj.Availability_Cross_dash_sell = 'No'

                    # ====================== Cross-Sell Location ======================#

                    try:
                        if dllobj.Cross_dash_sell_Product_Name == 'n/a':
                            dllobj.Cross_dash_sell_Location = "n/a"
                        else:
                            dllobj.Cross_dash_sell_Location = "PDP"
                    except Exception as e:
                        print(e)
                        dllobj.Cross_dash_sell_Location = "PDP"
                    #

                    up_header = {
                        'authority': 'pdpr.coppelomnicanal.com',
                        'method': 'GET',
                        'cheme': 'https',
                        'accept': '*/*',
                        'content-type': 'application/json',
                        'origin': 'https://www.coppel.com',
                        'sec-ch-ua-platform': '"Windows"',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
                    }
                    headers123 = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
                        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
                        'sec-ch-ua-platform': '"Windows"'
                    }

                    # print(prod_id_nw)
                    # # ====================== UP-SELL PRODUCT ======================#
                    # if Product_ID != '' or Product_ID != 'n/a':
                    #     upsell_products = f'https://pdpr.coppelomnicanal.com/v0/get/recommendation/2831663/IZTAPALAPA/DISTRITO%20FEDERAL?key=AIzaSyCc-ujJjD_f3s0M282wMwrpZ9zxQdyVfC4'
                    #
                    #     filename_up = f'/Product_2831663_upsell.html'
                    #     path_up = HTML_FOLDER_PATH + filename_up
                    #     path_up = path_up.replace("\\", "/")
                    #     try:
                    #         if os.path.exists(path_up):
                    #             # page save exists, so reading the saved page and loading the json file.
                    #             pass
                    #
                    #         else:
                    #             print(upsell_products)
                    #             response_upsell = requests.get(url=upsell_products, headers=headers123)
                    #
                    #             with open(path_up, 'w')as f:
                    #                 f.write(response_upsell.text)

                    #     except:
                    #         print("..................................")
                    # else:
                    #     print("Not related Product_ID")
                    #
                    # f = open(path_up, "rb")
                    # json_data = json.loads(f.read())
                    # f.close()
                    # print(json_data)
                    # up_products = json_data.get("Productos")
                    # print(up_products)
                    # up_nm_l=[]
                    # up_url_l=[]
                    # for i in up_products:
                    #     up_nm = i['Nombre']
                    #     up_url = i['URL_producto']
                    #     up_nm_l.append(up_nm)
                    #     up_url_l.append(up_url)
                    #
                    # up_nm_j='#||#'.join(up_nm_l)
                    # up_url_j='#||#'.join(up_url_l)
                    # print(up_nm_j)
                    # print(up_url_j)

                    print(prod_id_nw)
                    # =============================== NEW_LOGIC UP-SELLL =========================
                    if str(prod_id_nw) == '1931001':
                        prod_id_nw = '19310014'
                    else:
                        prod_id_nw = prod_id_nw
                    filename_up = f'/Product_{prod_id_nw}_upsell.html'
                    path_up = HTML_FOLDER_PATH + filename_up
                    path_up = path_up.replace("\\", "/")
                    print(path_up)
                    if os.path.exists(path_up):
                        with open(path_up, "r", encoding="utf-8")as f:
                            reviewbody = f.read()
                            re_text1 = reviewbody

                    else:
                        url1 = f'https://pdpr.coppelomnicanal.com/v0/get/recommendation/{prod_id_nw}/IZTAPALAPA/DISTRITO%20FEDERAL?key=AIzaSyCc-ujJjD_f3s0M282wMwrpZ9zxQdyVfC4'
                        re1 = requests.get(url=url1, headers=headers123)
                        print(re1.status_code)
                        re_text1 = re1.text
                        if re1.status_code != 200 or 'nav-logo-sprites' not in re1.text and '/errors/validateCaptcha' in re1.text:
                            print("UPSELL RESPONSE issue")
                            # time.sleep(3)
                            return None
                        else:
                            filename_up = f'/Product_{prod_id_nw}_upsell.html'
                            path_up = HTML_FOLDER_PATH + filename_up
                            path_up = path_up.replace("\\", "/")
                            with open(path_up, 'w', encoding="utf-8") as f:
                                f.write(re_text1)

                    """Leadtime"""
                    page_data_up = json.loads(re_text1)
                    page_data_p = page_data_up.get('Productos')
                    print(page_data_up)
                    if page_data_p == None or page_data_p == "":
                        dllobj.Upsell_Product_Name = "n/a"
                        dllobj.Upsell_URL = "n/a"
                    else:
                        up_nm_l = []
                        up_url_l = []
                        for i in page_data_p:
                            up_nm = i['Nombre']
                            up_url = i['URL_producto']
                            up_nm_l.append(up_nm)
                            up_url_l.append(up_url)

                        up_nm_j = '#||#'.join(up_nm_l)
                        up_url_j = '#||#'.join(up_url_l)
                        print(up_nm_j)
                        print(up_url_j)
                        if up_nm_j or up_url_j:
                            dllobj.Upsell_Product_Name = c_replace(up_nm_j)
                            dllobj.Upsell_URL = c_replace(up_url_j)
                        else:
                            dllobj.Upsell_Product_Name = "n/a"
                            dllobj.Upsell_URL = "n/a"

                    # =============================== NEW_LOGIC CROSS-SELLL =========================

                    if str(prod_id_nw) == '19310014':
                        prod_id_nw1 = '19310014'
                    else:
                        prod_id_nw1 = prod_id_nw
                    print(prod_id_nw)

                    filename_cp = f'/Product_{prod_id_nw1}_crosssell.html'
                    path_cp = HTML_FOLDER_PATH + filename_cp
                    path_cp = path_cp.replace("\\", "/")
                    print(path_cp)
                    if os.path.exists(path_cp):
                        with open(path_cp, "r", encoding="utf-8")as f:
                            reviewbody = f.read()
                            re_text1 = reviewbody

                    else:
                        url_cp = f'https://xsell.coppelomnicanal.com/v0/get/recommendation/{prod_id_nw1}/IZTAPALAPA/DISTRITO%20FEDERAL?key=AIzaSyBbDiJ7UOOauM0x6Kh-aKAJcZVctQGdfBM'
                        re1 = requests.get(url=url_cp, headers=headers123)
                        print(re1.status_code)
                        re_text1 = re1.text
                        if re1.status_code != 200 or 'nav-logo-sprites' not in re1.text and '/errors/validateCaptcha' in re1.text:
                            print("Review Response issue")

                            # time.sleep(3)
                        else:
                            filename_cp = f'/Product_{prod_id_nw1}_crosssell.html'
                            path_cp = HTML_FOLDER_PATH + filename_cp
                            path_cp = path_cp.replace("\\", "/")
                            with open(path_cp, 'w', encoding="utf-8") as f:
                                f.write(re_text1)

                    """ CROSS SELL JSON DATA"""
                    page_data_cp = json.loads(re_text1)
                    page_data_c = page_data_cp.get("Productos")
                    if page_data_c == None or page_data_c == "":
                        dllobj.Cross_dash_sell_Product_Name = "n/a"
                        dllobj.Cross_dash_sell_URL = "n/a"
                    else:

                        print(page_data_cp)
                        cp_nm_l = []
                        cp_url_l = []
                        for i in page_data_c:
                            cp_nm = i['Nombre']
                            cp_url = i['URL_producto']
                            cp_nm_l.append(cp_nm)
                            cp_url_l.append(cp_url)

                        cp_nm_j = '#||#'.join(cp_nm_l)
                        cp_url_j = '#||#'.join(cp_url_l)
                        if cp_nm_j or cp_url_j:
                            dllobj.Cross_dash_sell_Product_Name = c_replace(cp_nm_j)
                            dllobj.Cross_dash_sell_URL = c_replace(cp_url_j)
                        else:
                            dllobj.Cross_dash_sell_Product_Name = "n/a"
                            dllobj.Cross_dash_sell_URL = "n/a"

                    # ====================== CROSS-SELL PRODUCT ======================#
                    # if Product_ID != '' or Product_ID != 'n/a':
                    #     crossell_products = f'https://xsell.coppelomnicanal.com/v0/get/recommendation/2831663/IZTAPALAPA/DISTRITO%20FEDERAL?key=AIzaSyBbDiJ7UOOauM0x6Kh-aKAJcZVctQGdfBM'
                    #     filename_cp = f'/Product_2831663_Crossell.html'
                    #     path_cp = HTML_FOLDER_PATH + filename_cp
                    #     path_cp = path_cp.replace("\\", "/")
                    #     try:
                    #         if os.path.exists(path_cp):
                    #             # page save exists, so reading the saved page and loading the json file.
                    #             f = open(path_cp, "rb")
                    #             json_data = json.loads(f.read())
                    #             f.close()
                    #
                    #         else:
                    #             print(crossell_products)
                    #             crossell_product = requests.get(url=crossell_products, headers=headers123)
                    #
                    #             with open(path_cp, 'w')as f:
                    #                 f.write(crossell_product.text)

                    #     except:
                    #         print("..................................")
                    # else:
                    #     print("Not related Product_ID")
                    #
                    # print(json_data)
                    # cp_products = json_data.get("Productos")
                    # print(cp_products)
                    # cp_nm_l = []
                    # cp_url_l = []
                    # for i in cp_products:
                    #     cp_nm = i['Nombre']
                    #     cp_url = i['URL_producto']
                    #     cp_nm_l.append(cp_nm)
                    #     cp_url_l.append(cp_url)
                    #
                    # cp_nm_j = '#||#'.join(cp_nm_l)
                    # cp_url_j = '#||#'.join(cp_url_l)
                    # print(cp_nm_j)
                    # print(cp_url_j)

                    # ====================== CROSS-SELL PRODUCT ======================#

                    # --------------------------------- UP SELL PRODUCTS ----------------------------------
                    # try:
                    #     usp_lk = []
                    #     usp = response.xpath('//h2[contains(text(),"Productos similares")]/../following-sibling::div[@class="owl-carousel pdp-carrusel owl-theme owl-loaded owl-drag"]//a/@href').getall()
                    #     usp_name = response.xpath('//h2[contains(text(),"Productos similares")]/../following-sibling::div[@class="owl-carousel pdp-carrusel owl-theme owl-loaded owl-drag"]//a//div[@class="seccion-caracteristicas"]//p[@class="data-nombre"]//text()').getall()
                    #     for i in usp:
                    #         usp_lk.append("https://www.coppel.com" + i)
                    #     # print("usp_lk",usp_lk)
                    #     htp_usp = '#||#'.join(usp_lk)
                    #     usp_nam = '#||#'.join(usp_name)
                    #     if usp_lk:
                    #         dllobj.Upsell_Product_Name = c_replace(usp_nam)
                    #         dllobj.Upsell_URL = c_replace(htp_usp)
                    #         dllobj.Availability_Upsell = "Yes"
                    #     else:
                    #         dllobj.Upsell_Product_Name = "n/a"
                    #         dllobj.Upsell_URL = "n/a"
                    #         dllobj.Availability_Upsell = "No"
                    #
                    # except Exception as e:
                    #     print(e)
                    #     dllobj.Upsell_Product_Name = "n/a"
                    #     dllobj.Upsell_URL = "n/a"
                    #     dllobj.Availability_Upsell = "No"

                    # ====================== Sponsored/Adverrising_URL ======================#

                    try:

                        dllobj.Sponsored_backslash_Advertising_URL = "n/a"
                        dllobj.Sponsored_backslash_Advertising_Product_Name = "n/a"
                        dllobj.Availability_Sponsored_backslash_Advertising = "No"

                    except Exception as e:
                        print(e)

                    # ====================== List_What_in_the_box======================#

                    try:

                        dllobj.List_What_singlequote_s_in_the_box = 'n/a'
                        dllobj.Availability_What_singlequote_s_in_the_box = "No"

                    except Exception as e:
                        print(e)
                        dllobj.List_What_singlequote_s_in_the_box = 'n/a'
                        dllobj.Availability_What_singlequote_s_in_the_box = "No"

                    # ====================== Availability_product_badge ======================#

                    try:

                        dllobj.Availability_preferred_product__doublequote_badge_doublequote_ = "No"

                    except Exception as e:
                        print(e)

                    # ====================== Meta_Robot_Tag ======================#

                    try:

                        dllobj.Meta_Robots_No_Index_Tag = "n/a"

                    except Exception as e:
                        print(e)

                    # ====================== Availability of schema structred data ======================#

                    try:

                        dllobj.Availability_whitespace_of_whitespace_schema_whitespace_structured_whitespace_data = "Yes"

                    except Exception as e:
                        print(e)

                    # ====================== Availability_compatibility ======================#

                    try:

                        dllobj.Availability_Feature_Compatibility_space_for_space_ink = 'No'
                        dllobj.Availability_Feature_Compatibility_space_for_space_Toner = 'No'
                        dllobj.Availability_Feature_Compatibility_space_for_space_Page_space_Yield = 'No'

                    except Exception as e:
                        print(e)

                    # ====================== Keyword_include_product_name ======================#

                    try:

                        if str(dllobj.Lookup_Keyword).lower() in str(dllobj.Product_Name).lower():
                            dllobj.Keyword_backslash_s_space_included_space_in_space_product_space_name = 'Yes'
                        else:
                            dllobj.Keyword_backslash_s_space_included_space_in_space_product_space_name = 'No'

                    except Exception as e:
                        print(e)

                    # ====================== NEW--First_Carrousel_Product_Name =====================

                    try:

                        if dllobj.Upsell_Product_Name != "n/a" and dllobj.Cross_dash_sell_Product_Name != "n/a":
                            dllobj.First_Carrousel_Product_Name = c_replace(up_nm_j)
                            dllobj.Second_Carrousel_Product_Name = c_replace(cp_nm_j)
                        elif dllobj.Upsell_Product_Name != "n/a" and dllobj.Cross_dash_sell_Product_Name == "n/a":
                            dllobj.First_Carrousel_Product_Name = c_replace(up_nm_j)
                        elif dllobj.Upsell_Product_Name == "n/a" and dllobj.Cross_dash_sell_Product_Name != "n/a":
                            dllobj.First_Carrousel_Product_Name = c_replace(cp_nm_j)
                        else:
                            dllobj.First_Carrousel_Product_Name = "n/a"
                            dllobj.Second_Carrousel_Product_Name = "n/a"

                    except Exception as e:
                        print(e)

                    # # ====================== First_Carrousel_Product_Name ======================#
                    #
                    # try:
                    #     first_c =response.xpath('//h2[contains(text(),"Productos similares")]/../following-sibling::div[@class="owl-carousel pdp-carrusel owl-theme owl-loaded owl-drag"]//a//div[@class="seccion-caracteristicas"]//p[@class="data-nombre"]//text()').getall()
                    #     # print("First_c",first_c)
                    #     first_c_j = '#||#'.join(first_c).replace('"','/')
                    #     print("fIRST_C_J",first_c_j)
                    #
                    #     if first_c_j:
                    #         dllobj.First_Carrousel_Product_Name = c_replace(first_c_j)
                    #         dllobj.Availability_First_Carrousel = "Yes"
                    #     else:
                    #         dllobj.First_Carrousel_Product_Name = 'n/a'
                    #         dllobj.Availability_First_Carrousel = "No"
                    #
                    # except Exception as e:
                    #     print(e)
                    #     dllobj.First_Carrousel_Product_Name = 'n/a'
                    #     dllobj.Availability_First_Carrousel = "No"
                    #
                    # # ====================== Secound_Carrousel_Product_Name ======================#
                    #
                    # try:
                    #     sec_c = response.xpath('//h2[contains(text(),"Complementa tu compra")]//..//following-sibling::div//*[@id="owlStage2"]//div//a//div[@class="seccion-caracteristicas"]/p[@class="data-nombre"]//text()').getall()
                    #     sec_c_j = '#||#'.join(sec_c)
                    #
                    #     if sec_c_j:
                    #         dllobj.Second_Carrousel_Product_Name = c_replace(sec_c_j)
                    #         dllobj.Availability_Second_Carrousel = "Yes"
                    #     else:
                    #         dllobj.Second_Carrousel_Product_Name = 'n/a'
                    #         dllobj.Availability_Second_Carrousel = "No"
                    #
                    # except Exception as e:
                    #     print(e)
                    #     dllobj.Second_Carrousel_Product_Name = 'n/a'
                    #     dllobj.Availability_First_Carrousel = "No"

                    # ====================== Deliviery Lead Time ======================#

                    try:
                        dl = response.xpath('//span[@class="span-envio"]//p[@class="dias_envio"]//text()').get()
                        if dl:
                            dllobj.Delivery_Leadtime = c_replace(dl)
                        else:
                            dllobj.Delivery_Leadtime = "n/a"

                    except Exception as e:
                        print(e)
                        dllobj.Delivery_Leadtime = "n/a"

                    # ====================== Star_Rating ======================#

                    try:

                        dllobj.Product_Rating_greterthen_4 = 'n/a'
                        dllobj._1__Star = 'n/a'
                        dllobj._2__Star = 'n/a'
                        dllobj._3__Star = 'n/a'
                        dllobj._4__Star = 'n/a'
                        dllobj._5__Star = 'n/a'

                    except Exception as e:
                        print(e)

                    # ====================== Availability_of_R&R Manufacture Syndicate ======================#

                    try:

                        dllobj.Availability_space_of_space_Manufacturer_space_Syndication_space_Content = "No"
                        dllobj.R_ampercent_R_space_Manufacturer_space_Content_space_Syndicator_space_Name = "n/a"
                    except Exception as e:
                        print(e)
                        dllobj.Availability_space_of_space_Manufacturer_space_Syndication_space_Content = "No"
                        dllobj.R_ampercent_R_space_Manufacturer_space_Content_space_Syndicator_space_Name = "n/a"

                    # ====================== Avaialbility_#BRAND ======================#

                    try:

                        dllobj.Availability_space_of_space_why_space__singlequote__hash_Brand_singlequote__space_message = 'No'
                    except Exception as e:
                        print(e)
                        dllobj.Availability_space_of_space_why_space__singlequote__hash_Brand_singlequote__space_message = 'No'

                    # ====================== Avaialbility_schema_structured_data ======================#

                    try:

                        dllobj.Availability_space_of_space_schema_space_structured_space_data = "Yes"
                    except Exception as e:
                        print(e)
                        dllobj.Availability_space_of_space_schema_space_structured_space_data = "Yes"

                    # ====================== Avaialbility_secure_url_data ======================#

                    try:

                        dllobj.Availability_space_of_space_secure_space_URL_space_solution = "Yes"
                    except Exception as e:
                        print(e)
                        dllobj.Availability_space_of_space_secure_space_URL_space_solution = "Yes"

                    # ====================== Are page mobile-friendly ======================#

                    try:

                        dllobj.Are_space_pages_space_mobile_dash_friendly = "n/a"
                    except Exception as e:
                        print(e)
                        dllobj.Are_space_pages_space_mobile_dash_friendly = "n/a"

                    # ====================== Additional_header_1======================#

                    try:

                        dllobj.Additional_Header_1 = "n/a"
                    except Exception as e:
                        print(e)
                        dllobj.Additional_Header_1 = "n/a"

                    # ====================== R_R_Syndicate_nam_Availability======================#

                    try:

                        dllobj.Availability_space_of_space_R_ampercent_R_space_Manufacturer_space_Syndication_space_Content = "No"
                    except Exception as e:
                        print(e)
                        dllobj.Availability_space_of_space_R_ampercent_R_space_Manufacturer_space_Syndication_space_Content = "No"

                    # ====================== Manufacture_Content_Syndicator_name AND Availability======================#

                    try:

                        # mfs_cli=response.xpath('//h2[@class="panel-title"]/div[@class="iconoMenu"]').click()
                        mfs = response.xpath('//div[@id="contenidoIndexado"]//a//source/@srcset').extract_first(
                            default="").split('/')[2]
                        mfs_sp = mfs.split('.')[0:2]
                        mfs_j = '.'.join(mfs_sp)
                        print("MFS", mfs_j)

                        if mfs_j:
                            dllobj.Manufacturer_space_Content_space_Syndicator_space_Name = c_replace(mfs_j)
                            dllobj.Availability_space_of_space_Manufacturer_space_Syndication_space_Content = "Yes"
                        else:
                            dllobj.Manufacturer_space_Content_space_Syndicator_space_Name = "n/a"
                            dllobj.Availability_space_of_space_Manufacturer_space_Syndication_space_Content = "No"

                    except Exception as e:
                        print(e)
                        dllobj.Manufacturer_space_Content_space_Syndicator_space_Name = "n/a"
                        dllobj.Availability_space_of_space_Manufacturer_space_Syndication_space_Content = "No"

                    # ====================== Manufacture_Content ======================#

                    try:

                        if dllobj.Manufacturer_space_Content_space_Syndicator_space_Name == "n/a":
                            dllobj.Manufacturer_content = "No"
                        else:
                            dllobj.Manufacturer_content = "Yes"
                    except Exception as e:
                        print(e)

                    # ====================== ADDITIONAL_HEADER_12_13 ======================#

                    try:

                        dllobj.Additional_Header_12 = "n/a"
                        dllobj.Additional_Header_13 = "n/a"
                    except Exception as e:
                        print(e)

                    # ====================== Scrap_Completion ======================#

                    # try:
                    #     if dllobj.Product_Name == "n/a":
                    #         dllobj.Scrape_Completion = "Not Result"
                    #     else:
                    #         dllobj.Scrape_Completion = "n/a"
                    #
                    # except Exception as e:
                    #     print(e)

                    # # ====================== Page authority score greater than 40 ======================#+

                    try:
                        dllobj.Page_space_authority_space_score_space_greater_space_than_space_40 = "n/a"

                    except Exception as e:
                        print(e)
                        dllobj.Page_space_authority_space_score_space_greater_space_than_space_40 = "n/a"

                    # ====================== Additional hader 3 ======================#+

                    try:
                        if dllobj.Availability_specifications == "Yes":
                            dllobj.Additional_Header_3 = 'Y'
                        else:
                            dllobj.Additional_Header_3 = 'N'
                    except Exception as e:
                        print(e)

                    # ====================== Scrap_Completion ======================#

                    try:
                        dllobj.htmlpath_stock = "n/a"
                    except Exception as e:
                        print(e)
                        dllobj.htmlpath_stock = "n/a"

                    # ====================== Scrap_Completion ======================#

                    try:
                        dllobj.Review_space_out_space_of_space_stock_space_list_space_vs_space_offline_space_pages = "No"
                    except Exception as e:
                        print(e)

                    # # ====================== Page_Load_Time_80 ======================#

                    try:
                        dllobj.Page_space_loadtime_space__dash__space_Desktop_space__openingparentheses_Page_space_speed_space_score_greterthen_80_closingparentheses_ = "n/a"
                        dllobj.Page_space_loadtime_space__dash__space_Mobile_space__openingparentheses_Page_space_speed_space_score_greterthen_80_closingparentheses_ = "n/a"
                    except Exception as e:
                        print(e)

                    ## ------------- FOR QA CHECK ----------------------

                    strHtml = response.text
                    error_msgsdf = dllobj.QA_check(strHtml)

                    if error_msgsdf == "":
                        db = pymysql.connect(host=db_host, user=db_user, password=db_passwd, database=db_name)
                        cursor = db.cursor()
                        dllobj.update_table()
                        print(dllobj.update_table().encode('utf-8', 'replace').decode())
                        update_table_query = dllobj.update_table().encode('utf-8', 'replace').decode()
                        self.cursor.execute(update_table_query)
                        self.con.commit()
                    else:
                        print('QA function ERROR : {}'.format(error_msgsdf))

                else:

                    dllobj.Status = 'Not Found'
                    dllobj.Add_to_Cart = "No"
                    scrape_date = datetime.now().strftime('%m/%d/%Y')
                    image_name = infer_dict.get('image_name')
                    dllobj.id1 = str(infer_dict.get("row_id"))
                    dllobj.Additional_Header_2 = image_name.replace("\\", '')
                    dllobj.Scrape_Completion = "Not Result"
                    dllobj.row_id = infer_dict.get("row_id")
                    dllobj.htmlpath = path
                    dllobj.Partner_ID = infer_dict.get("Partner_ID")
                    dllobj.Partner_Name = infer_dict.get("Partner_Name")
                    dllobj.Country = infer_dict.get("Country")
                    dllobj.Scraping_Vendor_Name = infer_dict.get("Scraping_Vendor_Name")
                    dllobj.Product_URL = infer_dict.get("Product_URL")
                    dllobj.Brand = infer_dict.get("Brand")
                    dllobj.MPN_backslash_Model_Input = c_replace(str(infer_dict.get("MPN")))
                    dllobj.Product_Line = infer_dict.get("Product_Line")
                    dllobj.Category = infer_dict.get("Category")
                    dllobj.Subcategory = infer_dict.get("Subcategory")
                    dllobj.Scrape_Frequency = infer_dict.get("Scrape_Frequency")
                    dllobj.Scrape_Phase = infer_dict.get("Scrape_Phase")
                    dllobj.Scrape_Date = datetime.today().strftime("%m/%d/%Y")
                    # dllobj.Manufacturer_content = "No"
                    # dllobj.Availability_space_of_space_why_space__singlequote__hash_Brand_singlequote__space_message = "No"
                    detailed_partner_id = infer_dict.get("Detailed_Partner_ID")
                    dllobj.Detailed_Partner_ID = detailed_partner_id
                    dllobj.Availability_intrusive_Pop_dash_up_banners = "No"
                    dllobj.Additional_Header_3 = "N"
                    dllobj.screenshotpath = infer_dict.get("image_full_path").replace('\\', '/')
                    # dllobj.Availability_preferred_product__doublequote_badge_doublequote_ = "No"
                    # dllobj.Availability_Video = "No"
                    dllobj.FAQs_and_avoid_using_click_dash_to_dash_expand_content_blocks = "No"
                    dllobj.Availability_space_of_space_SEO_space_friendly_space_URL = "No"
                    dllobj.Keyword_backslash_s_space_included_space_in_space_product_space_name = "No"
                    dllobj.Availability_e_dash_Tail_headliner = "No"
                    dllobj.Content_space_visibility_space__openingparentheses_No_space_blocks_closingparentheses_ = "No"
                    dllobj.Feature_space_Keywords_Indoor_space_Air_space_Quality = infer_dict.get(
                        "Feature_Keywords_Indoor_Air_Quality")
                    dllobj.Lookup_Keyword = infer_dict.get("Lookup_Keyword")
                    dllobj.Scrape_frequency = infer_dict.get("Scrape_frequency")
                    dllobj.Feature_space_Keywords_Security = infer_dict.get("Feature_Keywords_Security")
                    dllobj.Feature_space_Keywords_Sustainability = infer_dict.get("Feature_Keywords_Sustainability")
                    dllobj.Product_ID="n/a"
                    # -------------------------------

                    dllobj.status = 'Not Found'

                    # dllobj.Scrape_Completion ="Not Result"
                    dllobj.Feature_space_Keywords_Quality = infer_dict.get('Feature_Keywords_Quality')
                    dllobj.Scrape_Date = scrape_date
                    dllobj.Product_ID = "n/a"
                    # dllobj.screenshotpath =  infer_dict.get("image_full_path")
                    dllobj.MPN_Output = 'n/a'
                    dllobj.First_Carrousel_Product_Name = "n/a"
                    dllobj.Second_Carrousel_Product_Name = "n/a"
                    dllobj.ASIN_backslash_UPC = 'n/a'
                    dllobj.EAN = 'n/a'
                    dllobj.Canonical_URL = 'n/a'
                    dllobj.Breadcrumbs = 'n/a'
                    dllobj.Product_Name = 'n/a'
                    dllobj.Availability_Product_Name = 'No'
                    dllobj.Stock_Message = 'n/a'
                    # dllobj.Stock_Status = 'n/a'
                    dllobj.Stock_Status = 'Out of Stock'
                    dllobj.Manufacturer_space_Content_space_Syndicator_space_Name = "n/a"
                    dllobj.Availability_space_of_space_Manufacturer_space_Syndication_space_Content = "No"
                    dllobj.R_ampercent_R_space_Manufacturer_space_Content_space_Syndicator_space_Name = "n/a"
                    dllobj.Availability_space_of_space_R_ampercent_R_space_Manufacturer_space_Syndication_space_Content = "No"
                    dllobj.Stock_Volume = 'n/a'
                    dllobj.Seller_Name = 'n/a'
                    dllobj.Seller_Type = 'n/a'
                    dllobj.Third_Party_Flag = 'False'
                    # dllobj.Delivery_Leadtime = "n/a"
                    dllobj.Delivery_Option = 'n/a'
                    dllobj.Product_description = 'n/a'
                    dllobj.Availability_product_description = 'No'
                    dllobj.Meta_title = 'n/a'
                    dllobj.Availability_meta_title = 'No'
                    dllobj.Meta_description = 'n/a'
                    dllobj.Availability_meta_description = 'No'
                    dllobj.No_of_customer_reviews = 'n/a'
                    dllobj.Availability_customer_reviews = 'No'
                    dllobj._No_of_customer_reviews_openingparentheses_21_closingparentheses__ = 'n/a'
                    dllobj.Product_Rating = 'n/a'
                    dllobj.Availability_product_rating = 'No'
                    dllobj.Product_Rating_greterthen_4 = 'n/a'
                    dllobj._1__Star = 'n/a'
                    dllobj._2__Star = 'n/a'
                    dllobj._3__Star = 'n/a'
                    dllobj._4__Star = 'n/a'
                    dllobj._5__Star = 'n/a'
                    dllobj.Feature_Bullets = 'n/a'
                    dllobj.Availability_Feature_Bullets = 'No'
                    dllobj.Product_specifications = 'n/a'
                    dllobj.Availability_specifications = 'No'
                    dllobj.Cross_dash_sell_URL = 'n/a'
                    dllobj.Cross_dash_sell_Product_Name = 'n/a'
                    dllobj.Availability_Cross_dash_sell = 'No'
                    dllobj.Cross_dash_sell_Location = 'n/a'
                    dllobj.Upsell_URL = 'n/a'
                    dllobj.Upsell_Product_Name = 'n/a'
                    dllobj.Availability_Upsell = 'No'
                    dllobj.Sponsored_backslash_Advertising_URL = 'n/a'
                    dllobj.Sponsored_backslash_Advertising_Product_Name = 'n/a'
                    dllobj.Availability_Sponsored_backslash_Advertising = 'No'
                    dllobj.Image_URLs = 'n/a'
                    dllobj.Availability_Image = 'No'
                    dllobj.Image_Alt_Text = 'n/a'
                    dllobj.Availability_alt_text_in_images = 'No'
                    dllobj.Availability_Video = 'No'
                    dllobj.List_What_singlequote_s_in_the_box = 'n/a'
                    dllobj.Availability_What_singlequote_s_in_the_box = 'No'
                    dllobj.Availability_e_dash_Tail_headliner = 'No'
                    dllobj.Availability_intrusive_Pop_dash_up_banners = 'No'
                    dllobj.Availability_preferred_product__doublequote_badge_doublequote_ = 'No'
                    dllobj.Availability_space_of_space_why_space__singlequote__hash_Brand_singlequote__space_message = 'No'
                    dllobj.Broken_URL = "n/a"
                    dllobj.FAQs_and_avoid_using_click_dash_to_dash_expand_content_blocks = 'No'
                    dllobj.Manufacturer_content = 'No'
                    dllobj.Header_Tag__openingparentheses_H1_Tag_closingparentheses_ = 'n/a'
                    dllobj.Meta_Robots_No_Index_Tag = 'n/a'

                    dllobj.Availability_space_of_space_SEO_space_friendly_space_URL = 'No'
                    dllobj.Content_space_visibility_space__openingparentheses_No_space_blocks_closingparentheses_ = 'No'
                    dllobj.Availability_Feature_Compatibility_space_for_space_ink = 'No'
                    dllobj.Availability_Feature_Compatibility_space_for_space_Toner = 'No'
                    dllobj.Availability_Feature_Compatibility_space_for_space_Page_space_Yield = 'No'
                    dllobj.Keyword_backslash_s_space_included_space_in_space_product_space_name = 'No'

                    dllobj.Availability_Breadcrumbs = 'No'

                    dllobj.Additional_Header_1 = 'n/a'
                    dllobj.Additional_Header_2 = infer_dict.get('image_name')
                    dllobj.Additional_Header_3 = "N"

                    # ---------- FOR QA CHECK ----------------------
                    print(dllobj.Product_Name)
                    strHtml = response.text
                    error_msgsdf = dllobj.QA_check(strHtml)
                    print(dllobj.Product_ID)
                    # @------------ UPDATE CONDITION CHECK ---------------------------
                    db = pymysql.connect(host=db_host, user=db_user, password=db_passwd, database=db_name)
                    cursor = db.cursor()
                    if error_msgsdf == "":
                        update_table_query = dllobj.update_table().encode('utf-8', 'replace').decode().replace('📦', '')
                        print(update_table_query)
                        cursor.execute(update_table_query)
                        db.commit()
                    else:
                        update_table_query = dllobj.update_table().encode('utf-8', 'replace').decode().replace('📦', '')
                        print(update_table_query)
                        print('QA function ERROR : {}'.format(error_msgsdf))

        except Exception as e:
            print(e)

    def close(spider, reason):

        try:
            # update counts
            feedid = "57"
            # a = common_code_100obj.found_query()
            # b = common_code_100obj.total_product_count()
            # c = common_code_100obj.not_found_query()
            # a = common_code_100obj.total_product_count
            # b = common_code_100obj.found_query
            # c = common_code_100obj.not_found_query


            feedcon = pymysql.connect(host=db_host, user=db_user, password=db_passwd, database=db_name)
            feedcursor = feedcon.cursor()

            # a = inkclubobj.total_product_count
            total_product_count = "SELECT count(*) FROM input_sku"
            feedcursor.execute(total_product_count)
            tpc = feedcursor.fetchall()
            a = tpc[0][0]

            found_query = f"SELECT count(id) FROM {product_data_table} WHERE STATUS='Done' AND Product_Name!=''"
            feedcursor.execute(found_query)
            fq = feedcursor.fetchall()
            b = fq[0][0]

            not_found_query = f"SELECT count(id) FROM {product_data_table} WHERE STATUS='Not Found'"
            feedcursor.execute(not_found_query)
            nfq = feedcursor.fetchall()
            c = nfq[0][0]
            feedcon.commit()
            feedcon.close()
            # update it to eoffice
            print("Updating to e-office....")
            dllobj.E_office_products_Update(feedid, str(a), str(b), str(c))
            db_ = pymysql.connect(host=db_host, user=db_user, password=db_passwd, database=db_name)
            cursor_ = db_.cursor()
            checksql = f"""select count(*) from {product_data_table} where Status='Pending'"""
            cursor_.execute(checksql)
            result = cursor_.fetchall()

            if result == ((0,),):
                print("no pending..going to make tsv...")
                from ugam_copple_mx.export_tsv import Export_TSV
                print('create TSV')
                c = Export_TSV()
                c.export_tsv()
            else:
                print("Some entries still pending..calling spider again")

        except Exception as e:
            print('exception in export csv / tsv method call time or updating to e office', e)

if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute('scrapy crawl ugam_prj -a start=1 -a end=45'.split())
