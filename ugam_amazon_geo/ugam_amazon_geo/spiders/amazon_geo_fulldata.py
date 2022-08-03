import hashlib
import time
import html
import datetime
import os
import scrapy
from ugam_amazon_geo.config import *
from ugam_amazon_geo.pipelines import *
from ugam_amazon_geo.items import *
from mymodules._common_ import c_replace
from scrapy.selector import Selector
import requests
import json
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from mymodules._common_ import c_replace
import re
proxystorm={"https":"lum-customer-c_11e7173f-zone-zone_us:33p04eaqxtpu@zproxy.lum-superproxy.io:22225",
            "http":"lum-customer-c_11e7173f-zone-zone_us:33p04eaqxtpu@zproxy.lum-superproxy.io:22225"}


def unknownrepl(s):
    s = c_replace(s)
    a = s.encode('unicode_escape').decode('ascii')
    r = r'\\u[\w]{4}'
    c = c_replace(re.sub(r, '', a))
    c = c_replace(c)
    return c

handle_httpstatus_list = [404,403]

class Amazon_Geo(scrapy.Spider):
    name = 'AmazonGeo'

    handle_httpstatus_list = [404,403]
    F_PATH = HTML

    def __init__(self, start='', end=''):

        try:
            self.cursor = UgamAmazonGeoPipeline.cursor
            self.con = UgamAmazonGeoPipeline.con
            self.start = start
            self.end = end
        except Exception as e:
            logger.error('exception in __init__ method main:{}'.format(e))

    def start_requests(self):

        try:
            self.cursor = UgamAmazonGeoPipeline.cursor
            self.con = UgamAmazonGeoPipeline.con
            brand_select = f"select Id,url,zipcode_input from {product_table} where Status = 'Pending' AND Id BETWEEN {self.start} AND {self.end}"
            # brand_select = f"select Id,searchterm from {db_brand_table} where Status = 'Pending'"

            self.cursor.execute(brand_select)
            brand_list = [column for column in self.cursor.fetchall()]

            for item in brand_list:
                row_id=item[0]
                url=item[1]
                zipcode = item[2]

                cookie = 'SELECT zipcode,cookies FROM cookies'
                self.cursor.execute(cookie)
                cookie = [column for column in self.cursor.fetchall()]

                for c in cookie:
                    zipcodec=c[0]
                    cookie=c[1]

                    if zipcode==zipcodec:

                        headers = {
                            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            "cookie": cookie,
                            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
                            "sec-fetch-site": "same-origin",
                            "sec-ch-ua-platform": '"Windows"',
                            'scheme': 'https',
                        }

                        # print(headers)
                        # mydata = json.loads(resp.text)
                        p_id = url.split('dp/')[1].split('/')[0]
                        if "?" in p_id:
                            p_id = p_id.split("?")
                            p_id = p_id[0]
                        else:
                            p_id = p_id

                        filename = f'/{row_id}_{p_id}_{zipcode}.html'
                        path = self.F_PATH + filename
                        path = path.replace("\\", "/")

                        time.sleep(1)
                        if os.path.exists(path):
                            yield scrapy.FormRequest(url=f'file:///{path}', callback=self.parse, dont_filter=True,
                                                     meta={'row_id': row_id, 'p_url': url, 'zpcode': zipcode})
                        else:
                            time.sleep(2)
                            yield scrapy.FormRequest(url=url, callback=self.parse,  headers=headers, dont_filter=True,
                                                     meta={'row_id': row_id, 'p_url': url, 'zpcode': zipcode})

        except Exception as e:
            logger.error('exception in start requests method main: {}'.format(e))

    def parse(self, response, **kwargs):

        print(response.status)
        row_id = response.meta.get('row_id')
        p_url = response.meta.get('p_url')
        zipcode = response.meta.get('zpcode')

        # if "Sorry! We couldn't find that page. Try searching or go to Amazon's home page." or "Amazon.com Page Not Found" not in response.text:
        if "Sorry! We couldn't find that page. Try searching or go to Amazon's home page." not in response.text and "Amazon.com Page Not Found" not in response.text:

            p_id = p_url.split('dp/')[1].split('/')[0]
            if "?" in p_id:
                p_id = p_id.split("?")
                p_id = p_id[0]
            else:
                p_id = p_id
            filename = f'/{row_id}_{p_id}_{zipcode}.html'
            path = self.F_PATH + filename
            path = path.replace("\\", "/")


            if zipcode in response.text:
                if os.path.exists(path):
                    pass
                else:
                    time.sleep(2)
                    with open(path, 'w', encoding='utf-8')as f:
                        time.sleep(1)
                        f.write(response.text)

            else:
                print("---- ZIPCODE NOT IN PAGE ------")

            # TODO -------  ITEMS CALL --------------

            item = UgamAmazonGeoItem()
            item['Id'] = row_id

            # TODO ----------- HEADERS SCRAPE------------------

            # TODO ----------- CATEGORY BREADCUMBS ------------

            try:
                category = response.xpath('//div[@id="wayfinding-breadcrumbs_container"]//ul/li/span[@class="a-list-item"]//text()').getall()
                if category==[]:
                    item['category_path']="n/a"
                else:
                    category=c_replace(category)
                    bread = '#||#'.join(category)
                    nw_bread = c_replace(bread).replace('"','')
                    print(nw_bread)
                    item['category_path'] = c_replace(nw_bread)
            except Exception as e:
                print(e)

            # TODO ----------- Product Image ------------

            try:
                prd_img = response.xpath('//div[@id="imgTagWrapperId"]/img/@src').get()
                nw_prd_img = c_replace(prd_img).replace('"','')
                print(nw_prd_img)
                item['Product_image'] = c_replace(str(nw_prd_img))

            except Exception as e:
                print(e)

            # TODO ----------- Product Name ------------

            try:
                prd_name = response.xpath('//h1/span/text()').get()
                nw_prd_name = c_replace(prd_name)
                nw_prd_nm=nw_prd_name.replace('"',"'")
                print(nw_prd_nm)
                item['Product_Name']=unknownrepl(nw_prd_nm)
            except Exception as e:
                print(e)

            # TODO ----------- MARKDOWN PRICE ------------

            try:
                mrk_price = response.xpath('//div[@id="apex_desktop"]//span[@class="a-price aok-align-center reinventPricePriceToPayMargin priceToPay"]//text()').get()
                if mrk_price==None:
                    mrk_price=response.xpath('//div[@id="apex_desktop"]//span[@class="a-price a-text-price"]//span//text()').get()

                    if mrk_price==None:
                        mrk_price=response.xpath('//div[@id="apex_desktop"]//span[@class="a-price a-text-price a-size-medium apexPriceToPay"]//span//text()').get()
                        if mrk_price:
                            nw_mrk_price = c_replace(mrk_price).replace('"', '')
                            print(nw_mrk_price)
                        else:
                            nw_mrk_price="n/a"
                    else:
                        if mrk_price:
                            nw_mrk_price = c_replace(mrk_price).replace('"', '')
                            print(nw_mrk_price)
                        else:
                            nw_mrk_price="n/a"
                else:
                    if mrk_price:
                        nw_mrk_price = c_replace(mrk_price).replace('"', '')
                        print(nw_mrk_price)
                    else:
                        nw_mrk_price="n/a"
            except Exception as e:
                print(e)
                nw_mrk_price = "n/a"

            # TODO ----------- Regular Price ------------

            try:
                regu_price = response.xpath('//div[@id="apex_desktop"]//*[contains(text(),"List Price:")]//span//span//text()').get()
                if regu_price == None:
                    regu_price=response.xpath('//div[@id="apex_desktop"]//*[contains(text(),"List Price:")]//..//span[@class="a-price a-text-price a-size-base"]//span//text()').get()
                    if regu_price==None:
                        regu_price=response.xpath('//div[@id="apex_desktop"]//*[contains(text(),"Was:")]//span//span//text()').get()
                        if regu_price:
                            nw_regu_price = c_replace(regu_price)
                            print(regu_price)
                        else:
                            nw_regu_price = "n/a"
                    else:
                        nw_regu_price = c_replace(regu_price)
                        print(regu_price)
                else:
                    nw_regu_price = c_replace(regu_price)
                    print(regu_price)
            except Exception as e:
                print(e)
                nw_regu_price = "n/a"

            # TODO ----------- Product_ID  ------------

            try:
                product_id = p_url.split('dp/')[1].split('/')[0]

                if "?" in product_id:
                    product_id = product_id.split("?")
                    product_id = product_id[0]
                else:
                    product_id = product_id

                item['product_id'] = c_replace(product_id)
            except Exception as e:
                print(e)

            # TODO ----------- Manufacture_PART_NUMBER  ------------

            try:
                part_num = response.xpath('//*[contains(text(),"Part Number")]/following-sibling::td//text()').get()
                if part_num == None:
                    nw_part_num = "n/a"
                else:
                    nw_part_num = c_replace(part_num).replace('"','')

            except Exception as e:
                print(e)
                nw_part_num = "n/a"

            # TODO ----------- Brand Name  ------------

            try:
                brandname = response.xpath('//table[@id="productDetails_techSpec_section_1"]//*[contains(text(),"Brand")]//..//td//text()').get()

                if not brandname:
                    brandname1=response.xpath('//table[@class="a-normal a-spacing-micro"]//*[contains(text(),"Brand")]//../following-sibling::td/span/text()').get()

                    if not brandname1:
                        brandname2=response.xpath('//table[@id="product-specification-table"]//*//*[contains(text(),"Brand")]//..//td').get()

                        if not brandname2:
                            brandname3=response.xpath('//div[@class="a-section a-spacing-none"]/a[@id="bylineInfo"]//text()').get()

                            if brandname3:
                                if 'Brand' in brandname3:
                                    brandname3=brandname3.split(':')[-1]
                                    brandname3 = c_replace(brandname3)
                                    nw_brandname = brandname3
                                else:
                                    nw_brandname='n/a'
                            else:
                                nw_brandname="n/a"
                        else:
                            if brandname2:
                                brandname2=c_replace(brandname2)
                                nw_brandname=brandname2
                            else:
                                nw_brandname="n/a"

                    else:
                        if brandname1:
                            nw_brandname = c_replace(brandname1).replace('"','')
                            print(nw_brandname)
                        else:
                            nw_brandname="n/a"
                else:
                    if brandname:
                        nw_brandname = c_replace(brandname).replace('"','')
                        print(nw_brandname)
                    else:
                        nw_brandname = "n/a"

            except Exception as e:
                print(e)
                nw_brandname = "n/a"


            # TODO ----------- Colour Finish  ------------

            try:
                colour_finsh1=response.xpath('//table[@id="productDetails_techSpec_section_1"]//*[contains(text(),"Color")]//..//td//text()').get()
                if not colour_finsh1:
                    colour_finsh2 = response.xpath('//table[@id="product-specification-table"]//*[contains(text(),"Color")]//..//td//text()').get()
                    if colour_finsh2:
                        mn_colour = c_replace(colour_finsh2).replace('"', '')
                    else:
                        colour_finsh3 = response.xpath('//table[@id="productDetails_detailBullets_sections1"]//*[contains(text(),"Color")]//..//td//text()').get()
                        if colour_finsh3:
                            mn_colour = c_replace(colour_finsh2).replace('"', '')
                        else:
                            # colour_finsh4 = response.xpath('//table[@class="a-normal a-spacing-micro"]//*[contains(text(),"Color")]//../following-sibling::td/span/text()').get()
                            colour_finsh4 = response.xpath('//table[@class="a-normal a-spacing-micro"]//*[contains(text(),"Color")]//text()').getall()
                            if "Color Temperature" in colour_finsh4 or colour_finsh4==[]:
                                mn_colour = "n/a"
                            else:
                                colour_finsh4 = response.xpath('//table[@class="a-normal a-spacing-micro"]//*[contains(text(),"Color")]//../following-sibling::td/span/text()').get()
                                mn_colour = c_replace(colour_finsh4).replace('"', '')
                else:
                    if "Kelvin" in colour_finsh1:
                        mn_colour = "n/a"
                    else:
                        print(len(colour_finsh1[0]))
                        mn_colour = c_replace(colour_finsh1).replace('"', '')

            except Exception as e:
                print(e)
                mn_colour="n/a"

            # TODO ----------- Capacity  ------------

            try:
                key=response.xpath('//table[@id="product-specification-table"]//tr//th//text()').getall()
                val=response.xpath('//table[@id="product-specification-table"]//tr//td//text()').getall()

                if key==[]:
                    key=response.xpath('//table[@id="productDetails_techSpec_section_1"]//tr//th//text()').getall()
                    val=response.xpath('//table[@id="productDetails_techSpec_section_1"]//tr//td//text()').getall()

                    if key==[]:
                        nw_cap="n/a"
                    else:
                        cap = {}
                        for i, j in zip(key,val):
                            cap[i] = j
                        print(cap)
                        nw_cap = ''
                        for x, l in cap.items():
                            if 'Capacity' in x:
                                nw_cap = nw_cap + l
                                break
                        print(nw_cap)
                        if nw_cap=='':
                            nw_cap='n/a'
                        else:
                            nw_cap=nw_cap
                else:
                    cap={}
                    for i,j in zip(key,val):
                        cap[i]=j
                    print(cap)
                    nw_cap=''
                    for x,l in cap.items():
                        if 'Capacity' in x:
                            nw_cap=nw_cap+l
                            break
                    print(nw_cap)
                    if nw_cap=='':
                        nw_cap="n/a"
                    else:
                        nw_cap=nw_cap
            except Exception as e:
                print(e)
                nw_cap = "n/a"

            # TODO ----------- Installation_Type  ------------

            try:
                keys = response.xpath('//table[@id="productDetails_techSpec_section_1"]//tr//th//text()').getall()
                vals = response.xpath('//table[@id="productDetails_techSpec_section_1"]//tr//td//text()').getall()

                if keys == []:
                    nw_install1 = "n/a"
                else:
                    cap = {}
                    for i, j in zip(keys, vals):
                        cap[i] = j
                    print(cap)
                    nw_install1 = ''
                    for x, l in cap.items():
                        if 'Installation' in x:
                            nw_install1 = nw_install1 + l
                            break
                    print(nw_install1)
                    if nw_install1 == '':
                        nw_install1 = 'n/a'
                    else:
                        nw_install1 = nw_install1
                # install1 = response.xpath('//table[@id="productDetails_techSpec_section_1"]//*[contains(text(),"Installation")]//..//td//text()').get()
            except Exception as e:
                print(e)
                nw_install1 = "n/a"

            # TODO ----------- Product Description  ------------

            try:
                prod_desc = response.xpath('//*[contains(text(),"Product Description")]//..//..//div[@id="productDescription"]//p//span//text()').getall()

                if prod_desc == [] or prod_desc==[' '] or prod_desc[0]=="Specs:":
                    prod_desc = response.xpath('//*[contains(text(),"Product Description")]//..//div[@class="a-section launchpad-text-left-justify"]/p//text()').getall()

                    if prod_desc==[] or prod_desc==[' '] or prod_desc[0]=="Specs:":
                        prod_desc=response.xpath('//*[contains(text(),"Product Description")]//..//..//p[@class="a-spacing-base"]//text()').getall()

                        if prod_desc==[] or prod_desc==[' '] or prod_desc[0]=="Specs:":
                            prod_desc=response.xpath('//*[contains(text(),"Product Description")]//..//div[@class="apm-sidemodule-textright"]//p//text()').getall()

                            if prod_desc==[] or prod_desc==[' '] or prod_desc[0]=="Specs:":

                                prod_desc=response.xpath('//*[contains(text(),"Specs:")]//../following-sibling::ul/li/span//text()').getall()

                                if prod_desc == [] or prod_desc == [' '] or prod_desc[0] == "Specs:":
                                    prod_desc=response.xpath('//*[contains(text(),"Product Description")]//../..//p/span/text()').getall()

                                    if prod_desc==[] or prod_desc==[' '] or prod_desc[0]=="Specs:":
                                        nw_prod_desc="n/a"
                                    else:
                                        j_prod_desc = ''.join(prod_desc)
                                        nw_prod_desc = c_replace(j_prod_desc.replace('"', ''))
                                        print(nw_prod_desc)
                                else:
                                    j_prod_desc = ''.join(prod_desc)
                                    nw_prod_desc = c_replace(j_prod_desc.replace('"', ''))
                                    print(nw_prod_desc)

                            else:
                                j_prod_desc = ''.join(prod_desc)
                                nw_prod_desc = c_replace(j_prod_desc.replace('"', ''))
                                print(nw_prod_desc)
                        else:
                            j_prod_desc = ''.join(prod_desc)
                            # nw_prod_desc=j_prod_desc.replace('💎','')
                            nw_prod_desc = c_replace(j_prod_desc.replace('"',''))
                            print(nw_prod_desc)
                    else:
                        j_prod_desc = ''.join(prod_desc)
                        nw_prod_desc = c_replace(j_prod_desc.replace('"', ''))
                        print(nw_prod_desc)

                else:
                    if prod_desc:
                        j_prod_desc = ''.join(prod_desc)
                        nw_prod_desc = c_replace(j_prod_desc.replace('"',''))
                        print(nw_prod_desc)
                    else:
                        nw_prod_desc = "n/a"

            except Exception as e:
                print(e)
                nw_prod_desc = "n/a"


            item['htmlpath'] = path
            item['extraction_date'] = datetime.today().strftime('%d/%m/%Y %H:%M:%S %p')
            # item['Product image'] = c_replace(nw_prd_img)
            # item['category_path'] = c_replace(nw_bread)
            # item['Product Name'] = c_replace(nw_prd_name)
            item['Markdown_Price'] = c_replace(nw_mrk_price)
            item['regular_price'] = c_replace(nw_regu_price)
            # item['product_id'] = c_replace(product_id)
            item['Manufacturer_Part_Number'] = c_replace(nw_part_num)
            item['Brand_Name'] = c_replace(nw_brandname)
            item['Color_Finish'] = c_replace(mn_colour)
            item['Capacity'] = c_replace(nw_cap)
            item['Installation_type'] = c_replace(nw_install1)
            item['Detailed_Specification'] = "n/a"
            item['Product_Description'] = c_replace(nw_prod_desc)
            item['zipcode_site'] = "n/a"
            item['Status']="Done"

            yield item

        else:

            p_id = p_url.split('dp/')[1].split('/')[0]
            if "?" in p_id:
                p_id=p_id.split("?")
                p_id=p_id[0]
            else:
                p_id=p_id

            filename = f'/{row_id}_{p_id}_{zipcode}.html'
            path = self.F_PATH + filename
            path = path.replace("\\", "/")

            if os.path.exists(path):
                pass
            else:
                try:
                    with open(path, 'w', encoding='utf-8')as f:
                        f.write(response.text)
                except Exception as e:
                    print(e)

            item=UgamAmazonGeoItem()
            item['Id']=row_id
            item['htmlpath'] = path
            item['extraction_date'] = datetime.today().strftime('%d/%m/%Y %H:%M:%S %p')
            item['Product_image'] = "n/a"
            item['category_path'] = "n/a"
            item['Product_Name'] = "n/a"
            item['Markdown_Price'] = "n/a"
            item['regular_price'] = "n/a"
            item['product_id'] = "n/a"
            item['Manufacturer_Part_Number'] = "n/a"
            item['Brand_Name'] = "n/a"
            item['Color_Finish'] = "n/a"
            item['Capacity'] = "n/a"
            item['Installation_type'] = "n/a"
            item['Detailed_Specification'] = "n/a"
            item['Product_Description'] = "n/a"
            item['zipcode_site']="n/a"
            item['Status'] = "Not Found"

            yield item

    def close(spider, reason):
        try:
            con = UgamAmazonGeoPipeline.con
            import pandas as pd
            sql_query = pd.read_sql_query(f'SELECT `uniqueIdentifier`,`extraction_date`,`category_path`,`Product_image`,`url`,`Product_Name`,`Markdown_Price`,`regular_price`,`product_id`,`Manufacturer_Part_Number`,`Brand_Name`,`Color_Finish`,`Capacity`,`Installation_type`,`Detailed_Specification`,`Product_Description`,`zipcode_input` from {product_table} where Status="Done"' , con)
            df = pd.DataFrame(sql_query)
            df.to_csv(f'Ugam_Amazon_us_{today_date}.csv', encoding='utf-8-sig', index=False)
            print("---------------------**********************************-------------------------------")
            print("create File")

        except Exception as e:
            print(e)


if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute('scrapy crawl AmazonGeo -a start=5694 -a end=5694'.split())
