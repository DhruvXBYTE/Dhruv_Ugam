"--------New change file......12-12-2021............"

from scrapy.cmdline import execute
import re
from scrapy.selector import Selector
import subprocess
import pymysql
from datetime import time
import json
import scrapy
from mymodules._common_ import c_replace
from ugam_saturn_de.pipelines import *
from ugam_saturn_de.config import *
from random_user_agent.params import SoftwareName, OperatingSystem
from random_user_agent.user_agent import UserAgent
from random import choice
import time
import requests

def get_useragent():
    l1 = [SoftwareName.CHROME.value, SoftwareName.FIREFOX.value, SoftwareName.OPERA.value]
    software_names = [choice(l1)]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value, OperatingSystem.SUNOS.value]
    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=1000)
    return user_agent_rotator.get_random_user_agent()

headers={

    'authority': 'www.saturn.de',
    'method':'GET',
    'scheme': 'https',
    # 'accept': 'text/html,applicatin/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language':'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    # 'cookie': 'optid=3d8c3824-eb71-4464-86e3-06285ac19494; a=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im8yc2lnbiJ9.eyJzdWIiOiI2MjM0ZDc5MS00ODBiLTQ1OWQtYmZmYi01ZDdkOTJhMzkxZmIiLCJpc3MiOiJtbXNlIiwiaWF0IjoxNjUzOTE0OTU2LCJleHAiOjE2NTUxMjQ1NTYsImF1ZCI6IndlYm1vYmlsZSIsInQiOiJ1IiwibyI6MTAxNX0.Be1A4HOFRAUp550_K4KL-PZSeh7hQkz_xVsATBqCM7Lm2800tDuOrIPflLW1I-88Kt_VD-VnizK_xVN1Mb4gAojpTVGqSQFhB9_E8gSYdgr97IJ8JPAx6OoMdIa2K4Qrg_IU64fYw4O06eZXlW8WOtqX-WAWggQrOEMyWACmq21nvFwawYM1Jrp6MB2MupKQZ9wCEPiTAa-rjq6ggVSAHr3OSEQGbXlLvMCCRkLp4AvT3JRWOcEBEeq35XDnOdqMLaZPPuFf5yy6nQwPZT8jwTzQi0qOdWPARjIAKcnEXLgpBQqokQFjc13YKIYpaXzXCVcRMl5HSSy01AJ7MqOv1Q; r=yDpWJidQZ+sAySIePPU7VppmdgMRCG8SqQ+xHQgAgcWZ0LDtS1taxiCf7EDV9E1d; pwaconsent=v:1.0~required:1&clf:1,cli:1,gfb:1,gtm:1,jot:1,ocx:1|comfort:1&baz:1,cne:1,fix:1,gfa:1,gfc:1,goa:1,gom:1,grc:1,grv:1,lob:1,opt:1,orc:1,ore:1,prd:1,sen:1,sis:1,spe:1,sst:1,swo:1,twi:1,usw:1,usz:1,yte:1|marketing:1&asm:1,cad:1,cma:1,eam:1,fab:1,fbn:1,gad:1,gam:1,gcm:1,gdv:1,gos:1,gse:1,gst:1,kru:1,msb:1,omp:1,pin:1,ttd:1,twt:1|; _gcl_au=1.1.774652435.1653914961; _gid=GA1.2.541576144.1653914961; _pin_unauth=dWlkPU56azJZVGs0WXpjdFpqVXhOaTAwTlRVekxXRmhZbUl0TVRGa04yRXpOamxsTW1WbA; NoCookie=true; t_fpd=true; s_id=f0751285-9373-405f-8cf5-64c3757331a6; MC_PS_SESSION_ID=f0751285-9373-405f-8cf5-64c3757331a6; p_id=f0751285-9373-405f-8cf5-64c3757331a6; MC_PS_USER_ID=f0751285-9373-405f-8cf5-64c3757331a6; __cfruid=4d814b86914410e679ff531751b35c8c4325a56d-1654148724; _clck=16zo6gw|1|f1z|0; ts_id=53ba3848-7f66-4e6e-a8ad-b6ba12b3a6c6; _msbps=95; __cf_bm=42Xg6ru12HcHIaxM_Xj7FH0VKQ6a98YVqnWOYKLXBEs-1654159670-0-ASjrpq9erEVTW3m9I2WZagTikMQjkZhZ+WtLOdcnTWf7ZJ1Dg3vlJ/o+sX1rKhS6j0f1QFhIOz/+oEk8FvR5P1CWG5Yey8DgzWquvG/qWXR1; lux_uid=165416010751407882; _dc_gtm_UA-25101917-1=1; _ga=GA1.1.639b70cf-d794-475c-8297-dba226e2f1b7; _ga_9ZJL7DLSGD=GS1.1.1654160108.25.0.1654160108.60; _uetsid=ecea1860e01611ec90c8b763030d21d4; _uetvid=ecea33f0e01611ec901847a194851ed5; BVBRANDID=edfb344a-dffd-4ba6-88ac-b3ce38a334a4; BVBRANDSID=cfa982a5-202e-49e0-8624-1d4db7e6d83c; _clsk=1q01wa|1654160114076|1|1|a.clarity.ms/collect',
    'pragma': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': get_useragent(),

}

proxy_host = "proxy.zyte.com"
proxy_port = "8011"
proxy_auth = "6500c987aae7435a90c249b35b1c9376:"

proxies = {"https": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port),
            "http": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port)}


class JSpiderSpider(scrapy.Spider):
    name = 'monitor_product'
    F_PATH = HTML

    handle_httpstatus_list = [503]

    def __init__(self, start='', end=''):

        try:
            self.cursor = UgamSaturnDePipeline.cursor
            self.con = UgamSaturnDePipeline.con
            self.start = start
            self.end = end

        except Exception as e:
            print('exception in __init__ method main:{}'.format(e))

    def start_requests(self):

        try:
            # select_query = f"SELECT id,`Product URL`,`category_url`, `cat_rank`,`cat_id` FROM {data_table} WHERE Status = 'Pending' AND ID BETWEEN {self.start} AND {self.end}"
            sql_query = f"select id, `Product URL`, HtmlPath, cat_id, HtmlPath_search, category_url, cat_rank from {db_data_table} where Status = 'Pending' AND ID BETWEEN {self.start} AND {self.end}"
            self.cursor.execute(sql_query)
            core_list = [column for column in self.cursor.fetchall()]
            for itm in core_list:
                time.sleep(1)

                row_id = itm[0]
                product_url = itm[1]
                HtmlPath = itm[2]
                cat_id = itm[3]
                HtmlPath_search = itm[4]
                category_url = itm[5]
                cat_rank = itm[6]

                nw_product_id = c_replace(product_url.split('-')[-1])
                product_id = nw_product_id.split('.')[0]
                # print(nw_product_id)
                filename = f'/{product_id}.html'
                path = self.F_PATH + filename
                path = path.replace("\\", "/")

                # delete_duplicate_row = catpdp.delete_category_Query()
                # print(delete_duplicate_row)
                # self.cursor.execute(delete_duplicate_row)
                # self.con.commit()

                meta_dict = {
                    'product_url': product_url,
                    'row_id': row_id,
                    'HtmlPath_search': HtmlPath_search,
                    'category_url': category_url,
                    'cat_rank': cat_rank,
                    'product_id': product_id,
                    'cat_id': cat_id

                }

                nw_product_id = c_replace(product_url.split('-')[-1])
                product_id = nw_product_id.split('.')[0]

                filename = f'/{product_id}.html'
                path = self.F_PATH + filename
                path = path.replace("\\", "/")

                if os.path.exists(path):
                    pass
                else:
                    # print(url_zipcode)
                    re = requests.get(url=product_url, headers=headers, verify=False, proxies=proxies)
                    time.sleep(2)
                    re_text1 = re.text
                    while re.status_code != 200:
                        print("Review Response issue re-request ")
                        re = requests.get(url=product_url, headers=headers, verify=False, proxies=proxies)
                        time.sleep(2)
                        re_text1 = re.text
                        with open(path, 'w', encoding="utf-8") as f:
                            f.write(re_text1)
                    else:
                        if os.path.exists(path):
                            pass
                        else:
                            with open(path, 'w', encoding="utf-8") as f:
                                f.write(re_text1)
                            time.sleep(1)

                if os.path.exists(path):
                    yield scrapy.FormRequest(url=f'file:///{path}', callback=self.parse, meta={'meta_dict': meta_dict})


        except Exception as e:
            print(e)

    def parse(self, response, **kwargs):

        print("Status", response.status)

        try:
            # todo ------------------------------- NOTFOUND ----------------------------
            if "Not Found" in response.text:

                print("Product Not found, Status code:{}".format(response.status))
                meta_dict = response.meta.get('meta_dict')
                row_id = meta_dict.get('row_id')

                product_url = meta_dict.get('product_url')
                catpdp.status = "Not Found"

                catpdp.Date_space_of_space_Crawl = datetime.today().strftime('%m/%d/%Y %H:%M:%S %p')
                catpdp.Product_space_URL = product_url.replace("'", "\\'")
                print(catpdp.Product_space_URL)
                catpdp.Product_space_ID = 'n/a'
                catpdp.cat_id = str(row_id)
                catpdp.HtmlPath_search = meta_dict.get('HtmlPath_search')
                catpdp.category_url = meta_dict.get('category_url')
                catpdp.cat_rank = str(meta_dict.get('cat_rank'))
                catpdp.Retailer = "Lenovo.com"
                catpdp.Brand = 'n/a'
                catpdp.Product_space_Title = 'n/a'
                catpdp.Image_space_URL = 'n/a'
                catpdp.MPN = 'n/a'
                catpdp.List_space_Price = 'n/a'
                catpdp.Markdown_space_Price = 'n/a'
                catpdp.Seller_space_Name = 'n/a'
                catpdp.Stock_space_Status = 'n/a'
                catpdp.Product_space_Description = 'n/a'
                catpdp.Product_space_Specification = 'n/a'
                catpdp.Product_space_Features = 'n/a'
                catpdp.Lead_space_time = 'n/a'

                filename = f'/Not_Found_id_{row_id}.html'
                path = self.F_PATH + filename
                path = path.replace("\\", "/")
                if not os.path.exists(path):
                    with open(path, 'wb') as f:
                        f.write(response.body)

                catpdp.htmlpath = path
                """ Update_productdata_Query """
                updateproduct = catpdp.Update_productdata_Query()
                # print(updateproduct)
                self.cursor.execute(updateproduct)
                self.con.commit()

            elif "</html>" in str(response.body):

                catpdp.intialize_variable()
                meta_dict = response.meta.get('meta_dict')
                row_id = meta_dict.get('row_id')
                HtmlPath_search = meta_dict.get('HtmlPath_search')
                cat_id = meta_dict.get('cat_id')
                # Product_URL = response.meta.get('Product_URL')
                cat_rank = meta_dict.get('cat_rank')
                Product_URL = meta_dict.get('product_url')
                print("------Product_URL:", Product_URL)
                category_url = meta_dict.get('category_url')

                nw_product_id = c_replace(Product_URL.split('-')[-1])
                product_id = nw_product_id.split('.')[0]

                if len(product_id) > 7:
                    prod_id = Product_URL.split(".", -1)[-2].split("-", -1)[-1]
                else:
                    prod_id = product_id

                filename = f'/{prod_id}.html'
                path = self.F_PATH + filename
                path = path.replace("\\", "/")
                if not os.path.exists(path):
                    with open(path, "w", encoding='utf-8') as f:
                        f.write(response.text)

                # Todo: end....

                # TODO ----------------------- PRICE --------------------------------

                main_json = response.xpath('//script[contains(text(),"__PRELOADED_STATE__")]//text()').get()
                # print("jsonresponse...........",main_json)
                if main_json:
                    main_json_1 = main_json.replace('window.__PRELOADED_STATE__ = ', '').replace(';', '')
                    j_data = json.loads(main_json_1)
                    # print(".....FINAL JSON...!",j_data)

                    pro_jason = j_data['apolloState']
                    # apolloState.GraphqlProduct:2723592.title
                    name = pro_jason[f'GraphqlProduct:{prod_id}']['title']
                    print("Title Name....", name)
                    product_title = c_replace(name)
                    # #price({"id":"2723592"})
                    price_data = pro_jason['ROOT_QUERY']

                    # TODO ------------------- DIRECT PRICE --------------
                    key = ''
                    for i in price_data:
                        if 'price' in str(i):
                            key = i
                            break
                    print(key)

                    # TODO ----------------------- MARKETPLACE PRICE ------------------
                    keym = ''
                    for x in price_data:
                        if 'marketplaceProductOffers' in str(x):
                            keym = x
                            break

                    # TODO ----------------------- PRICE & LEADTIME  ------------------
                    try:
                        price = pro_jason['ROOT_QUERY'][key]
                        if price == None:
                            price = pro_jason['ROOT_QUERY'][keym][0]['price']
                            print(price)
                            regular_price = None
                            try:
                                leadtime = pro_jason['ROOT_QUERY'][keym][0]['deliveryTime'][0]['latest']
                            except Exception as e:
                                print(e)
                                leadtime="n/a"

                        else:
                            price = pro_jason['ROOT_QUERY'][key]['price']
                            regular_price = pro_jason['ROOT_QUERY'][key]['strikePrice']
                            avai=''
                            for a in price_data:
                                if 'availability' in a:
                                    avai=a
                                    break
                            try:
                                leadtime=pro_jason['ROOT_QUERY'][avai]['delivery']['latest']
                                print(leadtime)
                            except Exception as e:
                                print(e)
                                leadtime="n/a"


                        if leadtime==None:
                            leadtimep="n/a"
                        else:
                            leadtimep=leadtime
                        final_price = c_replace(str(price))
                        if regular_price is not None:
                            regular_price = c_replace(str(regular_price))
                        else:
                            regular_price = 'n/a'
                        # print(" FINAL PRICE", final_price)
                        # print(" Regular Price", regular_price)
                    except:
                        final_price = 'n/a'
                        leadtimep = "n/a"
                        regular_price = 'n/a'

                    # TODO ------------------- First_description -----------------------------

                    try:
                        try:
                            First_des = pro_jason[f'GraphqlProduct:{prod_id}']['content']['infoTeaser']['secondParagraph'][0]['json']['content'][0]['content'][0]['value']
                        except:
                            First_des = ''
                        First_des = c_replace(First_des)
                        # print("FIRST_DESC", First_des)
                        try:
                            description = pro_jason[f'GraphqlProduct:{prod_id}']['description']
                            if description == None:
                                description = ''
                        except:
                            description = ''

                        # print("Secound_Desc", description)
                        if First_des != '' or description != '':
                            description = c_replace(description)
                            Final_Descriptions = First_des + description
                        else:
                            Final_Descriptions = description

                        if Final_Descriptions == '':
                            product_description = "n/a"
                        else:
                            product_description = Final_Descriptions
                    except:
                        product_description = 'n/a'
                        # print("PRODUCT_DEC", product_description)

                    # todo ------------------- IMAGE URL ---------------------------------------

                    try:
                        # Image = pro_jason[f'GraphqlProduct:{prod_id}']['assets'][0]['link'] #apolloState.GraphqlProduct:2723592.assets[0].link
                        Image = pro_jason[f'GraphqlProduct:{prod_id}']['titleImageId']  # apolloState.GraphqlProduct:2723592.assets[0].link
                        final_image = f'https://assets.mmsrg.com/isr/166325/c1/-/{Image}'
                        product_image = final_image
                        print('PRODUCT URL', product_image)

                    except Exception as  e:
                        print(e)

                    # TODO --------------------  Specifications ------------------------------------

                    # TEcnical_details = apolloState.GraphqlProduct:2723592.featureGroups[0].features[0].name
                    tech = pro_jason[f'GraphqlProduct:{prod_id}']['featureGroups']
                    # print(tech)
                    key_list = []
                    value_list = []

                    for a in tech:
                        features_1 = a['features']
                        # print("features_1 is hear", features_1)
                        for b in features_1:

                            features_key = b['name']
                            features_value = b['value']
                            key = features_key

                            try:
                                features_unit = b['unit']
                            except:

                                features_unit = ""
                            key_list.append(key)
                            if features_unit:
                                value = features_value + " " + features_unit
                            else:
                                value = features_value
                            value_list.append(value)
                            # print("KEYS ..... key is here",key)

                    tech_dict = dict(zip(key_list, value_list))
                    tech_details = []

                    for k, v in tech_dict.items():
                        tech_details.append(f'{k}:{v}')
                    exact_tech = '#||#'.join(tech_details)
                    technical_details = c_replace(exact_tech)
                    # print("Spec ",technical_details)

                    Avaiblity = response.xpath('//script[contains(text(),"availability")]//text()').get()
                    # print("Availability",Avaiblity)
                    if Avaiblity:
                        try:

                            Avaiblity_ = json.loads(Avaiblity)
                            on_off = Avaiblity_['offers']['availability']
                            on_off = on_off.split('/')[-1]
                            stock_availability = c_replace(on_off)
                            if stock_availability == "InStock":
                                stock_availability = "In Stock"
                            else:
                                stock_availability = "Out of stock"

                            # print("stock_avialability ",stock_availability)

                            brand = Avaiblity_['brand']['name']
                            # print("BRAND ", brand)
                        except:

                            stock_availability = 'Out of stock'
                            brand = product_title.split()[0]
                            # print("BRAND", brand)
                    else:
                        stock_availability = 'Out of stock'
                        brand = product_title.split()[0]
                        # print("BRAND",brand)

                    # TODO --------------------  MPN  -----------------------------------

                    try:
                        tech1 = pro_jason[f'GraphqlProduct:{prod_id}']['featureGroups']
                        # print(tech1)
                        final = {}
                        for a in tech1:
                            features_1 = a['features']
                            for b in features_1:
                                name = b['name']
                                value = b['value']
                                mpn_d = {name: value}
                                final.update(mpn_d)
                        mpn = final.get('Modelkennung')
                        # print(final)
                        # print(mpn)

                        if mpn == None:
                            catpdp.MPN = str("n/a")
                        else:
                            catpdp.MPN = mpn

                    except Exception as e:
                        logger.error("Error in scrape header MPN : {}".format(e))
                        return None

                    # TODO ----------------------  Seller_Name  ---------------------------

                    try:
                        seller_name = pro_jason['ROOT_QUERY'][keym][0]['sellerName']
                    except Exception as e:
                        print(e)
                        seller_name="n/a"

                    # apolloState.ROOT_QUERY.pwaFooter.legalText.json.content[2].content[0].value

                    catpdp.category_url = c_replace(category_url)
                    catpdp.status = "Done"
                    catpdp.Seller_space_Name = c_replace(seller_name)

                    # catpdp.MPN=c_replace(mpn)

                    catpdp.Condition = 'n/a'

                    catpdp.Brand = brand

                    catpdp.category_url = meta_dict.get('category_url')

                    catpdp.warrenty = 'n/a'

                    # catpdp.Seller_space_Name = 'Saturn'

                    # catpdp.Lead_space_time = "n/a"
                    catpdp.Lead_space_time =leadtimep

                    catpdp.htmlpath = path

                    catpdp.HtmlPath_search = HtmlPath_search

                    date = datetime.today().strftime('%m/%d/%Y %H:%M:%S %p')

                    catpdp.Date_space_of_space_Crawl = str(date)

                    catpdp.Retailer = "Saturn.de"

                    catpdp.cat_row_id = str(cat_id)

                    catpdp.cat_rank = str(cat_rank)

                    catpdp.Product_space_ID = c_replace(str(prod_id))

                    catpdp.Product_space_Title = c_replace(product_title)

                    catpdp.Product_space_URL = c_replace(Product_URL)

                    catpdp.List_space_Price = c_replace(regular_price)

                    catpdp.Markdown_space_Price = c_replace(str(final_price))

                    catpdp.Stock_space_Status = stock_availability
                    catpdp.Stock_space_Message = "n/a"

                    catpdp.Product_space_Description = product_description

                    catpdp.Product_space_Specification = c_replace(technical_details)
                    catpdp.Product_space_Features = 'n/a'
                    catpdp.Image_space_URL = c_replace(product_image)

                    try:
                        updateproduct = catpdp.Update_productdata_Query()
                        print(updateproduct)
                        print("-----------NEXT URL---------------")
                        self.cursor.execute(updateproduct)
                        self.con.commit()
                    except Exception as e:
                        print(e)

                else:
                    print("something went wrong, check properly.........")
                    logger.info("something went wrong, check properly.........")
                    return None

        except Exception as e:
            print(e)

            catpdp.status = "Not Found"

            catpdp.MPN = "n/a"

            catpdp.Condition = 'n/a'

            catpdp.Brand = "n/a"

            catpdp.category_url = meta_dict.get('category_url')

            catpdp.warrenty = 'n/a'

            catpdp.Seller_space_Name = 'n/a'

            catpdp.Lead_space_time = "n/a"

            catpdp.htmlpath = path

            catpdp.HtmlPath_search = HtmlPath_search

            date = datetime.today().strftime('%m/%d/%Y %H:%M:%S %p')

            catpdp.Date_space_of_space_Crawl = str(date)

            catpdp.Retailer = "Saturn.de"

            catpdp.cat_row_id = str(cat_id)

            catpdp.cat_rank = str(cat_rank)

            catpdp.Product_space_ID = "n/a"

            catpdp.Product_space_Title = "n/a"

            catpdp.Product_space_URL = Product_URL

            catpdp.List_space_Price = "n/a"

            catpdp.Markdown_space_Price = "n/a"

            catpdp.Stock_space_Status = "Out of stock"
            catpdp.Stock_space_Message = "n/a"

            catpdp.Product_space_Description = "n/a"

            catpdp.Product_space_Specification = "n/a"
            catpdp.Product_space_Features = 'n/a'
            catpdp.Image_space_URL = "n/a"

            updateproduct = catpdp.Update_productdata_Query()
            print(updateproduct)
            print("-----------NEXT URL---------------")
            self.cursor.execute(updateproduct)
            self.con.commit()

    # def close(spider, reason):
    #
    #     try:
    #         sql = f"SELECT id FROM {db_data_table} where status='Pending'"
    #         brand_pend = f"SELECT id FROM {db_category_table} where status='Pending'"
    #         cursor = UgamSaturnCategoryPipeline.cursor
    #         cursor.execute(sql)
    #         linkdata_row = cursor.fetchall()
    #         cursor.execute(brand_pend)
    #         brand_row = cursor.fetchall()
    #
    #         if linkdata_row == () and brand_row == ():
    #             print('spider is close,...................')
    #             print('going on QA and make csv..............')
    #             print("Going to make CSV..")
    #             from ugam_saturn_de.export_tsv import Export_Csv
    #             c = Export_Csv()
    #             c.export_csv()
    #             print("CSV Done..")
    #         else:

    #             ...
    #         # spider.start_requests()
    #         # ESpiderSpider.start_requests(self='')
    #         # execute('scrapy crawl emag -a start=120 -a end=120'.split())
    #     except Exception as e:
    #         logger.error('error in close spider method error :{}'.format(e))


if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute('scrapy crawl monitor_product -a start=1 -a end=3000'.split())





# "--------New change file......12-12-2021............"
#
# from scrapy.cmdline import execute
# import re
# from scrapy.selector import Selector
# import subprocess
# import pymysql
# from datetime import time
# import json
# import scrapy
# from mymodules._common_ import c_replace
# from ugam_saturn_de.pipelines import *
# from ugam_saturn_de.config import *
# import time
# import requests
# from random_user_agent.params import SoftwareName, OperatingSystem
# from random_user_agent.user_agent import UserAgent
# from random import choice
#
#
# def get_useragent():
#     l1 = [SoftwareName.CHROME.value, SoftwareName.FIREFOX.value, SoftwareName.OPERA.value]
#     software_names = [choice(l1)]
#     operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value, OperatingSystem.SUNOS.value]
#     user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=1000)
#     return user_agent_rotator.get_random_user_agent()
#
# headers={
#
#     'authority': 'www.saturn.de',
#     'method':'GET',
#     'scheme': 'https',
#     # 'accept': 'text/html,applicatin/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'accept-language':'en-GB,en-US;q=0.9,en;q=0.8',
#     'cache-control': 'no-cache',
#     # 'cookie': 'optid=3d8c3824-eb71-4464-86e3-06285ac19494; a=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im8yc2lnbiJ9.eyJzdWIiOiI2MjM0ZDc5MS00ODBiLTQ1OWQtYmZmYi01ZDdkOTJhMzkxZmIiLCJpc3MiOiJtbXNlIiwiaWF0IjoxNjUzOTE0OTU2LCJleHAiOjE2NTUxMjQ1NTYsImF1ZCI6IndlYm1vYmlsZSIsInQiOiJ1IiwibyI6MTAxNX0.Be1A4HOFRAUp550_K4KL-PZSeh7hQkz_xVsATBqCM7Lm2800tDuOrIPflLW1I-88Kt_VD-VnizK_xVN1Mb4gAojpTVGqSQFhB9_E8gSYdgr97IJ8JPAx6OoMdIa2K4Qrg_IU64fYw4O06eZXlW8WOtqX-WAWggQrOEMyWACmq21nvFwawYM1Jrp6MB2MupKQZ9wCEPiTAa-rjq6ggVSAHr3OSEQGbXlLvMCCRkLp4AvT3JRWOcEBEeq35XDnOdqMLaZPPuFf5yy6nQwPZT8jwTzQi0qOdWPARjIAKcnEXLgpBQqokQFjc13YKIYpaXzXCVcRMl5HSSy01AJ7MqOv1Q; r=yDpWJidQZ+sAySIePPU7VppmdgMRCG8SqQ+xHQgAgcWZ0LDtS1taxiCf7EDV9E1d; pwaconsent=v:1.0~required:1&clf:1,cli:1,gfb:1,gtm:1,jot:1,ocx:1|comfort:1&baz:1,cne:1,fix:1,gfa:1,gfc:1,goa:1,gom:1,grc:1,grv:1,lob:1,opt:1,orc:1,ore:1,prd:1,sen:1,sis:1,spe:1,sst:1,swo:1,twi:1,usw:1,usz:1,yte:1|marketing:1&asm:1,cad:1,cma:1,eam:1,fab:1,fbn:1,gad:1,gam:1,gcm:1,gdv:1,gos:1,gse:1,gst:1,kru:1,msb:1,omp:1,pin:1,ttd:1,twt:1|; _gcl_au=1.1.774652435.1653914961; _gid=GA1.2.541576144.1653914961; _pin_unauth=dWlkPU56azJZVGs0WXpjdFpqVXhOaTAwTlRVekxXRmhZbUl0TVRGa04yRXpOamxsTW1WbA; NoCookie=true; t_fpd=true; s_id=f0751285-9373-405f-8cf5-64c3757331a6; MC_PS_SESSION_ID=f0751285-9373-405f-8cf5-64c3757331a6; p_id=f0751285-9373-405f-8cf5-64c3757331a6; MC_PS_USER_ID=f0751285-9373-405f-8cf5-64c3757331a6; __cfruid=4d814b86914410e679ff531751b35c8c4325a56d-1654148724; _clck=16zo6gw|1|f1z|0; ts_id=53ba3848-7f66-4e6e-a8ad-b6ba12b3a6c6; _msbps=95; __cf_bm=42Xg6ru12HcHIaxM_Xj7FH0VKQ6a98YVqnWOYKLXBEs-1654159670-0-ASjrpq9erEVTW3m9I2WZagTikMQjkZhZ+WtLOdcnTWf7ZJ1Dg3vlJ/o+sX1rKhS6j0f1QFhIOz/+oEk8FvR5P1CWG5Yey8DgzWquvG/qWXR1; lux_uid=165416010751407882; _dc_gtm_UA-25101917-1=1; _ga=GA1.1.639b70cf-d794-475c-8297-dba226e2f1b7; _ga_9ZJL7DLSGD=GS1.1.1654160108.25.0.1654160108.60; _uetsid=ecea1860e01611ec90c8b763030d21d4; _uetvid=ecea33f0e01611ec901847a194851ed5; BVBRANDID=edfb344a-dffd-4ba6-88ac-b3ce38a334a4; BVBRANDSID=cfa982a5-202e-49e0-8624-1d4db7e6d83c; _clsk=1q01wa|1654160114076|1|1|a.clarity.ms/collect',
#     'pragma': 'no-cache',
#     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'none',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': get_useragent(),
#
# }
#
# proxy_host = "proxy.zyte.com"
# proxy_port = "8011"
# proxy_auth = "6500c987aae7435a90c249b35b1c9376:"
# proxies = {"https": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port),
#            "http": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port)}
#
# # luminati_proxy_us = {
# #         "https": f"lum-customer-c_11e7173f-zone-zone_us:mqy4l03550gl@zproxy.lum-superproxy.io:22225",
# #         "http": f"lum-customer-c_11e7173f-zone-zone_us:mqy4l03550gl@zproxy.lum-superproxy.io:22225"}
#
#
#
# class JSpiderSpider(scrapy.Spider):
#     name = 'monitor_product'
#     F_PATH = HTML
#
#     handle_httpstatus_list = [503, 429]
#     RETRY_HTTP_CODES = [429, 403]
#
#     def __init__(self, start='', end=''):
#         try:
#             self.cursor = UgamSaturnDePipeline.cursor
#             self.con = UgamSaturnDePipeline.con
#             self.start = start
#             self.end = end
#         except Exception as e:
#             print('exception in __init__ method main:{}'.format(e))
#
#
#     def start_requests(self):
#
#         try:
#             # select_query = f"SELECT id,`Product URL`,`category_url`, `cat_rank`,`cat_id` FROM {data_table} WHERE Status = 'Pending' AND ID BETWEEN {self.start} AND {self.end}"
#             sql_query = f"select id, `Product URL`, HtmlPath, cat_id, HtmlPath_search, category_url, cat_rank from {db_data_table} where Status = 'Pending' AND ID BETWEEN {self.start} AND {self.end}"
#             self.cursor.execute(sql_query)
#             core_list = [column for column in self.cursor.fetchall()]
#             for itm in core_list:
#                 time.sleep(1)
#
#                 row_id = itm[0]
#                 product_url = itm[1]
#                 HtmlPath = itm[2]
#                 cat_id = itm[3]
#                 HtmlPath_search = itm[4]
#                 category_url = itm[5]
#                 cat_rank = itm[6]
#
#                 nw_product_id = c_replace(product_url.split('-')[-1])
#                 product_id=nw_product_id.split('.')[0]
#                 # print(nw_product_id)
#                 filename = f'/{product_id}.html'
#                 path = self.F_PATH + filename
#                 path = path.replace("\\", "/")
#
#                 # delete_duplicate_row = catpdp.delete_category_Query()
#                 # print(delete_duplicate_row)
#                 # self.cursor.execute(delete_duplicate_row)
#                 # self.con.commit()
#
#                 meta_dict = {
#                              'product_url': product_url,
#                              'row_id': row_id,
#                              'HtmlPath_search': HtmlPath_search,
#                              'category_url': category_url,
#                              'cat_rank': cat_rank,
#                              'product_id': product_id,
#                              'cat_id': cat_id
#
#                              }
#
#                 if os.path.exists(path):
#                     with open(path, "r", encoding="utf-8")as f:
#                         reviewbody = f.read()
#                         re_text1 = reviewbody
#                 else:
#                     # print(url_zipcode)
#                     re = requests.get(url=product_url, headers=headers, verify=False, proxies=proxies)
#                     re_text1 = re.text
#                     while re.status_code != 200:
#                         print("Review Response issue re-request ")
#                         re = requests.get(url=product_url, headers=headers, verify=False, proxies=proxies)
#                         re_text1 = re.text
#                         with open(path, 'w', encoding="utf-8") as f:
#                             f.write(re_text1)
#                         time.sleep(3)
#                     with open(path, 'w', encoding="utf-8") as f:
#                         f.write(re_text1)
#
#                 if os.path.exists(path):
#                     yield scrapy.FormRequest(url=f'file:///{path}',headers=headers,callback=self.parse, meta={'meta_dict': meta_dict})
#
#
#         except Exception as e:
#             print(e)
#
#     def parse(self, response, **kwargs):
#
#         print("Status",response.status)
#
#         try:
#             # todo ------------------------------- NOTFOUND ----------------------------
#             if "Not Found" in response.text:
#
#                 print("Product Not found, Status code:{}".format(response.status))
#                 meta_dict = response.meta.get('meta_dict')
#                 row_id = meta_dict.get('row_id')
#
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
#                 updateproduct_q = catpdp.Update_productdata_Query()
#                 # print(updateproduct)
#                 self.cursor.execute(updateproduct_q)
#                 self.con.commit()
#
#             elif "</html>" in str(response.body):
#
#                 catpdp.intialize_variable()
#                 meta_dict = response.meta.get('meta_dict')
#                 row_id = meta_dict.get('row_id')
#                 HtmlPath_search = meta_dict.get('HtmlPath_search')
#                 cat_id = meta_dict.get('cat_id')
#                 # Product_URL = response.meta.get('Product_URL')
#                 cat_rank = meta_dict.get('cat_rank')
#                 Product_URL = meta_dict.get('product_url')
#                 print("------Product_URL:",Product_URL)
#                 category_url = meta_dict.get('category_url')
#
#                 nw_product_id = c_replace(Product_URL.split('-')[-1])
#                 product_id = nw_product_id.split('.')[0]
#
#
#                 if len(product_id) > 7:
#                     prod_id = Product_URL.split(".", -1)[-2].split("-", -1)[-1]
#                 else:
#                     prod_id = product_id
#
#                 filename = f'/{prod_id}.html'
#                 path = self.F_PATH + filename
#                 path = path.replace("\\", "/")
#
#
#                 if not os.path.exists(path):
#                     with open(path, "w",encoding='utf-8') as f:
#                         f.write(response.text)
#
#                 #Todo: end....
#
#                 #TODO ----------------------- PRICE --------------------------------
#
#                 main_json = response.xpath('//script[contains(text(),"__PRELOADED_STATE__ ")]//text()').get()
#                 print("jsonresponse...........",main_json)
#                 if main_json:
#                     main_json_1 =main_json.replace('window.__PRELOADED_STATE__ = ','').replace(';','')
#                     j_data = json.loads(main_json_1)
#                     print(".....FINAL JSON...!",j_data)
#
#                     pro_jason = j_data['apolloState']
#                     #apolloState.GraphqlProduct:2723592.title
#                     name = pro_jason[f'GraphqlProduct:{prod_id}']['title']
#                     print("Title Name....",name)
#                     product_title = c_replace(name)
#                     #price({"id":"2723592"})
#                     price_data = pro_jason['ROOT_QUERY']
#
#                     # TODO --------------- LEADTIME --------------
#                     leadtime = ''
#                     for s in price_data:
#                         if 'availability' in str(s):
#                             leadtime = s
#                             break
#                     try:
#                         leadtime = pro_jason['ROOT_QUERY'][leadtime]['delivery']['latest']
#                         print(leadtime)
#                         catpdp.Lead_space_time = leadtime
#
#                     except Exception as e:
#                         print(e)
#                         catpdp.Lead_space_time = "n/a"
#
#
#                     # TODO ----------------- PRICE ----------------
#                     key = ''
#                     for i in price_data:
#                         if 'price' in str(i):
#                             key = i
#                             break
#
#                     try:
#                         price = pro_jason ['ROOT_QUERY'][key]['price']
#                         regular_price = pro_jason ['ROOT_QUERY'][key]['strikePrice']
#                         final_price = c_replace(str(price))
#                         if regular_price is not None:
#                             regular_price = c_replace(str(regular_price))
#                         else:
#                             regular_price = 'n/a'
#                         print(" FINAL PRICE", final_price)
#                         print(" Regular Price", regular_price)
#                     except:
#                         final_price = 'n/a'
#                         regular_price = 'n/a'
#
#                     # TODO ------------------- First_description -----------------------------
#
#                     try:
#                         try:
#                             First_des = pro_jason[f'GraphqlProduct:{prod_id}']['content']['infoTeaser']['secondParagraph'][0]['json']['content'][0]['content'][0]['value']
#                         except:
#                             First_des = ''
#                         First_des = c_replace(First_des)
#                         print("FIRST_DESC", First_des)
#                         try:
#                             description = pro_jason[f'GraphqlProduct:{prod_id}']['description']
#                             if description == None:
#                                 description=''
#                         except:
#                             description = ''
#
#                         print("Secound_Desc", description)
#                         if First_des !='' or description !='':
#                             description = c_replace(description)
#                             Final_Descriptions = First_des + description
#                         else:
#                             Final_Descriptions = description
#
#                         if Final_Descriptions=='':
#                             product_description="n/a"
#                         else:
#                             product_description=Final_Descriptions
#                     except:
#                         product_description = 'n/a'
#                         print("PRODUCT_DEC", product_description)
#
#                     # todo ----------------- IMAGE URL ---------------------------------------
#
#                     try:
#                         # Image = pro_jason[f'GraphqlProduct:{prod_id}']['assets'][0]['link'] #apolloState.GraphqlProduct:2723592.assets[0].link
#                         Image = pro_jason[f'GraphqlProduct:{prod_id}']['titleImageId'] #apolloState.GraphqlProduct:2723592.assets[0].link
#                         final_image = f'https://assets.mmsrg.com/isr/166325/c1/-/{Image}'
#                         product_image = final_image
#                         print('PRODUCT URL', product_image)
#
#                     except Exception as  e:
#                         print(e)
#
#                     # TODO --------------------  Specifications ------------------------------------
#
#                     #TEcnical_details = apolloState.GraphqlProduct:2723592.featureGroups[0].features[0].name
#                     tech = pro_jason[f'GraphqlProduct:{prod_id}']['featureGroups']
#                     print(tech)
#                     key_list = []
#                     value_list = []
#                     for a in tech:
#                         features_1 = a['features']
#                         # print("features_1 is hear", features_1)
#                         for b in features_1:
#                             features_key = b['name']
#                             features_value = b['value']
#                             key = features_key
#                             try:
#                                 features_unit = b['unit']
#                             except:
#                                 features_unit = ""
#                             key_list.append(key)
#                             if features_unit:
#                                 value = features_value+" "+features_unit
#                             else:
#                                 value = features_value
#                             value_list.append(value)
#                             # print("KEYS ..... key is here",key)
#
#
#                     tech_dict = dict(zip(key_list, value_list))
#                     tech_details = []
#                     for k, v in tech_dict.items():
#                         tech_details.append(f'{k}:{v}')
#                     exact_tech = '#||#'.join(tech_details)
#                     technical_details = c_replace(exact_tech)
#                     print("Spec ",technical_details)
#
#                     # TODO ------------------- AVAILABILITY ------------------------
#
#                     Avaiblity = response.xpath('//script[contains(text(),"availability")]//text()').get()
#                     print("Availability",Avaiblity)
#                     if Avaiblity:
#                         try:
#                             Avaiblity_ = json.loads(Avaiblity)
#                             on_off = Avaiblity_['offers']['availability']
#                             on_off = on_off.split('/')[-1]
#                             stock_availability = c_replace(on_off)
#                             if stock_availability=="InStock":
#                                 stock_availability="In Stock"
#                             else:
#                                 stock_availability="Out of stock"
#
#                             print("stock_avialability ",stock_availability)
#
#                             brand = Avaiblity_['brand']['name']
#                             print("BRAND ", brand)
#                         except:
#                             stock_availability = 'Out of stock'
#                             brand = product_title.split()[0]
#                             print("BRAND", brand)
#                     else:
#                         stock_availability = 'Out of stock'
#                         brand = product_title.split()[0]
#                         print("BRAND",brand)
#
#                     # TODO --------------------  MPN  -----------------------------------
#
#                     try:
#                         tech1 = pro_jason[f'GraphqlProduct:{prod_id}']['featureGroups']
#                         print(tech1)
#                         final = {}
#                         for a in tech1:
#                             features_1 = a['features']
#                             for b in features_1:
#                                 name = b['name']
#                                 value = b['value']
#                                 mpn_d={name:value}
#                                 final.update(mpn_d)
#                         mpn=final.get('Modelkennung')
#                         print(final)
#                         print(mpn)
#
#                         if mpn==None:
#                             catpdp.MPN=str("n/a")
#                         else:
#                             catpdp.MPN=mpn
#
#                     except Exception as e:
#                         logger.error("Error in scrape header MPN : {}".format(e))
#                         return None
#
#                     # apolloState.ROOT_QUERY.pwaFooter.legalText.json.content[2].content[0].value
#                     catpdp.category_url = c_replace(category_url)
#                     catpdp.status = "Done"
#                     # catpdp.MPN=c_replace(mpn)
#                     catpdp.Condition = 'n/a'
#                     catpdp.Brand = brand
#                     catpdp.category_url = meta_dict.get('category_url')
#                     catpdp.warrenty = 'n/a'
#                     catpdp.Seller_space_Name = 'n/a'
#                     # catpdp.Lead_space_time="n/a"
#                     catpdp.htmlpath = path
#                     catpdp.HtmlPath_search = HtmlPath_search
#                     date = datetime.today().strftime('%m/%d/%Y %H:%M:%S %p')
#                     catpdp.Date_space_of_space_Crawl = str(date)
#                     catpdp.Retailer = "Saturn.de"
#                     catpdp.cat_row_id = str(cat_id)
#                     catpdp.cat_rank = str(cat_rank)
#                     catpdp.Product_space_ID = c_replace(str(prod_id))
#                     catpdp.Product_space_Title = c_replace(product_title)
#                     catpdp.Product_space_URL = c_replace(Product_URL)
#                     catpdp.List_space_Price = c_replace(regular_price)
#                     catpdp.Markdown_space_Price = c_replace(str(final_price))
#                     catpdp.Stock_space_Status = stock_availability
#                     catpdp.Stock_space_Message="n/a"
#                     catpdp.Product_space_Description=product_description
#                     catpdp.Product_space_Specification = c_replace(technical_details)
#                     catpdp.Product_space_Features = 'n/a'
#                     catpdp.Image_space_URL = c_replace(product_image)
#                     updateproduct_q = catpdp.Update_productdata_Query()
#                     print(updateproduct_q)
#                     try:
#                         updateproduct_q=catpdp.Update_productdata_Query()
#                         print(updateproduct_q)
#                         print("-----------NEXT URL---------------")
#                         self.cursor.execute(updateproduct_q)
#                         self.con.commit()
#                     except Exception as e:
#                         print(e)
#
#                 else:
#                     print("something went wrong, check properly.........")
#                     logger.info("something went wrong, check properly.........")
#                     return None
#
#         except Exception as e:
#             print(e)
#
#             catpdp.status = "Not Found"
#
#             catpdp.MPN="n/a"
#
#             catpdp.Condition = 'n/a'
#
#             catpdp.Brand = "n/a"
#
#             catpdp.category_url = meta_dict.get('category_url')
#
#             catpdp.warrenty = 'n/a'
#
#             catpdp.Seller_space_Name = 'n/a'
#
#             catpdp.Lead_space_time = "n/a"
#
#             catpdp.htmlpath = path
#
#             catpdp.HtmlPath_search = HtmlPath_search
#
#             date = datetime.today().strftime('%m/%d/%Y %H:%M:%S %p')
#
#             catpdp.Date_space_of_space_Crawl = str(date)
#
#             catpdp.Retailer = "Saturn.de"
#
#             catpdp.cat_row_id = str(cat_id)
#
#             catpdp.cat_rank = str(cat_rank)
#
#             catpdp.Product_space_ID = "n/a"
#
#             catpdp.Product_space_Title = "n/a"
#
#             catpdp.Product_space_URL = Product_URL
#
#             catpdp.List_space_Price = "n/a"
#
#             catpdp.Markdown_space_Price = "n/a"
#
#             catpdp.Stock_space_Status = "Out of stock"
#             catpdp.Stock_space_Message = "n/a"
#
#             catpdp.Product_space_Description ="n/a"
#
#             catpdp.Product_space_Specification = "n/a"
#             catpdp.Product_space_Features = 'n/a'
#             catpdp.Image_space_URL = "n/a"
#
#             updateproduct_q = catpdp.Update_productdata_Query()
#             print(updateproduct_q)
#             print("-----------NEXT URL---------------")
#             self.cursor.execute(updateproduct_q)
#             self.con.commit()
#
#     def close(spider, reason):
#
#         try:
#             sql = f"SELECT id FROM {db_data_table} where status='Pending'"
#             brand_pend = f"SELECT id FROM {db_category_table} where status='Pending'"
#             cursor = UgamSaturnDePipeline.cursor
#             cursor.execute(sql)
#             linkdata_row = cursor.fetchall()
#             cursor.execute(brand_pend)
#             brand_row = cursor.fetchall()
#
#             if linkdata_row == () and brand_row == ():
#                 print('spider is close,...................')
#                 print('going on QA and make csv..............')
#                 print("Going to make CSV..")
#                 from ugam_saturn_de.export_tsv import Export_Csv
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
#
# if __name__ == '__main__':
#     from scrapy.cmdline import execute
#     execute('scrapy crawl monitor_product -a start=15 -a end=15'.split())