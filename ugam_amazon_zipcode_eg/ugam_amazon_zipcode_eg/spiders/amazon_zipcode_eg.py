import hashlib
import time
import html
import datetime
import os
import scrapy
from ugam_amazon_zipcode_eg.config import *
from ugam_amazon_zipcode_eg.pipelines import *
from ugam_amazon_zipcode_eg.items import *
from mymodules._common_ import c_replace
from scrapy.selector import Selector
import requests
import json
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from mymodules._common_ import c_replace
import re
from random_user_agent.params import SoftwareName, OperatingSystem
from random_user_agent.user_agent import UserAgent
from random import choice


def get_useragent():
    l1 = [SoftwareName.CHROME.value, SoftwareName.FIREFOX.value, SoftwareName.OPERA.value]
    software_names = [choice(l1)]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value, OperatingSystem.SUNOS.value]
    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=1000)
    return user_agent_rotator.get_random_user_agent()


def unknownrepl(s):
    s = c_replace(s)
    a = s.encode('unicode_escape').decode('ascii')
    r = r'\\u[\w]{4}'
    c = c_replace(re.sub(r, '', a))
    c = c_replace(c)
    return c

class Amazon_Geo_EG(scrapy.Spider):
    name = 'AmazonGeoGE'

    handle_httpstatus_list = [404, 403, 407]
    F_PATH = HTML

    def __init__(self, start='', end=''):

        try:
            self.cursor = UgamAmazonZipcodeEgPipeline.cursor
            self.con = UgamAmazonZipcodeEgPipeline.con
            self.start = start
            self.end = end
        except Exception as e:
            logger.error('exception in __init__ method main:{}'.format(e))

    def start_requests(self):

        try:
            self.cursor = UgamAmazonZipcodeEgPipeline.cursor
            self.con = UgamAmazonZipcodeEgPipeline.con
            brand_select = f"select ID,Product_URL,postcode from {product_table} where Status = 'Pending' AND Id BETWEEN {self.start} AND {self.end}"

            self.cursor.execute(brand_select)
            brand_list = [column for column in self.cursor.fetchall()]

            for item in brand_list:
                row_id = item[0]
                url = item[1]
                postcode = item[2]

                cookie = 'SELECT zipcode,cookies FROM cookies'
                self.cursor.execute(cookie)
                cookie = [column for column in self.cursor.fetchall()]

                for c in cookie:
                    zipcodec = c[0]
                    cookie = c[1]

                    if postcode == zipcodec:

                        headers = {
                            'authority': 'www.amazon.com',
                            'accept-language': 'en-US,en;q=0.9',
                            'method':'GET',
                            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                            "cookie": f'{cookie}',
                            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
                            "sec-fetch-site": "same-origin",
                            "sec-ch-ua-platform": '"Windows"',
                            'scheme': 'https',
                        }

                        # print(headers)
                        # headers['x-requested-with'] = "XMLHttpRequest"
                        # headers['X-Crawlera-Cookies'] = "disable"
                        # scre=f'http://api.scraperapi.com/?api_key=4c90a6838c880e80492c51eaac9734d3&url={url}&keep_headers=true&country_code=us'
                        # print(headers)
                        # mydata = json.loads(resp.text)

                        p_id = url.split('dp/')[1].split('#')[0]
                        if "?" in p_id:
                            p_id = p_id.split("?")
                            p_id = p_id[0]
                        else:
                            p_id = p_id

                        filename = f'/{row_id}_{p_id}_{postcode}.html'
                        path = self.F_PATH + filename

                        if os.path.exists(path):
                            yield scrapy.FormRequest(url=f'file:///{path}', callback=self.parse, dont_filter=True,
                                                     meta={'row_id': row_id, 'p_url': url, 'zpcode': postcode})
                        else:
                            main_req = requests.get(f'http://api.scraperapi.com/?api_key=4c90a6838c880e80492c51eaac9734d3&url={url}=1&country_code=us&keep_headers=true',headers=headers)
                            if zipcodec in main_req.text:
                                print("yes")
                            else:
                                print("Zip code is not selected-----")
                                continue

                            with open(path, 'w', encoding='utf-8') as f:
                                f.write(main_req.text)

                            path = path.replace("/", "\\")
                            path = path.replace("\\\\", "\\")

                            yield scrapy.FormRequest(url=f'file:{path}', callback=self.parse, headers=headers, dont_filter=True,
                                                     meta={'row_id': row_id, 'p_url': url, 'zpcode': postcode})

        except Exception as e:
            logger.error('exception in start requests method main: {}'.format(e))

    def parse(self, response, **kwargs):

        print(response.status)
        row_id = response.meta.get('row_id')
        p_url = response.meta.get('p_url')
        zipcode = response.meta.get('zpcode')

        if "Sorry! We couldn't find that page. Try searching or go to Amazon's home page." not in response.text and "Amazon.com Page Not Found" not in response.text:

            p_id = p_url.split('dp/')[1].split('#')[0]
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

            else:
                print("-----ZIPCODE NOT FOUND IN PAGE-----")

            # TODO -------  ITEMS CALL ----------------

            item = UgamAmazonZipcodeEgItem()
            item['ID'] = row_id

            # TODO ----------- Product Name ------------

            try:
                prd_name = response.xpath('//h1/span/text()').get()
                nw_prd_name = c_replace(prd_name)
                nw_prd_nm = nw_prd_name.replace('"', "'")
                print(nw_prd_nm)
                item['product_name'] = c_replace(nw_prd_nm)

            except Exception as e:
                print(e)

            # TODO ----------- Product_ID  ------------

            try:
                product_id = p_url.split('dp/')[1].split('#')[0]

                if "?" in product_id:
                    product_id = product_id.split("?")
                    product_id = product_id[0]
                else:
                    product_id = product_id

                item['ProductID'] = product_id
            except Exception as e:
                print(e)

            # TODO ----------- CATEGORY BREADCUMBS ------------

            try:
                category = response.xpath('//div[@id="wayfinding-breadcrumbs_container"]//ul/li/span[@class="a-list-item"]//text()').getall()
                if category == []:
                    nw_bread = "n/a"
                else:
                    category = c_replace(category)
                    bread = ' > '.join(category)
                    nw_bread = c_replace(bread).replace('"', '')
                    print(nw_bread)

                item['site_category_path'] = c_replace(nw_bread)
            except Exception as e:
                print(e)

            # TODO ----------- MARKDOWN PRICE ------------

            try:
                mrk_price = response.xpath('//div[@id="apex_desktop"]//span[@class="a-price aok-align-center reinventPricePriceToPayMargin priceToPay"]/span[@class="a-offscreen"]//text()').get()
                if mrk_price == None:
                    mrk_price = response.xpath('//div[@id="apex_desktop"]//span[@class="a-price a-text-price a-size-medium apexPriceToPay"]//span//text()').get()
                    if mrk_price:
                        nw_mrk_price = c_replace(mrk_price).replace('"', '')
                        print(nw_mrk_price)
                    else:
                        nw_mrk_price = "n/a"
                else:
                    if mrk_price:
                        nw_mrk_price = c_replace(mrk_price).replace('"', '')
                        print(nw_mrk_price)
                    else:
                        nw_mrk_price = "n/a"

                item['Price'] = c_replace(nw_mrk_price)

            except Exception as e:
                print(e)
                nw_mrk_price = "n/a"


            # TODO ------------- Ship_From -------------------

            try:
                ship_fr=response.xpath('//div[@id="tabular-buybox"]//*[contains(text(),"Ships from")]//..//../following-sibling::div[@tabular-attribute-name="Ships from"]/div/span/text()').get()

                if ship_fr==None:
                    nw_ship="n/a"
                else:
                    nw_ship=ship_fr

                item['Ships_from'] = c_replace(nw_ship)
            except Exception as e:
                print(e)

            # TODO ------------- SOLD BY --------------------

            try:
                sold_by=response.xpath('//div[@id="tabular-buybox"]//*[contains(text(),"Sold by")]//..//../following-sibling::div[@tabular-attribute-name="Sold by"]/div/span/text()').get()

                if sold_by==None:
                    sold_by=response.xpath('//div[@id="tabular-buybox"]//*[contains(text(),"Sold by")]//..//../following-sibling::div[@tabular-attribute-name="Sold by"]/div/span/a/text()').get()
                    if sold_by==None:
                        nw_sold_by="n/a"
                    else:
                        nw_sold_by=sold_by
                else:
                    nw_sold_by=sold_by

                item['Sold_by'] = c_replace(nw_sold_by)
            except Exception as e:
                print(e)


            # TODO ---------earliest_delivery_date-----------

            try:
                early_1=response.xpath('//div[@id="mir-layout-DELIVERY_BLOCK-slot-PRIMARY_DELIVERY_MESSAGE_LARGE"]//span//span[@class="a-text-bold"]//text()').get()
                if early_1:
                    early_2=response.xpath('//div[@id="mir-layout-DELIVERY_BLOCK-slot-PRIMARY_DELIVERY_MESSAGE_LARGE"]//span/span/following-sibling::text()').get()
                    if early_2==None:
                        mn_early=f'FREE delivery: {early_1}'
                    else:
                        mn_early = f'FREE delivery: {early_1} {early_2}'
                else:
                    mn_early="n/a"

                item['earliest_delivery_date'] = c_replace(mn_early)
            except Exception as e:
                print(e)


            # TODO --------- Fastest_delivery--------------
            try:
                fast_del=response.xpath('//div[@id="mir-layout-DELIVERY_BLOCK-slot-SECONDARY_DELIVERY_MESSAGE_LARGE"]//span/span[@class="a-text-bold"]//text()').get()
                if fast_del:
                    fast_del1=response.xpath('//div[@id="mir-layout-DELIVERY_BLOCK-slot-SECONDARY_DELIVERY_MESSAGE_LARGE"]//span/span[@class="a-text-bold"]/following-sibling::text()').get()
                    fast_del2=response.xpath('//div[@id="mir-layout-DELIVERY_BLOCK-slot-SECONDARY_DELIVERY_MESSAGE_LARGE"]//span//span[@id="ftCountdown"]//text()').get()

                    if fast_del1==None and fast_del2==None:
                        mn_fast = f"Fastest delivery: {fast_del}"
                    else:
                        mn_fast = f"Fastest delivery: {fast_del} {fast_del1} {fast_del2}"

                else:
                    mn_fast="n/a"

                item['Fastest_delivery'] = c_replace(mn_fast)

            except  Exception as e:
                print(e)


            # TODO -------- promo_message ---------------
            try:
                promo=response.xpath('//div[@id="apex_desktop"]//div[@id="freeShippingPriceBadging_feature_div"]//span[@class="a-size-base"]//text()').getall()
                if promo==[]:
                    fre_re=response.xpath('//div[@id="apex_desktop"]//a[@id="creturns-policy-anchor-text"]/i//..//text()').get()
                    if fre_re==None:
                        fre_re=response.xpath('//div[@class="olp-text-box"]//span[contains(text(),"FREE Scheduled Delivery")]//text()').get()
                        if fre_re==None:
                            final_promo="n/a"
                        else:
                            final_promo=fre_re
                            print(final_promo)
                    else:
                        final_promo=f'& {fre_re}'
                        print(final_promo)
                else:
                    fre_re = response.xpath('//div[@id="apex_desktop"]//a[@id="creturns-policy-anchor-text"]/i//..//text()').get()
                    pr1=promo[0]
                    pr2= promo[1]
                    pr3= promo[2]
                    pr4= promo[3]
                    final_promo = f'{pr1}{pr2}{pr3}{pr4} & {fre_re}'
                    print(final_promo)

                item['promo_message'] = c_replace(final_promo)

            except Exception as e:
                print(e)

            # TODO -------- Stock_Status -------------

            try:
                stock_st=response.xpath('//div[@class="a-section a-spacing-none a-padding-none"]//div[@id="availability"]//span//text()').get()
                if stock_st==None:
                    stock_st=response.xpath('//div[@id="availability_feature_div"]//div[@id="availability"]/span/text()').get()
                    if stock_st==None:
                        nw_stock_s="n/a"
                    else:
                        nw_stock_s=stock_st
                else:
                    nw_stock_s=stock_st

                item['Stock_Status'] = c_replace(nw_stock_s)
            except Exception as e:
                print(e)

            item['htmlpath'] = path
            item['Status']="Done"
            item['HtmlPath']=path
            # item['product_name']=nw_prd_nm
            # item['ProductID']=product_id
            # item['Ships_from']=nw_ship
            # item['Sold_by']=nw_sold_by
            # item['earliest_delivery_date']=mn_early
            # item['Fastest_delivery']=mn_fast
            item['extraction_date']=datetime.today().strftime('%d/%m/%Y %H:%M:%S %p')
            # item['promo_message']=final_promo
            # item['Stock_Status']=nw_stock_s
            # item['site_category_path']=nw_bread
            # item['Price']=nw_mrk_price

            yield item

        else:

            p_id = p_url.split('dp/')[1].split('#')[0]
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

            item=UgamAmazonZipcodeEgItem()
            item['ID']=row_id
            item['htmlpath'] = path
            item['extraction_date'] = datetime.today().strftime('%d/%m/%Y %H:%M:%S %p')
            item['product_name']="n/a"
            item['ProductID']="n/a"
            item['Ships_from']="n/a"
            item['Sold_by']="n/a"
            item['earliest_delivery_date']="n/a"
            item['Fastest_delivery']="n/a"
            item['extraction_date']=datetime.today().strftime('%d/%m/%Y %H:%M:%S %p')
            item['promo_message']=f"n/a"
            item['Stock_Status']="n/a"
            item['site_category_path']="n/a"
            item['Price']="n/a"
            item['Status']="Not Found"

            yield item

    # def close(spider, reason):
    #     try:
    #         con = UgamAmazonZipcodeEgPipeline.con
    #         import pandas as pd
    #         sql_query = pd.read_sql_query(
    #             f'SELECT `ID`,`product_name`,`postcode`,`ProductID`,`Product_URL`,`Ships_from`,`Sold_by`,`earliest_delivery_date`,`Fastest_delivery`,`extraction_date`,`promo_message`,`Stock_Status`,`site_category_path`,`Price` from {product_table} where Status="Done"',
    #             con)
    #         df = pd.DataFrame(sql_query)
    #         df.to_csv(f'Ugam_Amazon_US_8_ZIPCODE{today_date}.csv', encoding='utf-8-sig', index=False)
    #         print("---------------------**********************************-------------------------------")
    #         print("create File")
    #
    #     except Exception as e:
    #         print(e)

if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute('scrapy crawl AmazonGeoGE -a start=1 -a end=1'.split())