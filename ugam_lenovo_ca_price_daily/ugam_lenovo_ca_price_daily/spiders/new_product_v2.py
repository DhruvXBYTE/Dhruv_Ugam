# -*- coding: utf-8 -*-
import hashlib
import json
import subprocess

import pymysql
import scrapy
from mymodules._common_ import c_replace
import re
import json
from scrapy import Selector
from pymysql import OperationalError

from ugam_lenovo_ca_price_daily.items import UgamLenovoCaPriceDailyItem
from ugam_lenovo_ca_price_daily.pipelines import UgamLenovoCaPriceDailyPipeline
from ugam_lenovo_ca_price_daily.config import *
import time
import requests

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'cookie': 's_ecid=MCMID%7C15898899919205004223810527332888129364; aam_uuid=16048364323353588723797762463263119882; BVBRANDID=ea939c34-7761-41c4-a3f5-799ef3133ca0; split10=control; split=control; MSART_inen=PC%20%26%20TABLETS%7C%2Fin%2Fen%2Fpc; _fbp=fb.1.1626500304186.51578466; _mkto_trk=id:026-ENO-001&token:_mch-lenovo.com-1626500305347-83106; _gcl_au=1.1.1544956528.1626500306; QuantumMetricUserID=9bbc39a63e7bb533117aa506897589d4; _uetvid=34d06ca0e6c111eb8ec817c8f6d7cedf; _ga_EYNZYSHSG4=GS1.1.1626502831.2.1.1626504272.59; MSART_auen=PC%20%26%20TABLETS%7C%2Fau%2Fen%2Fpc; _caid=58d312ae-9b15-4e06-8a9c-d911669e39d3; _ga=GA1.2.1915923925.1626500306; _gid=GA1.2.870382769.1627560453; ki_r=; sn.vi=6b2ab0d3-0c13-45f2-8c85-ec3470f54875; sn.tpc=1; LOSAD=1; p3094257258_done=1; cto_bundle=KY0VYl9odElETWpxQmNDOGRpOTZSSFBwalliJTJCcjJzT3l5c25UcDFjekE5bHdDd0FrTDYzM0N5UUdXeEIwVSUyQjZBSWQlMkJVOTRJUk5wUjN4blRiaHdGcUYlMkJSTzklMkJQYkJMQm8lMkZ5N0tzbVBOTGZHVW9FTXZESWJVaDRhJTJCQnIza1NQWkJNVUczc09XJTJCQmMzdE53TXBqMGRqWlVpbExRJTNEJTNE; LSESSION=CC8D5525-9A43-44CF-8C0C-22E30002FDF4; at_check=true; AMCVS_F6171253512D2B8C0A490D45%40AdobeOrg=1; s_eng_rfd=0.00; s_cc=true; ki_t=1627560453132%3B1627618041581%3B1627618041581%3B2%3B16; inside-au=939712676-9dfefa9c79e9da14e01b630d5f4e35e654337fdeb1a1414be2c60cbae93854ae-0-0; _abck=F8FAB10D4992DFC7E46A7EFAD060EC8E~0~YAAQp13SF+X+P516AQAA/Hp99gZY1LqmDE2Pu2dUik7X2V8+kum1aNpKN3bol6qWSD0IMrJXpelS8cibP+AM8FGlee3VB2zJV5owF1qOrfzW1VBXZ8LeRxWZQX6C5FlfBazmNDQC9N3SGLfW1AuGlFLbscXft5xuf/UYirCvxqTm67Vh/0nB3YmZg3zZathX6IwG0p2z9gD20BbFur85/0pKKLwnogybeeL8h80vSQkdnfqchQ2csvWLpxo/0MsEQf3h0ZChZC6HFtCni1zsRTfBvQRcQ2auqt0FXCSjyRUUawj9J9F6vD4u6febRIqLFx6Q+M5BtxZbVSbmzMOmamdp1I0Xj4tuZw6SnjGx0zCb4tiDhIVrDMa4016jtfM90ZN9uzc6YAlr8aJ4LrNU4IxzMKp9lacY~-1~-1~-1; bm_sz=2F7D04E875DCADEE633F1018AC2AAB1F~YAAQp13SF+f+P516AQAA/Hp99gwFOxhW6OB+Qs+ACwv3Rv0I5LeHH9kS21ePhEtH/ofyCGpEvbrFTW/A4ty6JEWaPXYn38SNVma7WWdovS+AZALJSMVJgUIfyRF/ObWpclO9atbGzRhpuBFavmjZcLfszQ/QhlgJuGD7gc4AuQs9S4et2nPoi0L2Fy6zmRxWlXoPxXKVyE0vxauUcR9bA28QdMJq6jj7cSyGGvdJR7AShi7HUgZXyuZau2F63O9z4vTF4pqX9mvc6vQIX7FaDNAdgAowJF8piC0k7+9bvjj5xnU=~3749176~4339763; s_dfa=lenovomypub%2Clenovoglobal; s_inv=14963; s_ivc=true; s_vnc365=1659169000085%26vn%3D5; s_dur=1627633000087; AMCV_F6171253512D2B8C0A490D45%40AdobeOrg=-1124106680%7CMCIDTS%7C18838%7CMCMID%7C15898899919205004223810527332888129364%7CMCAAMLH-1628237800%7C12%7CMCAAMB-1628237800%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1627640200s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.2.0; ak_bmsc=B0428A59C349429AE2094075F52DEB0D~000000000000000000000000000000~YAAQp13SFwP/P516AQAAUIR99gzu/Ms57NbQyx+Isr3ypwPxVRRwGHM4npKf1gf6xGXPQo0wRHgYo+9jk0fOKKypNUaPVzdAaWFSYjfoPk7JEIbQuq0nijAb/Q8Jn64Qp3WPwYuvAM68GTtRa/eYFtHzk+ceYriFRPjIrAJf8BR73SPzM/66i0XLRKiqaSURWvpficMN5Dxe+aU65KiaH3h++W7YffcRLEinCWKfd8UKTNHLkjeYMyW+2sOG3dJabUckgyE2JmVZrmNMTqyZai5H7U72dxI353I0XLkZtwJ3L1vAEGISb7fouY3aAtR6pWYpTe5A/SrqcKlZZSdpxHZ+Bu0LjJp7zh07hw9s2GBSpnAYSDOtZLnJ03sXgiAQ4StIIlxhPc3RbkmLlNgnlrduCIwtPr+iWY7ApU3++qqb/2FSch/6Fg9gZRWtjLZbfQPx5KWpp8+RC/zMBTVCIwGWwNZuTwiylbIjgsI2pqOXoltIbkUsuscrThI=; BVBRANDSID=edc9a981-fd47-4421-ad71-e8d72b3893d8; MSART=PC%20%26%20Tablets%7C%2Fmy%2Fen%2Fpc; MSART_myen=PC%20%26%20Tablets%7C%2Fmy%2Fen%2Fpc; QuantumMetricSessionID=1b1946714d40353984ec5011be18fa30; AKA_A2=A; MSESSIONID=C1C1FDC4AEC50CA24836AA6CA0DC630D; JSESSIONID=17E397382F784EE637133F19A6044122.app6; s_eVar57=%3B82C10000MA; s_gpv=my_en%3Alaptops%3Alenovo%3Astudent-chromebooks%3Aideapad-3-cb-14igl05%3Ap%3A82c10000ma; s_sq=%5B%5BB%5D%5D; aam_sc=aamsc%3D11169887; s_tot_rfd=1.72; s_tslv=1627633355398; akavpau_WaitingRoomController=1627633713~id=2b7a5ab32cb542ad13057eb40051ae9f; bm_sv=15AD5B64C1BE28AECE821F603A261FDA~vnr/M/52AibNbA/HskXL7u4/XOnsDLI+eqE8XJ0A4xlRJpZx2RJBFKlU5M50egt8Sj8vU9SlZYaHJtKbbdw0935ALnYr+4aru/3Eo65sQWDawL35Yj1I3nMzvLQyWYz8GGpKEZ1kSz3VmubfNTqRdrSEb6KIGpkzG+Gp6yUGjGA=; aamtest1=seg%3Dabc%2Cseg%3Ddef%2Cseg%3Dghi; s_tp=7081; s_ppv=my_en%253Alaptops%253Alenovo%253Astudent-chromebooks%253Aideapad-3-cb-14igl05%253Ap%253A82c10000ma%2C3%2C3%2C184; utag_main=v_id:017ab2f9099600100d19f5abb3ed03073006d06b009dc$_sn:5$_se:6$_ss:0$_st:1627635157024$dc_visit:5$ses_id:1627633001802%3Bexp-session$_pn:6%3Bexp-session$criteo_sync:1%3Bexp-session$dc_event:6%3Bexp-session$dc_region:ap-east-1%3Bexp-session; inside-asia=584642970-fc40efe0ce27f17dfc361ff167ef4125a635cbaf37cbd8ee8647edcbd1b3523b-0-0; mbox=PC#7305ccfb39174bc6a179f89a388e80b6.38_0#1690877867|session#89c0e51c3a8e404a83472eeb2e20b90c#1627635219; RT="z=1&dm=lenovo.com&si=df4569b1-1e78-46f3-8cd2-67af4bff7039&ss=krq2nv4q&sl=5&tt=5pc&bcn=%2F%2F6852bd0a.akstat.io%2F&ld=7omz&ul=7tuv"',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}


class ProductSpider(scrapy.Spider):
    handle_httpstatus_list = [404]

    name = 'lenovo_ca_product'

    F_PATH = HTML

    def __init__(self, start='', end=''):
        try:
            self.start = start
            self.end = end
        except Exception as e:
            logger.error('spider in __init__ method error :{}'.format(e))
            print('__init__ error:', e)

    def start_requests(self):
        try:
            self.cursor = UgamLenovoCaPriceDailyPipeline.cursor
            self.con = UgamLenovoCaPriceDailyPipeline.con

            sql_query = f"select `id`,`product_id`,`product_url` from {db_data_table} where Status = 'Pending' AND ID BETWEEN {self.start} AND {self.end}"
            # sql_query = f"select `id`,`Product ID`,`Product URL` from {db_data_table} where Status = 'Pending' and id between 1 and 100"
            self.cursor.execute(sql_query)

            core_list = [column for column in self.cursor.fetchall()]

            for itm in core_list:
                try:
                    # time.sleep(1)
                    row_id = itm[0]
                    Product_ID = itm[1]
                    Product_URL = itm[2]

                    meta_dict = {'row_id': row_id,
                                 'Product_ID': Product_ID,
                                 'Product_URL': Product_URL
                                 }

                    filename = f'/{Product_ID}.html'
                    path = self.F_PATH + filename
                    print(path)

                    if os.path.exists(path):
                        yield scrapy.FormRequest(url=f'file:///{path}', callback=self.parse, headers=headers,
                                                 dont_filter=True,
                                                 meta={"meta_dict": meta_dict})
                    else:
                        yield scrapy.FormRequest(url=Product_URL, callback=self.parse, headers=headers,
                                                 dont_filter=True,
                                                 meta={"meta_dict": meta_dict})
                except Exception as e:
                    logger.error('start requests method error in sku for loop: {}'.format(e))
        except Exception as e:
            logger.error('start requests method error in main: {}'.format(e))

    def parse(self, response):
        try:
            if "</html>" in str(response.body) and 'lenovo logo' in response.text:
                print("||----------------------------------------------------------------------------------------||")
                catpdp.intialize_variable()

                meta_dict = response.meta.get('meta_dict')
                row_id = meta_dict.get('row_id')
                product_url = meta_dict.get('Product_URL')
                Product_ID = meta_dict.get('Product_ID')
                catpdp.product_url = product_url.replace("\'", "\'\'")
                catpdp.ugam_id = str(row_id)
                """ Product ID """
                catpdp.product_id = c_replace(Product_ID)

                filename = f'/{Product_ID}.html'
                path = self.F_PATH + filename
                path = path.replace("\\", "/")
                if os.path.exists(path):
                    pass
                else:
                    with open(path, 'wb') as f:
                        f.write(response.body)

                """ HtmlPath """
                catpdp.htmlpath = path

                """ Date of Crawl """
                # catpdp.Date_space_of_space_Crawl = datetime.today().strftime('%m/%d/%Y %H:%M:%S')

                """ Retailer """
                catpdp.site_name = "Lenovo.CA"

                catpdp.msrp = 'n/a'

                if response.xpath('//h2[@class="product_summary"]//text()').get():

                    """ Product Title """
                    try:

                        product_title = response.xpath('//h2[@class="product_summary"]//text()').get()
                        if product_title:
                            catpdp.product_name = c_replace(product_title)
                        else:
                            catpdp.product_name = 'n/a'
                    except Exception as e:
                        logger.info("Error in scrape header Product Title : {}".format(e))
                        return None

                    if response.xpath('//meta[@name="description"]/@content'):
                        meta_description = response.xpath('//meta[@name="description"]/@content').get()
                        meta_description = c_replace(meta_description).replace('"','')
                    else:
                        meta_description = 'n/a'

                    catpdp.meta_description = "n/a"

                    catpdp.meta_title = 'n/a'

                    """ MPN """
                    try:
                        mpn = response.xpath('''//div[@class="part-number"]//span[@class="value"]//text()''').get()
                        if mpn:
                            MPN = c_replace(mpn)
                            catpdp.mpn = c_replace(MPN)
                        else:
                            catpdp.mpn = c_replace(Product_ID)
                    except Exception as e:
                        logger.info("Error in scrape header MPN : {}".format(e))
                        return None

                    """Canonical url"""
                    canonical_url = response.xpath('//link[@rel="canonical"]//@href').get()
                    if canonical_url:
                        catpdp.canonical_url = canonical_url
                    else:
                        catpdp.canonical_url = "n/a"

                    """ List Price """
                    try:
                        list_price = response.xpath("""//meta[@name='productprice']//@content""").get()
                        if list_price:
                            catpdp.regular_price = str(c_replace(list_price).replace('$', ''))
                        elif response.xpath('//div[contains(text(),"Web Price")]//span/strike//text()'):
                            list_price = response.xpath('//div[contains(text(),"Web Price")]//span/strike//text()').get()
                            catpdp.regular_price = str(c_replace(list_price).replace('$', ''))
                        elif response.xpath('//dd[contains(text(),"List price")]//text()'):
                            list_price = response.xpath('//dd[contains(text(),"List price")]//text()').get()
                            catpdp.regular_price = str(c_replace(list_price).replace('$', '').replace('List price: $', ''))
                        else:
                            catpdp.regular_price = 'n/a'
                    except Exception as e:
                        logger.info("Error in scrape header List Price : {}".format(e))
                        return None

                    """ Markdown Price """
                    try:
                        markdown_price = response.xpath("""//meta[@name='productpromotionprice']//@content""").get()
                        if markdown_price:
                            catpdp.final_price = str(c_replace(markdown_price).replace('$', ''))
                        elif response.xpath(
                                '//dl[@id="builderPricingSummary"]//dd[contains(@data-pricetypevalue,"potentialCouponPrice-COUPONPRICE")]//text()'):
                            markdown_price = response.xpath(
                                '//dl[@id="builderPricingSummary"]//dd[contains(@data-pricetypevalue,"potentialCouponPrice-COUPONPRICE")]//text()').get()
                            catpdp.final_price = str(c_replace(markdown_price).replace('$', ''))
                        elif response.xpath(
                                '//dt[contains(text(),"After Instant Savings")]//following-sibling::dd//text()'):
                            markdown_price = response.xpath(
                                '//dt[contains(text(),"After Instant Savings")]//following-sibling::dd//text()').get()
                            catpdp.final_price = str(c_replace(markdown_price).replace('$', ''))
                        elif response.xpath('//dd[contains(text(),"Sale price")]//text()'):
                            markdown_price = response.xpath('//dd[contains(text(),"Sale price")]//text()').get()
                            catpdp.final_price = str(c_replace(markdown_price).replace('$', '').replace('Sale price: $', ''))
                        elif response.xpath('//dd[@itemprop="price"]//text()'):
                            markdown_price = response.xpath('//dd[@itemprop="price"]//text()').get()
                            catpdp.final_price = str(c_replace(markdown_price).replace('$', '').replace('Sale price: $', ''))
                        elif response.xpath('//p[@itemprop="price"]//text()'):
                            markdown_price = response.xpath('//p[@itemprop="price"]//text()').get()
                            catpdp.final_price = str(c_replace(markdown_price).replace('$', '').replace('Sale price: $', ''))
                        else:
                            catpdp.final_price = 'n/a'
                    except Exception as e:
                        logger.info("Error in scrape header Markdown Price : {}".format(e))
                        return None

                    if catpdp.final_price == 'n/a':
                        catpdp.final_price = catpdp.regular_price
                        catpdp.regular_price = 'n/a'



                    """ Seller Name """
                    catpdp.Seller_space_Name = 'n/a'

                    """ Stock Status """
                    try:
                        stock_status=response.xpath('//meta[@name="productstatus"]//@content').get()
                        unavail=response.xpath('//div[contains(@data-marketing-status,"Temporarily Unavailable")]').get()
                        if not stock_status and unavail:
                            catpdp.stock_availability = 'Out of Stock'
                        if stock_status:
                            if 'unavailable' in stock_status.lower() or 'end of life' in stock_status.lower():
                                catpdp.stock_availability = 'Out of Stock'

                            elif 'available' in stock_status.lower():
                                catpdp.stock_availability = 'In Stock'

                            elif response.xpath("//span[contains(text(),'The product you are looking for is no longer available')]"):
                                catpdp.stock_availability = 'Out of Stock'
                            elif response.xpath('//span[@class="stock_message"]//text()'):
                                Stock_Status = response.xpath('//span[@class="stock_message"]//text()').get()
                                if "Out of Stock" in Stock_Status or "out of stock" in Stock_Status:
                                    catpdp.stock_availability = 'Out of Stock'
                                elif "Only few left" in Stock_Status or "only few left" in Stock_Status:
                                    catpdp.stock_availability = 'In Stock'
                                else:
                                    catpdp.stock_availability = 'In Stock'
                            elif response.xpath("//button[contains(text(),'Customize')]"):
                                catpdp.stock_availability = 'In Stock'
                            elif response.xpath("//button[contains(text(),'Add to cart')]//text()"):
                                Stock_Status = response.xpath("//button[contains(text(),'Add to cart')]//text()").get()
                                if "Add to cart" in Stock_Status or "add to cart" in Stock_Status:
                                    catpdp.stock_availability = 'In Stock'
                                else:
                                    return None
                            elif response.xpath('//button[@id="addToCartButtonTop"]//text()'):
                                Stock_Status = response.xpath('//button[@id="addToCartButtonTop"]//text()').getall()
                                if "add to cart" in (''.join(c_replace(Stock_Status))).lower():
                                    catpdp.stock_availability = 'In Stock'
                                else:
                                    return None
                        else:
                            catpdp.stock_availability = 'Out of Stock'
                    except Exception as e:
                        logger.error("Error in scrape header Stock Status at url :{} {}".format(e, product_url))
                        return None



                    if catpdp.regular_price == 'n/a' and catpdp.final_price == 'n/a' and catpdp.stock_availability != 'Out of Stock' :
                        try:
                            price_headers = {
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.3'
                            }

                            price_req = 'https://www.lenovo.com/ca/en/thinkvisionM14/p/61DDUAR6US/singlev2/price/json'
                            req = requests.get(url=price_req, headers=price_headers)
                            # print(req.text)
                            price_data = eval(req.text)
                            list_price = price_data.get('price')
                            if list_price:
                                catpdp.regular_price = c_replace(list_price)
                            else:
                                catpdp.regular_price = 'n/a'
                            markdown_price = price_data.get('potentialDiscountedPrice')
                            if markdown_price:
                                catpdp.final_price = c_replace(markdown_price)
                            else:
                                catpdp.final_price = 'n/a'
                        except Exception as e:
                            logger.info("Error in price req : {}".format(e))
                            # pass
                            return None


                    """ Image URL """
                    try:
                        image_url = response.xpath('//div[@class="image-pic"]//img//@src').get()
                        if image_url:
                            if "https" not in image_url:
                                catpdp.product_image = f'https:{c_replace(image_url)}'
                            else:
                                catpdp.product_image = image_url
                        elif response.xpath('//div[@class="galleryContent"]/img//@src'):
                            image_url = response.xpath('//div[@class="galleryContent"]/img//@src').get()
                            if "https" not in image_url:
                                catpdp.product_image = f'https://www.lenovo.com{c_replace(image_url)}'
                            else:
                                catpdp.product_image = image_url
                        elif response.xpath('//div[@class="hero-image"]/img//@src'):
                            image_url = response.xpath('//div[@class="hero-image"]/img//@src').get()
                            if "https" not in image_url:
                                catpdp.product_image = f'https://www.lenovo.com{c_replace(image_url)}'
                            else:
                                catpdp.product_image = image_url
                        else:
                            catpdp.product_image = 'n/a'
                    except Exception as e:
                        logger.error("Error in scrape header Image URL : {}".format(e))
                        return None

                    """ Lead time """
                    try:
                        lead_time = response.xpath('//meta[contains(@name,"Ship_date_")]//@content').get()
                        if lead_time:
                            lead_time = c_replace(lead_time)
                            if "call for availability" not in lead_time.lower():
                                catpdp.ship_n_sold = c_replace(lead_time)
                            else:
                                catpdp.ship_n_sold = 'n/a'
                        else:
                            catpdp.ship_n_sold = 'n/a'
                    except Exception as e:
                        logger.info("Error in scrape header Lead time : {}".format(e))
                        return None

                    """ Product Specification """
                    product_spec = ''
                    product_spec1 = ''
                    try:
                        product_specification = response.xpath('//div[@class="system_specs_container"]//ul//li//div[@class="title"]//text()').getall()
                        product_specification1 = response.xpath('//div[@class="system_specs_container"]//ul//li//div[@class="title"]//following-sibling::p//text()').getall()
                        if product_specification and product_specification1:
                            product_spec_keys = c_replace(product_specification)
                            # product_spec_values = c_replace(product_specification1)
                            speclist = []
                            for i in range(len(product_spec_keys)):
                                a = f"{product_spec_keys[i]}:{c_replace(product_specification1[i])}"
                                speclist.append(a)
                            product_spec = c_replace('#||#'.join(speclist))

                        if response.xpath('//table[@class="techSpecs-table"]//td[1]'):
                            # product_specification2 = response.xpath('//table[@class="techSpecs-table"]//td[1]').getall()
                            # product_specification3 = response.xpath('//table[@class="techSpecs-table"]//td[2]').getall()
                            # if product_specification2 and product_specification3:
                            #     keys = []
                            #     for i in product_specification2:
                            #         clean_tag = re.compile('<.*?>')
                            #         a = re.sub(clean_tag, '', i)
                            #         keys.append(c_replace(a))
                            #
                            #     values = []
                            #     for i in product_specification3:
                            #         clean_tag = re.compile('<.*?>')
                            #         a = re.sub(clean_tag, '', i)
                            #         values.append(c_replace(a))
                            #
                            #     spec_final = []
                            #     for i in range(len(keys)):
                            #         spec_final.append(f'{keys[i]}:{values[i]}')
                            spec_final = []
                            product_specification2 = response.xpath('//div[@id="tab-techspec"]//tr')
                            for k in product_specification2:
                                title = k.xpath('./td[1]//text()').get()
                                if title:
                                    value = k.xpath('./td[2]//text()').getall()
                                    value = "".join(value)
                                    s = k.xpath('./td[2]//table//tr')
                                    if s:
                                        for j in s:
                                            value = j.xpath('.//td//text()').getall()
                                            value = ",".join(value)
                                            spec_final.append(c_replace(f'{title}:{value}'))
                                    else:
                                        spec_final.append(c_replace(f'{title}:{value}'))

                            product_spec1 = '#||#'.join(spec_final).replace(',Dimensions', 'Dimensions')

                        if product_spec and product_spec1:
                            catpdp.technical_details = product_spec + '#||#' + product_spec1
                        elif product_spec:
                            catpdp.technical_details = product_spec
                        elif product_spec1:
                            catpdp.technical_details = product_spec1
                        else:
                            catpdp.technical_details = 'n/a'
                    except Exception as e:
                        logger.info("Error in scrape header Product Specification url :{} {}".format(e, product_url))
                        return None

                    # if catpdp.technical_details == 'n/a':
                    #     pro_spec = response.xpath('//table//tr//td[1]//text()').getall()
                    #     pro_spec1 = response.xpath('//table//tr//td[2]/div//text()').getall()
                    #     if pro_spec and pro_spec1:
                    #         pro_spec = c_replace(pro_spec)
                    #         pro_spec1 = c_replace(pro_spec1)
                    #         if len(pro_spec) == len(pro_spec1):
                    #             spec_list = []
                    #             for i in range(len(pro_spec)):
                    #                 a = f"{pro_spec[i]}:{c_replace(pro_spec1[i])}"
                    #                 spec_list.append(a)
                    #             catpdp.technical_details = c_replace('#||#'.join(spec_list))

                    """new speccc"""
                    if catpdp.technical_details == 'n/a':
                        specification_key = response.xpath('//div[@class="tabbedBrowse"]//ul[@id="tab-content"]//li[@id="tab-li-techspec"]//table[@class="techSpecs-table"]//tr//td[1]').getall()
                        specification_key = c_replace(specification_key)
                        specification_value = response.xpath('//div[@class="tabbedBrowse"]//ul[@id="tab-content"]//li[@id="tab-li-techspec"]//table[@class="techSpecs-table"]//tr//td[2]').getall()
                        specification_value = c_replace(specification_value)
                        if len(specification_key) == len(specification_value):
                            spec_dict = dict(zip(specification_key, specification_value))

                            specifiaction_main_ls = []
                            for k, v in spec_dict.items():
                                specs = k + ':' + v
                                specifiaction_main_ls.append(specs)
                            if specifiaction_main_ls:
                                catpdp.technical_details = c_replace('#||#'.join(specifiaction_main_ls))
                            else:
                                catpdp.technical_details = 'n/a'

                    if catpdp.technical_details == '':
                        catpdp.technical_details = 'n/a'

                    # """ status """
                    # catpdp.status = "Done"


                    if catpdp.technical_details == 'n/a':
                        allnew_spec=response.xpath('//div[@class="specs-inner"]//tr[contains(@class,"item")]')
                        if allnew_spec:
                            technical_details=[]
                            for ks in  allnew_spec:
                                s_key=ks.xpath('.//th//text()').get()
                                s_value=ks.xpath('.//td//text()').getall()
                                dict_spec=f"{s_key}:{c_replace(''.join(s_value))}"
                                technical_details.append(dict_spec)

                            catpdp.technical_details = c_replace("#||#".join(technical_details))

                    """ Product Description """
                    try:
                        product_description = response.xpath("""//div[@class="hero-productDescription mediaGallery-productDescription"]//text()""").getall()
                        if not product_description:
                            product_description_check = response.xpath("""//div[@class="banner_content_desc"]""").get()
                            if 'class="system_specs_title"' not in product_description_check:
                                product_description = response.xpath("""//div[@class="banner_content_desc"]//ul//li//text()""").getall()
                        if product_description:
                            catpdp.product_description = c_replace(' '.join(c_replace(product_description)))
                        elif response.xpath("""//p[@class="hero-description"]//text()"""):
                            product_description = response.xpath('//p[@class="hero-description"]//text()').getall()
                            catpdp.product_description = ' '.join(c_replace(product_description))
                        elif response.xpath('//div[@class="overviewSection"]//div//text()'):
                            product_description = response.xpath('//div[@class="overviewSection"]//div//text()').getall()
                            product_description = c_replace(product_description)
                            product_description = ' '.join(product_description)
                            product_description = c_replace(product_description.replace(".bld { font-weight: bold; }", ""))
                            product_description = product_description.replace(".bld {font-weight: bold;}", "")
                            product_description = c_replace(product_description)

                            if product_description:

                                catpdp.product_description = product_description
                            else:
                                catpdp.product_description = 'n/a'


                        else:
                            catpdp.product_description = 'n/a'
                    except Exception as e:
                        logger.info("Error in scrape header SProduct Description : {}".format(e))
                        return None


                    """ Product Features """
                    try:
                        product_features = response.xpath('//div[@name="features"]//div[contains(@class,"feature-item")]//text()').getall()
                        if product_features:
                            product_features = c_replace(product_features)
                            catpdp.features = c_replace(' '.join(product_features))
                        elif response.xpath('//div[@id="tab-features"]//p//text()'):
                            product_features = response.xpath('//div[@id="tab-features"]//p//text()').getall()
                            product_features = c_replace(product_features)
                            catpdp.features = c_replace(' '.join(product_features))
                        elif response.xpath('//div[@class="bundleIncludesItmes"]//ul//li//text()'):
                            product_features = response.xpath(
                                '//div[@class="bundleIncludesItmes"]//ul//li//text()').getall()
                            product_features = c_replace(product_features)
                            catpdp.features =c_replace('#||#'.join(product_features))
                        else:
                            catpdp.features = 'n/a'
                    except Exception as e:
                        logger.info("Error in scrape header Product Features : {}".format(e))
                        return None

                    """===================================="""

                    catpdp.HtmlPath_search = 'n/a'

                    catpdp.category = 'n/a'

                    catpdp.category_path = 'n/a'

                    catpdp.category_path_url = 'n/a'

                    catpdp.division = 'n/a'

                    catpdp.department = 'n/a'

                    catpdp._class = 'n/a'

                    catpdp.subclass = 'n/a'

                    catpdp.cat_id = 'n/a'

                    catpdp.cat_rank = str(1)

                    catpdp.regular_price_range = "n/a"

                    catpdp.shipping_price = "n/a"

                    catpdp.brand = 'n/a'

                    catpdp.shipping_text = 'n/a'

                    catpdp.reviews_count = 'n/a'

                    catpdp.average_rating = 'n/a'

                    catpdp.upc = 'n/a'

                    # catpdp.technical_details = 'n/a'

                    catpdp.meta_keywords = 'n/a'

                    catpdp.stock_status = 'n/a'

                    catpdp.item_condition = 'n/a'

                    catpdp.buybox_winner_vendor_name = 'n/a'

                    catpdp.buybox_winner_vendor_price = 'n/a'

                    catpdp.top_3_buybox_winners = 'n/a'

                    catpdp.top_3_buybox_winners_price = 'n/a'

                    catpdp.item_status = 'n/a'

                    catpdp.item_level_status = 'n/a'

                    catpdp.color = 'n/a'

                    catpdp.price_by_size = 'n/a'

                    catpdp.additional_information = 'n/a'

                    catpdp.promo_message = 'n/a'

                    catpdp.price_promo = 'n/a'

                    catpdp.promo_description = 'n/a'

                    catpdp.live_category_path = 'n/a'

                    catpdp.online_exclusive = 'n/a'

                    catpdp.extraction_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    catpdp.image_url_large = 'n/a'

                    catpdp.image_url_small = 'n/a'

                    catpdp.base_unique_identifier = 'n/a'

                    catpdp.page_title = 'n/a'

                    catpdp.shipping_weight = 'n/a'

                    # catpdp.meta_description = 'n/a'

                    catpdp.product_dimensions = 'n/a'

                    catpdp.product_weight = 'n/a'

                    catpdp.product_material = 'n/a'
                    catpdp.markdown_price = "n/a"

                    """ status """
                    catpdp.status = "Done"
                    catpdp.Stock_space_Message = 'n/a'
                    catpdp.Condition = 'n/a'
                    catpdp.warrenty = 'n/a'

                    """ Update_productdata_Query """
                    updateproduct = catpdp.Update_productdata_Query().encode('utf-8', 'replace').decode()
                    print(updateproduct)
                    self.cursor.execute(updateproduct)
                    self.con.commit()

                elif response.status==404 or 'page-not-found__title' in response.text:
                    catpdp.mpn = c_replace(Product_ID)
                    catpdp.product_name = 'n/a'

                    catpdp.stock_availability = 'n/a'
                    catpdp.technical_details = 'n/a'
                    catpdp.ship_n_sold = 'n/a'

                    catpdp.Seller_space_Name = 'n/a'
                    catpdp.features = 'n/a'

                    catpdp.canonical_url = "n/a"
                    catpdp.product_description = 'n/a'

                    catpdp.final_price = 'n/a'

                    catpdp.regular_price = 'n/a'

                    catpdp.meta_description = "n/a"
                    catpdp.product_image = 'n/a'

                    catpdp.meta_title = 'n/a'

                    catpdp.HtmlPath_search = 'n/a'

                    catpdp.category = 'n/a'

                    catpdp.category_path = 'n/a'

                    catpdp.category_path_url = 'n/a'

                    catpdp.division = 'n/a'

                    catpdp.department = 'n/a'

                    catpdp._class = 'n/a'

                    catpdp.subclass = 'n/a'

                    catpdp.cat_id = 'n/a'

                    catpdp.cat_rank = "n/a"

                    catpdp.regular_price_range = "n/a"

                    catpdp.shipping_price = "n/a"

                    catpdp.brand = 'n/a'

                    catpdp.shipping_text = 'n/a'

                    catpdp.reviews_count = 'n/a'

                    catpdp.average_rating = 'n/a'

                    catpdp.upc = 'n/a'

                    # catpdp.technical_details = 'n/a'

                    catpdp.meta_keywords = 'n/a'

                    catpdp.stock_status = 'n/a'

                    catpdp.item_condition = 'n/a'

                    catpdp.buybox_winner_vendor_name = 'n/a'

                    catpdp.buybox_winner_vendor_price = 'n/a'

                    catpdp.top_3_buybox_winners = 'n/a'

                    catpdp.top_3_buybox_winners_price = 'n/a'

                    catpdp.item_status = 'n/a'

                    catpdp.item_level_status = 'n/a'

                    catpdp.color = 'n/a'

                    catpdp.price_by_size = 'n/a'

                    catpdp.additional_information = 'n/a'

                    catpdp.promo_message = 'n/a'

                    catpdp.price_promo = 'n/a'

                    catpdp.promo_description = 'n/a'

                    catpdp.live_category_path = 'n/a'

                    catpdp.online_exclusive = 'n/a'

                    catpdp.extraction_date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

                    catpdp.image_url_large = 'n/a'

                    catpdp.image_url_small = 'n/a'

                    catpdp.base_unique_identifier = 'n/a'

                    catpdp.page_title = 'n/a'

                    catpdp.shipping_weight = 'n/a'

                    # catpdp.meta_description = 'n/a'

                    catpdp.product_dimensions = 'n/a'

                    catpdp.product_weight = 'n/a'

                    catpdp.product_material = 'n/a'
                    catpdp.markdown_price = "n/a"

                    """ status """
                    catpdp.status = "Not found"
                    catpdp.Stock_space_Message = 'n/a'
                    catpdp.Condition = 'n/a'
                    catpdp.warrenty = 'n/a'


                    """ Update_productdata_Query """
                    updateproduct = catpdp.Update_productdata_Query().encode('utf-8', 'replace').decode()
                    print(updateproduct)
                    self.cursor.execute(updateproduct)
                    self.con.commit()

                    print("something went wrong, check properly.........")
                    logger.info("something went wrong, check properly.........")
                    return None
                # print("Product Not found, Status code:{}".format(response.status))
                # meta_dict = response.meta.get('meta_dict')
                # row_id = meta_dict.get('row_id')
                # product_url = meta_dict.get('product_url')
                # catpdp.status = "Not Found"
                #
                # catpdp.Date_space_of_space_Crawl = datetime.today().strftime('%m/%d/%Y %H:%M:%S %p')
                # catpdp.Product_space_URL = product_url
                # catpdp.Product_space_ID = 'n/a'
                # catpdp.cat_id = str(row_id).encode('ascii', 'ignore').decode("utf-8")
                # catpdp.HtmlPath_search = meta_dict.get('HtmlPath_search')
                # catpdp.category_url = meta_dict.get('category_url')
                # catpdp.cat_rank = str(meta_dict.get('cat_rank'))
                # catpdp.Retailer = "amazon.fr"
                # catpdp.brand = 'n/a'
                # catpdp.Product_space_Title = 'n/a'
                # catpdp.Image_space_URL = 'n/a'
                # catpdp.MPN = 'n/a'
                # catpdp.List_space_Price = 'n/a'
                # catpdp.Markdown_space_Price = 'n/a'
                # catpdp.Seller_space_Name = 'n/a'
                # catpdp.Stock_space_Status = 'n/a'
                # catpdp.Product_space_Description = 'n/a'
                # catpdp.Product_space_Specification = 'n/a'
                # catpdp.Product_space_Features = 'n/a'
                # catpdp.Lead_space_time = 'n/a'
                #
                # filename = f'/Not_Found_id_{row_id}.html'
                # path = self.F_PATH + filename
                # path = path.replace("\\", "/")
                # if not os.path.exists(path):
                #     with open(path, 'wb') as f:
                #         f.write(response.body)
                #
                # catpdp.htmlpath = path
                # """ Update_productdata_Query """
                # updateproduct = catpdp.Update_productdata_Query()
                # # print(updateproduct)
                # self.cursor.execute(updateproduct)
                # self.con.commit()

        except Exception as e:
            import sys
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error("parse main error: {}".format(e))
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno
            logger.error('line---:{}'.format(sys.exc_info()))
            logger.error("Exception type: {}".format(exception_type))
            logger.error("File name: {}".format(filename))
            logger.error("Error is:{} ".format(e))
            logger.error("Line number: {}:".format(line_number))

    def close(spider, reason):
        try:
            sql = f"SELECT id FROM {db_data_table} where status='Pending'"
            # brand_pend = f"SELECT id FROM {db_category_table} where status='Pending'"
            cursor = UgamLenovoCaPriceDailyPipeline.cursor
            cursor.execute(sql)
            linkdata_row = cursor.fetchall()
            # cursor.execute(brand_pend)
            # brand_row = cursor.fetchall()

            if linkdata_row == ():
                print('spider is close,...................')
                print('going on QA and make csv..............')
                print("Going to make CSV..")
                # from croma_in_category_daily.export_csv import Export_Csv
                from ugam_lenovo_ca_price_daily.export_csv_new_upload import Export_Csv
                c = Export_Csv()
                c.export_csv()
                print("CSV Done..")

                """E-Office"""
                # todo..-----E-Office----------------------------------------------------------
                feedcon = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name)
                feedcursor = feedcon.cursor()
                feedid = "924"

                total_product_count = "SELECT count(id) FROM input_sku"
                feedcursor.execute(total_product_count)
                tpc = feedcursor.fetchall()
                a = tpc[0][0]

                found_query = f"SELECT count(id) FROM {db_data_table} WHERE STATUS='Done' AND `product_name`!=''"
                feedcursor.execute(found_query)
                fq = feedcursor.fetchall()
                b = fq[0][0]

                not_found_query = f"SELECT count(id) FROM {db_data_table} WHERE STATUS='Not Found'"
                feedcursor.execute(not_found_query)
                nfq = feedcursor.fetchall()
                c = nfq[0][0]
                feedcon.commit()
                feedcon.close()
                try:
                    print("Updating to e-office....")
                    catpdp.E_office_products_Update(feedid, str(a), str(b), str(c))
                    print("Updated to e-office..")
                except Exception as e:
                    print("E-office error.. ", e)
                try:
                    subprocess.call([r"D:\Ugam_File_Upload_App\UGAM_Upload_File_APP.exe",
                                     r"D:\Dhruv\Ugam\ugam_lenovo_ca_price_daily\ugam_lenovo_ca_price_daily\ftpconfig.text"])

                except Exception as e:
                    logger.error('exception in file method in call subprocess :{}'.format(e))
            else:
                ...
            # spider.start_requests()
            # ESpiderSpider.start_requests(self='')
            # execute('scrapy crawl emag -a start=120 -a end=120'.split())
        except Exception as e:
            logger.error('error in close spider method error :{}'.format(e))

#

if __name__ == '__main__':

    from scrapy.cmdline import execute
    #
    # # execute('scrapy crawl lenovo_ca_product'.split())
    execute('scrapy crawl lenovo_ca_product -a start=1 -a end=150'.split())

