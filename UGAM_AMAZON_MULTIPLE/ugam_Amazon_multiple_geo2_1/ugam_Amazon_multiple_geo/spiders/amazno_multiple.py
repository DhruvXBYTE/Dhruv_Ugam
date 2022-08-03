import hashlib
import time
import html
import datetime
import os
import scrapy
from ugam_Amazon_multiple_geo.config import *
from ugam_Amazon_multiple_geo.pipelines import *
from ugam_Amazon_multiple_geo.items import *
from mymodules._common_ import c_replace
from scrapy.selector import Selector
import requests
import json
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from mymodules._common_ import c_replace
import re


def unknownrepl(s):
    s = c_replace(s)
    a = s.encode('unicode_escape').decode('ascii')
    r = r'\\u[\w]{4}'
    c = c_replace(re.sub(r, '', a))
    c = c_replace(c)
    return c

handle_httpstatus_list = [404,403]
class Amazon_Multiple_Geo(scrapy.Spider):

    name = 'AmazonMultiple1'
    handle_httpstatus_list = [404, 403]
    F_PATH = HTML

    def __init__(self, start='', end=''):

        try:
            self.cursor = UgamAmazonMultipleGeoPipeline.cursor
            self.con = UgamAmazonMultipleGeoPipeline.con
            self.start = start
            self.end = end
        except Exception as e:
            logger.error('exception in __init__ method main:{}'.format(e))


    def start_requests(self):
        try:
            self.cursor = UgamAmazonMultipleGeoPipeline.cursor
            self.con = UgamAmazonMultipleGeoPipeline.con

            postcode=f"select Id,url,zipcode_input from {product_table} where Status = 'Pending' AND Id BETWEEN {self.start} AND {self.end}"
            self.cursor.execute(postcode)
            pst = [column for column in self.cursor.fetchall()]
            for i in pst:
                row_id=i[0]
                url=i[1]
                zipcode=i[2]

                if "/product" in url:
                    p_id=url.split('product/')[1].split('/')[0]
                    if "?" in url:
                        p_id = p_id.split("?")
                        p_id = p_id[0]
                    else:
                        p_id = p_id
                else:
                    p_id = url.split('dp/')[1].split('/')[0]
                    if "?" in url:
                        p_id = p_id.split("?")
                        p_id = p_id[0]
                    else:
                        p_id = p_id

                filename = f'/{row_id}_{p_id}_{zipcode}.html'
                path = self.F_PATH + filename
                path = path.replace("\\", "/")

                if os.path.exists(path):
                    pass
                else:

                    dd = webdriver.ChromeOptions()
                    dd = webdriver.Chrome(ChromeDriverManager().install())
                    dd.get("https://www.amazon.com/")
                    dd.maximize_window()
                    time.sleep(3)
                    dd.find_element_by_xpath('//a[@id="nav-global-location-popover-link"]').click()
                    time.sleep(3)
                    dd.find_element_by_id('GLUXZipUpdateInput').send_keys(f'{zipcode}')
                    time.sleep(1)
                    dd.find_element_by_xpath('//span[@id="GLUXZipUpdate"]').click()
                    time.sleep(1)
                    dd.find_element_by_xpath('//div[@class="a-popover-wrapper"]//div[@class="a-popover-footer"]//span[@class="a-declarative"]').click()
                    # dd.find_element_by_xpath('//div[@class="a-popover-footer"]//span//input[@id="GLUXConfirmClose"]').click()
                    cookieimid = ""
                    d = dd.get_cookies()
                    for c in d:
                        cookieimid += '{name}={value}; '.format(
                            name=c['name'],
                            value=c['value']
                        )


                    headers = {
                        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        "cookie": f'{cookieimid}',
                        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
                        "sec-fetch-site": "same-origin",
                        "sec-ch-ua-platform": '"Windows"',
                        'scheme': 'https',
                    }
                    print(headers)

                    # p_id = url.split('dp/')[1].split('/')[0]
                    # if "?" in p_id:
                    #     p_id = p_id.split("?")
                    #     p_id = p_id[0]
                    # else:
                    #     p_id = p_id
                    #
                    # filename = f'/{row_id}_{p_id}_{zipcode}.html'
                    # path = self.F_PATH + filename
                    # path = path.replace("\\", "/")

                    re=requests.get(url=url,headers=headers)
                    if zipcode in re.text:
                        with open(path,'w',encoding='utf-8')as f:
                            f.write(re.text)
                    else:
                        print("-------ZIPCODE NOT IN PAGE-------")
                        with open(path,'w',encoding='utf-8')as f:
                            f.write(re.text)
                        print("-------ZIPCODE NOT IN PAGE-------")


                time.sleep(1)
                if os.path.exists(path):
                    yield scrapy.FormRequest(url=f'file:///{path}', callback=self.parse, dont_filter=True,
                                             meta={'row_id': row_id, 'p_url': url, 'zpcode': zipcode})
                # else:
                #     time.sleep(2)
                #     yield scrapy.FormRequest(url=url, callback=self.parse, headers=headers, dont_filter=True,
                #                              meta={'row_id': row_id, 'p_url': url, 'zpcode': zipcode})

        except Exception as e:
            print(e)

    def parse(self, response, **kwargs):

        row_id=response.meta.get('row_id')
        p_url=response.meta.get('p_url')
        zpcode=response.meta.get('zpcode')

        print(response.status)

        if "Sorry! We couldn't find that page. Try searching or go to Amazon's home page." not in response.text and "Amazon.com Page Not Found" not in response.text:

            if "/product" in p_url:
                p_id = p_url.split('product/')[1].split('/')[0]
                if "?" in p_url:
                    p_id = p_id.split("?")
                    p_id = p_id[0]
                else:
                    p_id = p_id
            else:
                p_id = p_url.split('dp/')[1].split('/')[0]
                if "?" in p_url:
                    p_id = p_id.split("?")
                    p_id = p_id[0]
                else:
                    p_id = p_id

            filename = f'/{row_id}_{p_id}_{zpcode}.html'
            path = self.F_PATH + filename
            path = path.replace("\\", "/")

            # if zpcode in response.text:
            #     if os.path.exists(path):
            #         pass
            #     else:
            #         time.sleep(2)
            #         with open(path, 'w', encoding='utf-8')as f:
            #             time.sleep(1)
            #             f.write(response.text)
            #
            # else:
            #     print("---- ZIPCODE NOT IN PAGE ------")

            # TODO -------  ITEMS CALL --------------

            item = UgamAmazonMultipleGeoItem()
            item['Id'] = row_id

            # TODO ----------- HEADERS SCRAPE------------------

            # Todo --------- Category_Path ---------------
            item['category_path']="n/a"

            # Todo --------- estimated_installation_features ---------------
            item['estimated_installation_features']="n/a"

            # Todo ---------- Product_Name ----------------
            try:
                p_name=response.xpath('//div[@id="vasTitle"]//h1//text()').get()
                item['product_name']=p_name

            except Exception as e:
                print(e)

            # Todo ----- Available_option --------
            item['available_options']="n/a"

            # Todo ------- Regular Price -------------

            item['regular_price']="n/a"

            # Todo -------- stock_status-----------
            try:
                s_stauts=response.xpath('//div[@class="displayForm"]//div//span//text()').getall()
                nw_status=''.join(s_stauts)
                print(nw_status)
                item['stock_status']=c_replace(nw_status)
            except Exception as e:
                print(e)

            # Todo ------Sku_Variant -----------
            try:
                sku_title=response.xpath('//div[@id="vasTwister2_feature_div"]//div[@class="a-section a-spacing-medium a-spacing-top-medium"]//span//text()').getall()
                sku_value=response.xpath('//ul[@class="a-unordered-list a-nostyle a-button-list a-declarative a-button-toggle-group a-horizontal a-spacing-medium a-spacing-top-micro"]//span[@class="a-button a-button-selected a-button-toggle"]//span//a//span//text()').getall()
                # sku_description=response.xpath('//div[@id="description-twister-wrapper"]//div[@id="vasDescription"]//div//span//text()').getall()

                spec = []
                keys = response.xpath('//div[@id="vasTwister2_feature_div"]//div[@class="a-section a-spacing-medium a-spacing-top-medium"]//span//text()').getall()
                if keys==[]:
                    sku_description = response.xpath('//div[@id="description-twister-wrapper"]//div[@id="vasDescription"]//div//span//text()').getall()
                    description=c_replace(sku_description)
                    specification = ' #||# '.join(description)
                    print(specification)
                    specification=specification
                else:
                    keys = response.xpath('//div[@id="vasTwister2_feature_div"]//div[@class="a-section a-spacing-medium a-spacing-top-medium"]//span//text()').getall()
                    values = response.xpath('//ul[@class="a-unordered-list a-nostyle a-button-list a-declarative a-button-toggle-group a-horizontal a-spacing-medium a-spacing-top-micro"]//span[@class="a-button a-button-selected a-button-toggle"]//span//a//span//text()').getall()
                    specification = ' #||# '.join([str(key).strip() +  " " + str(value).strip().replace('#','') for key, value in zip(keys, values)])
                    print("sp:", specification)

                item['sku_variant']=c_replace(specification)


            except Exception as e:
                print(e)

            # Todo ------Add To cart -----------
            item['add_to_cart']="n/a"


            # Todo ---- Image_url----------
            try:
                img_url=response.xpath('//div[@id="vasBleedImage_feature_div"]//script[@type="a-state"]//text()').get()
                ld_img_url=json.loads(img_url)
                print(ld_img_url)
                p_img=ld_img_url['vasBleedImageUrl']
                item['product_image']=p_img

            except Exception as e:
                print(e)

            # todo ------- PRODUCT ID ---------

            try:
                item['product_id'] = p_id
            except Exception as e:
                print(e)

            # todo ------- Feature ---------
            try:
                item['features']="n/a"

            except Exception as e:
                print(e)

            # Todo ------ Review Count ------------
            try:
                rv_ct=response.xpath('//div[@id="vasAsinStarRating"]//a[@class="a-link-normal"]//text()').get()
                review_cnt=re.findall(r"^\d*\d",rv_ct)[0]
                item['review_count']=review_cnt

            except Exception as e:
                print(e)

            # Todo ------ average_rating -----------
            try:
                avj_rt=response.xpath('//div[@id="vasAsinStarRating"]//i[@class="a-icon a-icon-star-medium a-star-medium-4-5"]//span//text()').get()
                if avj_rt==None:
                    nw_avj=response.xpath('//div[@id="vasAsinStarRating"]//i[@class="a-icon a-icon-star-medium a-star-medium-5"]//span//text()').get()
                    if nw_avj:
                        nw_rt=nw_avj.split(' ')[0]
                    else:
                        nw_rt="n/a"
                else:
                    nw_rt=avj_rt.split(' ')[0]
                print(nw_rt)

                item['average_rating']=nw_rt+" out of 5 Stars"
            except Exception as e:
                print(e)

            # Todo --------- Parent URL -----------
            try:
                parent_url=f"https://www.amazon.com/gp/delivery/ajax/address-change.html?ASIN={p_id}&zipcode={zpcode}"
                item['parent_url']=parent_url

            except Exception as e:
                print(e)

            # Todo ------- Market Number -------

            item['Market_Number']="n/a"

            # Todo ------ Market_Name ---------
            item['Market_Name']="n/a"

            # Todo ---------Store_Number -------
            item['Store_Number']="n/a"

            # Todo ---------- Status -----------
            item['Status']="Done"
            item['htmlpath']=path

            yield item

        else:

            if "/product" in p_url:
                p_id = p_url.split('product/')[1].split('/')[0]
                if "?" in p_url:
                    p_id = p_id.split("?")
                    p_id = p_id[0]
                else:
                    p_id = p_id
            else:
                p_id = p_url.split('dp/')[1].split('/')[0]
                if "?" in p_url:
                    p_id = p_id.split("?")
                    p_id = p_id[0]
                else:
                    p_id = p_id

            filename = f'/{row_id}_{p_id}_{zpcode}.html'
            path = self.F_PATH + filename
            path = path.replace("\\", "/")

            item = UgamAmazonMultipleGeoItem()
            item['Id'] = row_id
            item['htmlpath']=path
            item['category_path'] = "n/a"
            item['estimated_installation_features'] = "n/a"
            item['product_name'] = "n/a"
            item['available_options'] = "n/a"
            item['cookie']="n/a"
            item['regular_price'] = "n/a"
            item['stock_status']="n/a"
            item['sku_variant']="n/a"
            item['review_count']="n/a"
            item['average_rating']="n/a"
            item['add_to_cart'] = "n/a"
            item['product_image']="n/a"
            item['product_id'] = "n/a"
            item['features'] = "n/a"
            item['parent_url'] = "n/a"
            item['Market_Number'] = "n/a"
            item['Market_Name'] = "n/a"
            item['Store_Number'] = "n/a"
            item['Status'] = "Not Found"

            yield item

if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute('scrapy crawl AmazonMultiple1 -a start=1 -a end=1'.split())


