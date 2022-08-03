import random
import re

import scrapy
import requests
from scrapy.selector import Selector
import urllib.parse
import time
import json
from datetime import datetime
from amazon_us_keyword_pdp.items import *
from amazon_us_keyword_pdp.config import *
from amazon_us_keyword_pdp.pipelines import AmazonUsKeywordPdpPipeline
import base64
import math
import pymysql
import requests
import json
from mymodules_simple._common_ import c_replace
from scraper_api import ScraperAPIClient
from mymodules_html._common_ import c_replace as html_replace

client = ScraperAPIClient('30aa984ae6a94b0d8898f8e9393413c1')
crawlera_key = '66b18fe5e75149d8b42fa081d35da7da'
from random_user_agent.params import SoftwareName, OperatingSystem
from random_user_agent.user_agent import UserAgent
from random import choice

file_page_cookie_path = f'{os.getcwd()}\\login_cookie.txt'
b_file = open(file_page_cookie_path)
file_contents_core = b_file.read()
if file_contents_core.strip().endswith(';'):
    file_contents_core = file_contents_core.strip()[:-1]

proxy_host = "proxy.zyte.com"
proxy_port = "8011"
# proxy_auth = "6bb62d174feb4c10a6019897cae22244:"
proxy_auth = "295076252cfd4c6785db5845825ed279:"

# proxyle = {
#     "https": f"http://{proxy_auth}@{proxy_host}:{proxy_port}/",
#     "http": f"http://{proxy_auth}@{proxy_host}:{proxy_port}/"
# }
proxystorm={"https":"lum-customer-c_11e7173f-zone-zone_us:mqy4l03550gl@zproxy.lum-superproxy.io:22225",
"http":"lum-customer-c_11e7173f-zone-zone_us:mqy4l03550gl@zproxy.lum-superproxy.io:22225"}


# userid = 'storm4xbyte1'
# password = 'storm4xbyte1'
# host = '5.79.73.131'
# port = '13150'
#
# proxystorm = {
#             "https": f"http://{userid}:{password}@{host}:{port}/",
#             "http": f"http://{userid}:{password}@{host}:{port}/",
#             }

# proxystorm = {
#     "https": f"http://{proxy_auth}@{proxy_host}:{proxy_port}/",
#     "http": f"http://{proxy_auth}@{proxy_host}:{proxy_port}/"
# }

proxylumi=proxystorm




def get_useragent():
    l1 = [SoftwareName.CHROME.value, SoftwareName.FIREFOX.value, SoftwareName.OPERA.value]
    software_names = [choice(l1)]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value, OperatingSystem.SUNOS.value]
    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=1000)
    return user_agent_rotator.get_random_user_agent()

cookie_text=open(f'{os.getcwd()}\\login_cookie.txt').read().strip()



vheaders = {
    "cookie": f'{file_contents_core}',
    "user-agent": get_useragent(),
'X-Crawlera-Cookies' : "disable"}


def unknownrepl(s):
    s = c_replace(s)
    a = s.encode('unicode_escape').decode('ascii')
    r = r'\\u[\w]{4}'
    c = c_replace(re.sub(r, '', a))
    c = c_replace(c)
    return c


class pandaSpider(scrapy.Spider):
    name = 'variation_pdp'
    handle_httpstatus_list = [404]

    F_PATH = asin_HTML

    def __init__(self, start='', end='', proxy_type=''):
        try:
            self.start = start
            self.end = end
            # self.proxy_type = proxy_type
            self.cursor = AmazonUsKeywordPdpPipeline.cursor
            self.con = AmazonUsKeywordPdpPipeline.con

        except Exception as e:
            logger.error('spider in __init__ method error :{}'.format(e))
            print('__init__ error:', e)

    def start_requests(self):
        try:

            sql = f"""select `id`,`ASIN`,`url` from {pdp_asin_input} where Variation_status='Pending' AND ID BETWEEN {self.start} AND {self.end}"""
            print(sql)
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            urlpage = list(result)
            for i in urlpage:
                row_id = f'{i[0]}'
                asin = f'{i[1]}'
                url = f'{i[2]}'

                filename = f'/Product_{asin}.html'
                path = self.F_PATH + filename
                path = path.replace("\\", "/")

                headers = {
                    "cookie": f'{file_contents_core}',
                    "user-agent": get_useragent(),

                }

                delete_duplicate_row = f"delete from {variation_pdp_table} where ID1 = {row_id}"
                self.cursor.execute(delete_duplicate_row)
                self.con.commit()

                meta_dict = {'row_id': row_id, 'asin': asin, 'URL': url}
                if os.path.exists(path):
                    meta_dict['page_save'] = "no"
                    yield scrapy.Request(url=f'file:///{path}', callback=self.get_response,
                                         meta=meta_dict)
                else:
                    # if self.proxy_type=="Crawlera":
                    #     yield scrapy.Request(url=URL, callback=self.get_response,headers=headers,
                    #                          meta={'row_id': row_id, 'asin_link': asin_link, 'URL': URL,'ProductId':asin_link,'proxy_type':"Crawlera",
                    #                                })
                    # else:
                    meta_dict['page_save'] = "Yes"
                    yield scrapy.Request(url, callback=self.get_response, headers=headers,
                                         meta=meta_dict)

        except Exception as e:
            logger.error('exception in start requests method main: {}'.format(e))

    def get_response(self, response):

        product_id = str(response.meta.get('ProductId'))
        # product_id = "Product_trial"
        url = response.meta.get('URL')
        cat_name = response.meta.get('Category')
        sub_cat_name = response.meta.get('Sub_Category')
        row_id = response.meta.get('row_id')

        checkreload = response.xpath('//div[contains(text(),"Please reload this page")]')
        print(checkreload)

        if "/errors/validateCaptcha" not in response.text and not checkreload and 'nav-logo-sprites' in response.text and 'Hello, Herrisan' in response.text:
            checksclass = response.xpath('//span[@id="productTitle"]')
            if checksclass:
                try:

                    product_id = str(response.meta.get('asin'))
                    # product_id = "Product_trial"
                    url = response.meta.get('URL')
                    cat_name = response.meta.get('Category')
                    sub_cat_name = response.meta.get('Sub_Category')
                    row_id = response.meta.get('row_id')

                    filename = f'/Product_{product_id}.html'
                    path = self.F_PATH + filename
                    path = path.replace("\\", "/")
                    if not os.path.exists(path):
                        with open(path, "w", encoding="utf-8")as f:
                            f.write(response.text)


                    canonical_url = response.xpath('//link[@rel="canonical"]//@href').get()
                    if canonical_url:
                         pass
                    else:
                        return None
                    # Asin1=response.xpath('//th[contains(text(),"ASIN")]//following-sibling::td//text()').get()
                    # if not Asin1:
                    #     Asin1=response.xpath('//span[contains(text(),"ASIN")]//following-sibling::span//text()').get()
                    #     if not Asin1:
                    #         Asin1=''.join(re.findall('var asin = "(.*?)";', response.text))
                    #         if not Asin1:
                    #             Asin1=c_replace(''.join(re.findall('/dp/(.*?)/',url)))
                    #             if not Asin1:
                    #                 Asin1 = c_replace(''.join(re.findall('/dp/(.*?)\?', url)))
                    #
                    # print(unknownrepl(Asin1))


                    html_text = response.xpath('//div[@id="twister-plus-inline-twister"]').get()


                    try:
                        # forvariationmatch1 = re.findall('asinVariationValues\"\s\:\s(.*?),\\n', response.text)
                        # if not forvariationmatch1:
                        #     forvariationmatch1 = re.findall('asinVariationValues\"\s\:\s(.*?),\\r', response.text)
                        #     if not forvariationmatch1:
                        #         forvariationmatch1 = re.findall('asinVariationValues\"\s\:\s(.*?)\,\"dimensio',
                        #                                         c_replace(response.text))
                        # forvariationmatch1 = "".join(forvariationmatch1)
                        # if forvariationmatch1:
                        #     for_variation_json = json.loads(forvariationmatch1)
                        #     variant_bnch_dict = re.findall('variationValues\"\s\:\s(.*?),\\n', response.text)
                        #     if not variant_bnch_dict:
                        #         variant_bnch_dict = re.findall('variationValues\"\s\:\s(.*?),\\r', response.text)
                        #
                        #     variant_bnch_dict = "".join(variant_bnch_dict)
                        #
                        #     variantname = ""
                        #     # globals()['vvaluelist' + f'{variantname}'] = []
                        #     type_of_var = json.loads(variant_bnch_dict)
                        #     # for k, v, in variantjsonvalue.items():
                        #     #     variantname=k
                        #     #     globals()['vvaluelist' + f'{variantname}']=v
                        #     #     print(globals()['vvaluelist' + f'{variantname}'])
                        #     variationlist = []
                        #     # getvarvalue=""
                        #     variant_name_global = []
                        #     new_variant_json = dict()
                        #     for key, value in for_variation_json.items():
                        #         v_type_name_list = value.keys()
                        #         type_of_key_name = type_of_var.keys()
                        #         for v_name in type_of_key_name:
                        #             variant_name_global.append(v_name)
                        #             # print(type_of_var[v_name][value[v_name)]])
                        #             for_variation_json[key][v_name] = type_of_var[v_name][int(value[v_name])]
                        #         variationlist.append(value)
                        #
                        #         ...
                        #         # getvarvalue = ""
                        #         # getvarvalue = value[f'{variantname}']
                        #         # value[f'{variantname}'] = vvaluelist[int(getvarvalue)]
                        #         # varianlist.append(value)
                        # else:
                        variationlist=[]

                        if not variationlist:
                            try:
                                new_text=c_replace(response.text)
                                variationlist=re.findall('\"dimensionToAsinMap\"\s\:\s(.*?)\},',new_text)[0]
                                variationlist=f'{variationlist}'+'}'
                                variationlist=json.loads(variationlist)
                            except:
                                print("variation not found")
                        if variationlist:

                            for vk,vs in variationlist.items():
                                variant_detail_item = Variant_detail()
                                variant_detail_item['Master ASIN'] = product_id
                                variant_detail_item['html_text'] = html_text


                                variant_detail_item['HtmlPath'] = path
                                variant_detail_item['created_time'] = datetime.today().strftime('%d/%m/%Y %H:%M:%S %p')



                                v_asin = vs
                                if 'color' in str(vs):
                                    print("color in variation")
                                    return None
                                
                                if len(variationlist)==1 and v_asin!=product_id:
                                    v_asin=product_id

                                if v_asin == product_id:
                                    v_asin_seller = response.xpath('//div[@tabular-attribute-name="Sold by"]//a[@id="sellerProfileTriggerId"]//text()').get()
                                    if not v_asin_seller:
                                        v_asin_seller = response.xpath('//div[@tabular-attribute-name="Sold by"]//following-sibling::div[@tabular-attribute-name="Sold by"]//span//text()').get()
                                    if v_asin_seller:
                                        variant_detail_item['Variant ASIN Seller'] = c_replace(v_asin_seller.replace('Auto-deliveries sold BY','').replace('AND Fulfilled BY Amazon',''))
                                    else:
                                        variant_detail_item['Variant ASIN Seller'] = "NA"

                                    sellprice = response.xpath('//span[contains(@class,"apexPriceToPay")]//span[@class="a-offscreen"]//text()').get()
                                    if not sellprice:
                                        sellprice = response.xpath('//span[contains(@class,"priceToPay")]//span[@class="a-offscreen"]//text()').get()
                                    if sellprice:
                                        variant_detail_item['Selling Price (Variant ASIN)'] = c_replace(sellprice)
                                    else:
                                        variant_detail_item['Selling Price (Variant ASIN)'] = "NA"

                                    price_per_count = response.xpath('//td[contains(text(),"Price:")]//following-sibling::td//span[@class="a-price a-text-price a-size-small"]//text()').get()
                                    if not price_per_count:
                                        price_per_count = response.xpath('//span[contains(@class,"pricePerUnit")]//span[@class="a-offscreen"]//text()').get()

                                    if price_per_count:
                                        variant_detail_item['price per unit  (Variant ASIN)'] = c_replace(price_per_count).replace('$','')
                                        priceunit_price = response.xpath('//td[contains(text(),"Price:")]//following-sibling::td//span[@class="a-price a-text-price a-size-small"]//following-sibling::text()').get()
                                        if not priceunit_price:
                                            priceunit_price = response.xpath('//span[@class="a-price a-text-price"]//following-sibling::text()').get()
                                        variant_detail_item['per unit type (Variant ASIN)'] = c_replace(priceunit_price.replace('/', '').replace(')', ''))
                                    else:
                                        variant_detail_item['price per unit  (Variant ASIN)'] = "NA"
                                        variant_detail_item['per unit type (Variant ASIN)'] = "NA"

                                    style_name = response.xpath('//div[@id="variation_style_name"]//label[contains(text(),"Style:")]//following-sibling::span//text()').get()
                                    if not style_name:
                                        style_name = response.xpath('//div[@id="inline-twister-singleton-header-style_name"]//span[contains(text(),"Style")]//following-sibling::span//text()').get()
                                        if not style_name:
                                            style_name = response.xpath('//div[@id="inline-twister-dim-title-style_name"]//span[contains(text(),"Style")]//following-sibling::span//text()').get()

                                    flavour_name = response.xpath('//div[@id="variation_flavor_name"]//label[contains(text(),"Flavor Name:")]//following-sibling::span//text()').get()
                                    if not flavour_name:
                                        flavour_name = response.xpath('//div[@id="inline-twister-dim-title-flavor_name"]//span[contains(text(),"Flavor Name")]//following-sibling::span//text()').get()


                                    if style_name:
                                        variant_detail_item['Style/Flavour (Variant ASIN)'] = c_replace(style_name)
                                    elif flavour_name:
                                        variant_detail_item['Style/Flavour (Variant ASIN)'] = c_replace(flavour_name)
                                    else:
                                        variant_detail_item['Style/Flavour (Variant ASIN)'] = "NA"

                                    size_variant = response.xpath('//div[@id="variation_size_name"]//label[contains(text(),"Size:")]//following-sibling::span//text()').get()
                                    if not size_variant:
                                        size_variant = response.xpath('//div[@id="inline-twister-expander-header-size_name"]//span[contains(text(),"Size:")]//following-sibling::span//text()').get()
                                    size_variant2 = response.xpath('//div[@id="variation_size_name"]//label[contains(text(),"Size:")]//parent::div//following::span[@id="dropdown_selected_size_name"]//span[@class="a-dropdown-prompt"]//text()').get()
                                    if size_variant:
                                        variant_detail_item['Size (Variant ASIN)'] = c_replace(size_variant)
                                    elif size_variant2:
                                        variant_detail_item['Size (Variant ASIN)'] = c_replace(size_variant2)
                                    else:
                                        variant_detail_item['Size (Variant ASIN)'] = "NA"

                                    color_variant = response.xpath('//div[@id="variation_color_name"]//label[contains(text(),"Color:")]//parent::div//following::span[@id="dropdown_selected_color_name"]//span[@class="a-dropdown-prompt"]//text()').get()
                                    if color_variant:
                                        variant_detail_item['Color (Variant ASIN)'] = c_replace(color_variant)
                                    else:
                                        variant_detail_item['Color (Variant ASIN)'] = "NA"

                                    variant_detail_item['Variant ASIN'] = v_asin
                                    variant_detail_item['id1'] = row_id
                                    variant_detail_item['parent'] = "Yes"

                                    if variant_detail_item['Variant ASIN Seller'] == "NA":
                                        sold_by_new = response.xpath('//div[@data-feature-name="shipsFromSoldByMessage"]//span//text()').get()
                                        if sold_by_new:
                                            variant_detail_item['Variant ASIN Seller'] = c_replace(sold_by_new.replace('Ships from and sold by', ''))
                                        else:
                                            pass


                                    yield variant_detail_item

                                else:
                                    # for insert parent no
                                    v_filename = f'/VProduct_{v_asin}.html'
                                    v_path = self.F_PATH + v_filename
                                    if os.path.exists(v_path):
                                        v_response = Selector(text=open(v_path,'r',encoding='utf-8').read())
                                    else:
                                        # v_res = requests.get(url=f'https://www.amazon.com/dp/{v_asin}?th=1&psc=1', headers=vheaders,proxies=proxyle,verify=False)
                                        random_no=[1,2]
                                        v_res_status=True
                                        while v_res_status:
                                            random_id=random.choice(random_no)
                                            if random_id==1:
                                                print("try with storm or crwalera--")
                                                v_res = requests.get(url=f'https://www.amazon.com/dp/{v_asin}?th=1&psc=1',
                                                                     headers=vheaders, proxies=proxystorm, verify=False)
                                            elif random_id==2:
                                                print("try with lumi----")
                                                v_res = requests.get(url=f'https://www.amazon.com/dp/{v_asin}?th=1&psc=1',headers=vheaders, proxies=proxylumi, verify=False)
                                            else:
                                                return None
                                            # elif random_id=3:
                                            #     v_res = requests.get(url=f'https://www.amazon.com/dp/{v_asin}?th=1&psc=1',headers=vheaders, proxies=proxylumi, verify=False)
                                            if v_res.status_code == 200:
                                                v_response = Selector(text=v_res.text)
                                                if "/errors/validateCaptcha" not in v_res.text and not checkreload and 'nav-logo-sprites' in v_res.text and '07054' in v_res.text and 'Hello, Herrisan' in v_res.text:
                                                    open(v_path, 'w', encoding='utf-8').write(v_res.text)
                                                    v_res_status=False
                                                else:
                                                    print("wrong variant_response",v_res.text)
                                                    v_res_status = True
                                                    # return None
                                            else:
                                                print("wrong variant_response")
                                                v_res_status = True

                                    if v_response:

                                        v_asin_seller = v_response.xpath('//div[@tabular-attribute-name="Sold by"]//a[@id="sellerProfileTriggerId"]//text()').get()
                                        if not v_asin_seller:
                                            v_asin_seller = v_response.xpath('//div[@tabular-attribute-name="Sold by"]//following-sibling::div[@tabular-attribute-name="Sold by"]//span//text()').get()
                                        if v_asin_seller:
                                            variant_detail_item['Variant ASIN Seller'] = c_replace(v_asin_seller.replace('Auto-deliveries sold by','').replace('and Fulfilled by Amazon',''))
                                        else:
                                            variant_detail_item['Variant ASIN Seller'] = "NA"

                                        if variant_detail_item['Variant ASIN Seller'] == "NA":
                                            sold_by_new = v_response.xpath('//div[@data-feature-name="shipsFromSoldByMessage"]//span//text()').get()
                                            if sold_by_new:
                                                variant_detail_item['Variant ASIN Seller'] = c_replace(sold_by_new.replace('Ships from and sold by', '').replace('Auto-deliveries sold by','').replace('and Fulfilled by Amazon',''))
                                            else:
                                                pass

                                        sellprice = v_response.xpath('//span[contains(@class,"apexPriceToPay")]//span[@class="a-offscreen"]//text()').get()
                                        if not sellprice:
                                            sellprice = v_response.xpath('//span[contains(@class,"priceToPay")]//span[@class="a-offscreen"]//text()').get()
                                        if sellprice:
                                            variant_detail_item['Selling Price (Variant ASIN)'] = c_replace(sellprice)
                                        else:
                                            variant_detail_item['Selling Price (Variant ASIN)'] = "NA"

                                        price_per_count = v_response.xpath('//td[contains(text(),"Price:")]//following-sibling::td//span[@class="a-price a-text-price a-size-small"]//text()').get()
                                        if not price_per_count:
                                            price_per_count = response.xpath('//span[contains(@class,"pricePerUnit")]//span[@class="a-offscreen"]//text()').get()
                                        if price_per_count:
                                            variant_detail_item['price per unit  (Variant ASIN)'] = c_replace(price_per_count).replace('$', '')
                                            priceunit_price = v_response.xpath('//td[contains(text(),"Price:")]//following-sibling::td//span[@class="a-price a-text-price a-size-small"]//following-sibling::text()').get()
                                            if not priceunit_price:
                                                priceunit_price = response.xpath('//span[@class="a-price a-text-price"]//following-sibling::text()').get()
                                            variant_detail_item['per unit type (Variant ASIN)'] = c_replace(priceunit_price.replace('/', '').replace(')', ''))
                                        else:
                                            variant_detail_item['price per unit  (Variant ASIN)'] = "NA"
                                            variant_detail_item['per unit type (Variant ASIN)'] = "NA"

                                        style_name = v_response.xpath('//div[@id="variation_style_name"]//label[contains(text(),"Style:")]//following-sibling::span//text()').get()
                                        if not style_name:
                                            style_name = v_response.xpath('//div[@id="inline-twister-singleton-header-style_name"]//span[contains(text(),"Style")]//following-sibling::span//text()').get()
                                            if not style_name:
                                                style_name = v_response.xpath('//div[@id="inline-twister-dim-title-style_name"]//span[contains(text(),"Style")]//following-sibling::span//text()').get()

                                        flavour_name = v_response.xpath('//div[@id="variation_flavor_name"]//label[contains(text(),"Flavor Name:")]//following-sibling::span//text()').get()
                                        if not flavour_name:
                                            flavour_name = v_response.xpath('//div[@id="inline-twister-dim-title-flavor_name"]//span[contains(text(),"Flavor Name")]//following-sibling::span//text()').get()
                                        if style_name:
                                            variant_detail_item['Style/Flavour (Variant ASIN)'] = c_replace(style_name)
                                        elif flavour_name:
                                            variant_detail_item['Style/Flavour (Variant ASIN)'] = c_replace(flavour_name)
                                        else:
                                            variant_detail_item['Style/Flavour (Variant ASIN)'] = "NA"

                                        size_variant = v_response.xpath('//div[@id="variation_size_name"]//label[contains(text(),"Size:")]//following-sibling::span//text()').get()
                                        if not size_variant:
                                            size_variant = v_response.xpath('//div[@id="inline-twister-expander-header-size_name"]//span[contains(text(),"Size:")]//following-sibling::span//text()').get()
                                        size_variant2 = v_response.xpath('//div[@id="variation_size_name"]//label[contains(text(),"Size:")]//parent::div//following::span[@id="dropdown_selected_size_name"]//span[@class="a-dropdown-prompt"]//text()').get()
                                        if size_variant:
                                            variant_detail_item['Size (Variant ASIN)'] = c_replace(size_variant)
                                        elif size_variant2:
                                            variant_detail_item['Size (Variant ASIN)'] = c_replace(size_variant2)
                                        else:
                                            variant_detail_item['Size (Variant ASIN)'] = "NA"

                                        color_variant = v_response.xpath('//div[@id="variation_color_name"]//label[contains(text(),"Color:")]//parent::div//following::span[@id="dropdown_selected_color_name"]//span[@class="a-dropdown-prompt"]//text()').get()
                                        if color_variant:
                                            variant_detail_item['Color (Variant ASIN)'] = c_replace(color_variant)
                                        else:
                                            variant_detail_item['Color (Variant ASIN)'] = "NA"

                                        variant_detail_item['Variant ASIN'] = v_asin
                                        variant_detail_item['id1'] = row_id
                                        variant_detail_item['parent'] = "No"
                                        yield variant_detail_item


                                    else:
                                        print("response issue")
                                        return None
                            branch_sql = f'update {pdp_asin_input} set variation_Status = "Done" where id ="{row_id}"'
                            print(branch_sql)
                            self.cursor.execute(branch_sql)
                            self.con.commit()
                        else:
                            variant_detail_item = Variant_detail()
                            variant_detail_item['Master ASIN'] = product_id
                            variant_detail_item['html_text'] = "NA"

                            variant_detail_item['HtmlPath'] = path
                            variant_detail_item['created_time'] = datetime.today().strftime('%d/%m/%Y %H:%M:%S %p')
                            v_asin_seller = response.xpath('//div[@tabular-attribute-name="Sold by"]//a[@id="sellerProfileTriggerId"]//text()').get()
                            if not v_asin_seller:
                                v_asin_seller = response.xpath('//div[@tabular-attribute-name="Sold by"]//following-sibling::div[@tabular-attribute-name="Sold by"]//span//text()').get()
                            if v_asin_seller:
                                variant_detail_item['Variant ASIN Seller'] = c_replace(
                                    v_asin_seller.replace('Auto-deliveries sold BY', '').replace(
                                        'AND Fulfilled BY Amazon', ''))
                            else:
                                variant_detail_item['Variant ASIN Seller'] = "NA"

                            sellprice = response.xpath(
                                '//span[contains(@class,"apexPriceToPay")]//span[@class="a-offscreen"]//text()').get()
                            if not sellprice:
                                sellprice = response.xpath(
                                    '//span[contains(@class,"priceToPay")]//span[@class="a-offscreen"]//text()').get()
                            if sellprice:
                                variant_detail_item['Selling Price (Variant ASIN)'] = c_replace(sellprice)
                            else:
                                variant_detail_item['Selling Price (Variant ASIN)'] = "NA"

                            price_per_count = response.xpath(
                                '//td[contains(text(),"Price:")]//following-sibling::td//span[@class="a-price a-text-price a-size-small"]//text()').get()
                            if not price_per_count:
                                price_per_count = response.xpath(
                                    '//span[contains(@class,"pricePerUnit")]//span[@class="a-offscreen"]//text()').get()

                            if price_per_count:
                                variant_detail_item['price per unit  (Variant ASIN)'] = c_replace(
                                    price_per_count).replace('$', '')
                                priceunit_price = response.xpath(
                                    '//td[contains(text(),"Price:")]//following-sibling::td//span[@class="a-price a-text-price a-size-small"]//following-sibling::text()').get()
                                if not priceunit_price:
                                    priceunit_price = response.xpath(
                                        '//span[@class="a-price a-text-price"]//following-sibling::text()').get()
                                variant_detail_item['per unit type (Variant ASIN)'] = c_replace(
                                    priceunit_price.replace('/', '').replace(')', ''))
                            else:
                                variant_detail_item['price per unit  (Variant ASIN)'] = "NA"
                                variant_detail_item['per unit type (Variant ASIN)'] = "NA"

                            style_name = response.xpath('//div[@id="variation_style_name"]//label[contains(text(),"Style:")]//following-sibling::span//text()').get()
                            if not style_name:
                                style_name = response.xpath('//div[@id="inline-twister-singleton-header-style_name"]//span[contains(text(),"Style")]//following-sibling::span//text()').get()
                                if not style_name:
                                    style_name = response.xpath('//div[@id="inline-twister-dim-title-style_name"]//span[contains(text(),"Style")]//following-sibling::span//text()').get()
                            flavour_name = response.xpath('//div[@id="variation_flavor_name"]//label[contains(text(),"Flavor Name:")]//following-sibling::span//text()').get()
                            if not flavour_name:
                                flavour_name = response.xpath('//div[@id="inline-twister-dim-title-flavor_name"]//span[contains(text(),"Flavor Name")]//following-sibling::span//text()').get()
                            if style_name:
                                variant_detail_item['Style/Flavour (Variant ASIN)'] = c_replace(style_name)
                            elif flavour_name:
                                variant_detail_item['Style/Flavour (Variant ASIN)'] = c_replace(flavour_name)
                            else:
                                variant_detail_item['Style/Flavour (Variant ASIN)'] = "NA"

                            size_variant = response.xpath('//div[@id="variation_size_name"]//label[contains(text(),"Size:")]//following-sibling::span//text()').get()
                            if not size_variant:
                                size_variant = response.xpath('//div[@id="inline-twister-expander-header-size_name"]//span[contains(text(),"Size:")]//following-sibling::span//text()').get()
                            size_variant2 = response.xpath(
                                '//div[@id="variation_size_name"]//label[contains(text(),"Size:")]//parent::div//following::span[@id="dropdown_selected_size_name"]//span[@class="a-dropdown-prompt"]//text()').get()
                            if size_variant:
                                variant_detail_item['Size (Variant ASIN)'] = c_replace(size_variant)
                            elif size_variant2:
                                variant_detail_item['Size (Variant ASIN)'] = c_replace(size_variant2)
                            else:
                                variant_detail_item['Size (Variant ASIN)'] = "NA"

                            color_variant = response.xpath(
                                '//div[@id="variation_color_name"]//label[contains(text(),"Color:")]//parent::div//following::span[@id="dropdown_selected_color_name"]//span[@class="a-dropdown-prompt"]//text()').get()
                            if color_variant:
                                variant_detail_item['Color (Variant ASIN)'] = c_replace(color_variant)
                            else:
                                variant_detail_item['Color (Variant ASIN)'] = "NA"

                            variant_detail_item['Variant ASIN'] = product_id
                            variant_detail_item['id1'] = row_id
                            variant_detail_item['parent'] = "Yes"

                            if variant_detail_item['Variant ASIN Seller'] == "NA":
                                sold_by_new = response.xpath(
                                    '//div[@data-feature-name="shipsFromSoldByMessage"]//span//text()').get()
                                if sold_by_new:
                                    variant_detail_item['Variant ASIN Seller'] = c_replace(
                                        sold_by_new.replace('Ships from and sold by', ''))
                                else:
                                    pass

                            yield variant_detail_item




                            print("there is no variation----------------")
                            branch_sql = f'update {pdp_asin_input} set variation_Status = "Not found" where id ="{row_id}"'
                            print(branch_sql)
                            self.cursor.execute(branch_sql)
                            self.con.commit()
                            return None


                    except Exception as e:
                        print("No variation Found")

                    # yield asin_detail_item






                except Exception as e:
                    logger.error('exception in get_response method main:{}'.format(e))
                    print('error url', response.meta.get('url'), e)
            else:
                print("please check htmls-------")
                return None

                item = AmazonUsKeywordPdpPipeline()
                filename = f'/Product_{product_id}.html'
                path = self.F_PATH + filename
                path = path.replace("\\", "/")

                with open(path, "w", encoding="utf-8")as f:
                    f.write(response.text)

                item['HtmlPath'] = path
                item['status'] = 'Not found'
                AmazonUsKeywordPdpPipeline.update_item(self, item, row_id)

        elif response.status == 404  or "Sorry! We couldn't find that page" in response.text:

            branch_sql = f'update {pdp_asin_input} set variation_Status = "Not found" where id ="{row_id}"'
            print(branch_sql)
            self.cursor.execute(branch_sql)
            self.con.commit()

            return None
            filename = f'/Product_{product_id}.html'
            print(filename)
            path = self.F_PATH + filename
            path = path.replace("\\", "/")

            with open(path, "w", encoding="utf-8")as f:
                f.write(response.text)

            asin_detail_item = Amazon_pdp_asin()

            asin_detail_item['HtmlPath'] = path
            asin_detail_item['created_time'] = datetime.today().strftime('%d/%m/%Y %H:%M:%S %p')

            asin_detail_item['Master ASIN'] = product_id
            asin_detail_item['ASIN Title'] = "NA"
            asin_detail_item['review_count'] = "NA"
            asin_detail_item['rating'] = "NA"
            asin_detail_item['QnA Count'] = "NA"
            asin_detail_item['List Price'] = "NA"
            asin_detail_item['Selling Price'] = "NA"
            asin_detail_item['price per unit'] = "NA"
            asin_detail_item['per unit type'] = "NA"
            asin_detail_item['SnS Price'] = "NA"
            asin_detail_item['Coupon'] = "NA"
            asin_detail_item['cart_quantity'] = "NA"
            asin_detail_item['Ships From'] = "NA"
            asin_detail_item['Sold by'] = "NA"
            asin_detail_item['brand'] = "NA"
            asin_detail_item['Manufacturer'] = "NA"
            asin_detail_item['Date First Available'] = "NA"
            asin_detail_item['Item Form'] = "NA"
            
            asin_detail_item['Other Sellers Count'] = "NA"
            asin_detail_item['primary image url'] = "NA"

            asin_detail_item['Availability'] = 'Not Listed'

            asin_detail_item['status'] = 'Not found'

            # product_id = str(response.meta.get('ProductId'))
            # item['ProductId']=product_id

            asin_detail_item['HtmlPath'] = path

            AmazonUsKeywordPdpPipeline.update_item(self, asin_detail_item, row_id)
            print("Not found response")
        else:
            print("Wrong response")


from scrapy.cmdline import execute

if __name__ == '__main__':
    execute('scrapy crawl variation_pdp -a start=15 -a end=15'.split())
# execute('scrapy crawl amzpdp -a start=6 -a end=100 -a proxy_type=scraper'.split())
#
