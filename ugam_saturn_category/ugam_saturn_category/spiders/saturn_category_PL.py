import requests
import random
import scrapy
from ugam_saturn_category.config import *
from ugam_saturn_category.pipelines import *
import pymysql
import json
import requests
from random_user_agent.params import SoftwareName, OperatingSystem
from random_user_agent.user_agent import UserAgent
from random import choice
import time
from ugam_saturn_category.header_all import *

def get_useragent():
    l1 = [SoftwareName.CHROME.value, SoftwareName.FIREFOX.value, SoftwareName.OPERA.value]
    software_names = [choice(l1)]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value, OperatingSystem.SUNOS.value]
    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=1000)
    return user_agent_rotator.get_random_user_agent()


class Ugame_saturn_de(scrapy.Spider):
    name = 'santurn_de_category'
    F_PATH = HTML

    # TODO ------------------- HEADERS ------------------------------
    # headers={
    #
    #     'authority': 'www.saturn.de',
    #     'method': 'GET',
    #     'path': '/api/v1/graphql?operationName=CategoryV4&variables=%7B%22hasMarketplace%22%3Atrue%2C%22maxNumberOfAds%22%3A2%2C%22isRequestSponsoredSearch%22%3Atrue%2C%22isDemonstrationModelAvailabilityActive%22%3Afalse%2C%22withMarketingInfos%22%3Afalse%2C%22filters%22%3A%5B%5D%2C%22pimCode%22%3A%22CAT_DE_SAT_2582%22%2C%22page%22%3A1%2C%22experiment%22%3A%22mp%22%2C%22sessionId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22customerId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22pageType%22%3A%22Category%22%2C%22productFilters%22%3A%5B%5D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%22e32ccad3bd5aa0781a4e27cf31af311d7936e6513719045adc070371710afa4c%22%7D%2C%22pwa%22%3A%7B%22salesLine%22%3A%22Saturn%22%2C%22country%22%3A%22DE%22%2C%22language%22%3A%22de%22%2C%22ccr%22%3Atrue%7D%7D',
    #     'scheme': 'https',
    #     'accept': '*/*',
    #     'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    #     'apollographql-client-name': 'pwa-client',
    #     'apollographql-client-version': '1.79.0',
    #     'cache-control': 'no-cache',
    #     'content-type': 'application/json',
    #     'cookie': 'optid=0e26086e-b797-4ce7-b30a-c51085ddc0a7; pwaconsent=v:1.0~required:1&clf:1,cli:1,gfb:1,gtm:1,jot:1,ocx:1|comfort:1&baz:1,cne:1,fix:1,gfa:1,gfc:1,goa:1,gom:1,grc:1,grv:1,lob:1,opt:1,orc:1,ore:1,prd:1,sen:1,sis:1,spe:1,sst:1,swo:1,twi:1,usw:1,usz:1,yte:1|marketing:1&asm:1,cad:1,cma:1,eam:1,fab:1,fbn:1,gad:1,gam:1,gcm:1,gdv:1,gos:1,gse:1,gst:1,kru:1,msb:1,omp:1,pin:1,ttd:1,twt:1|; _gcl_au=1.1.2080703172.1654864663; NoCookie=true; _pin_unauth=dWlkPU5ERXhaVE5pWTJZdFpEaGtPQzAwTURVM0xXRTFZemt0WWpSalpXTTNZVEUyTW1SbQ; cf_clearance=SA_u608X7uLRJs_vMu6xpDUPoner9KWCF01LAfoUiEY-1655299743-0-1-3b6693ae.23026482.6c67cc4e-150; _gid=GA1.2.1270608410.1655882585; a=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im8yc2lnbiJ9.eyJzdWIiOiJlZmYxNGY0NC1iZmYzLTRiMDMtOTY1Mi02YjUzMTMwYjA5YWEiLCJpc3MiOiJtbXNlIiwiaWF0IjoxNjU1OTY2OTYyLCJleHAiOjE2NTcxNzY1NjIsImF1ZCI6IndlYm1vYmlsZSIsInQiOiJ1IiwibyI6MTAxNX0.AL8qpjEkEiEuo20P67EsysB2oTrr_bOCNmw8hKz-I127-11AO3R4G2vcThwQsLjDmlI3HNW3dLuH1bcAxFGX_ybV2ZaTeUxd31HVgW89eKGXDkHEda8xU-lT8iADo6vrbErd6UN8RtyLDk3uhr_7KsWkVngyhbcLGFRtrs12dzuyH6Cdrl4oEbnql1-171nbKlJPexazt5Ea0j-XOnPYaTLfnpSufyb81zZMwKSNYxJPtPoFDz5YrWD84gV9ixfZIQ3lE4ICsn8CLY7_JlhjTOfnR5UbSFQ139EI7oH1APhWw1RY-U9l-VyoVUp3wS6CCiy-uh3neW2kB7jV0C3cTQ; r=SNNEXcEnxhvmK5iUOgWI73bkZ7RdPm6DnIEAxl9L66oRUN9l26wXWK0VWUQBAEam; BVBRANDID=d6ed1941-5d54-4cc5-b733-73b53a05572a; __cf_bm=JCwwYLe0KnUk6LKOXMYNJubKY3Ip3zjJ7HGCYjb.euk-1656047477-0-AcOWd+6O+b40dTIEfqfVJEAsZf8NMFKaLDhGLjR5F0Lr1jyiktDMsPt3tUS41+CMbqOb4ZoCaLSBtG6ZCSGNQfTP0kffe4pW0hvLh70ZHIJO; ts_id=3eae2cf6-d91d-4a19-a703-3d03c82578a1; t_fpd=true; s_id=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; MC_PS_SESSION_ID=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; p_id=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; MC_PS_USER_ID=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; __cfruid=5ce9277937f35b0509ea571d823a42e90d1feb4c-1656047481; lux_uid=165604748329125097; _ga=GA1.2.69ecb800-76e8-4ca4-864b-aaae21efda0b; _dc_gtm_UA-25101917-1=1; _uetsid=28915a40f1fc11eca7afb9eecc1c579a; _uetvid=24005d80e8ba11ec98bccb532996a8b6; _clck=1vw2yro|1|f2l|0; _clsk=11av6ee|1656047486683|1|1|h.clarity.ms/collect; _ga_9ZJL7DLSGD=GS1.1.1656047483.31.0.1656047513.30; _msbps=98',
    #     'pragma': 'no-cache',
    #     'referer': 'https://www.saturn.de/de/category/gaming-notebooks-2582.html',
    #     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    #     'sec-ch-ua-mobile': '?0',
    #     'sec-ch-ua-platform': '"Windows"',
    #     'sec-fetch-dest': 'empty',
    #     'sec-fetch-mode': 'cors',
    #     'sec-fetch-site': 'same-origin',
    #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    #     'x-cacheable': 'true',
    #     'x-flow-id': '82bd3151-9517-4d84-8589-80941a0f7a6b',
    #     'x-mms-country': 'DE',
    #     'x-mms-language': 'de',
    #     'x-mms-salesline': 'Saturn',
    #     'x-operation': 'CategoryV4',
    # }

    proxy_host = "proxy.zyte.com"
    proxy_port = "8011"
    proxy_auth = "6500c987aae7435a90c249b35b1c9376:"


    proxies = {"https": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port),
               "http": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port)}

    handle_httpstatus_list = [503, 429]
    RETRY_HTTP_CODES = [429, 403]


    def start_requests(self):

        cursor = UgamSaturnCategoryPipeline.cursor
        con = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name)

        try:
            # brand_select = f"-- select Id,Category_url from {db_category_table} where Status = 'Pending' AND ID BETWEEN {self.start} AND {self.end}"
            brand_select = f"select Id,Category_url from {db_category_table} where Status = 'Pending'"
            cursor.execute(brand_select)
            category_list = cursor.fetchall()
            # category_list = [column for column in cursor.fetchall()]

            for cat_item in category_list:
                cat_row_id = cat_item[0]
                cat_url = cat_item[1]

                # TODO  -----delete duplicate data in link data table with brand id----- """
                delete_duplicate_row = f"delete from {db_data_table} where cat_id like {cat_row_id}"
                cursor.execute(delete_duplicate_row)
                con.commit()

                page_no = 1
                meta_dict = {
                    'cat_url': cat_url,
                    'cat_row_id': cat_row_id,
                    'page_no': page_no,
                    'counter': 0,
                }

                if cat_row_id == 1:
                    url = 'https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_2582","page":1,"experiment":"mp","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"e32ccad3bd5aa0781a4e27cf31af311d7936e6513719045adc070371710afa4c"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
                elif cat_row_id == 2:
                    url = 'https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_5197","page":1,"experiment":"mp","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"be8d5bf908c10bee725d49531ef357bd55c44ff67d0eb9b8412b54b29f033919"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
                elif cat_row_id == 3:
                    url = 'https://www.saturn.de/api/v1/graphql?operationName=SearchV4&variables={"hasMarketplace":true,"isRequestSponsoredSearch":true,"maxNumberOfAds":2,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"categoryIds":"CAT_DE_SAT_1","experiment":"mp","filters":["brand:APPLE"],"page":1,"query":"Mac","sessionId":"aa0c43f3-eefe-44ec-a270-852dae0dde21","customerId":"aa0c43f3-eefe-44ec-a270-852dae0dde21","pageType":"Search","productFilters":[["brand:APPLE"]]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"9fb05c43e35132d1652195e729b67ea5bffe51ed3f87338aeaceafd29004b150"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
                elif cat_row_id == 4:
                    url='https://www.saturn.de/api/v1/graphql?operationName=SearchV4&variables=%7B%22hasMarketplace%22%3Atrue%2C%22isRequestSponsoredSearch%22%3Atrue%2C%22maxNumberOfAds%22%3A2%2C%22isDemonstrationModelAvailabilityActive%22%3Afalse%2C%22withMarketingInfos%22%3Afalse%2C%22categoryIds%22%3A%22CAT_DE_SAT_66%22%2C%22experiment%22%3A%22mp%22%2C%22filters%22%3A%5B%22brand%3AAPPLE%22%5D%2C%22page%22%3A1%2C%22query%22%3A%22MacBook%2BPro%20-maus%22%2C%22sessionId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22customerId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22pageType%22%3A%22Search%22%2C%22productFilters%22%3A%5B%5B%22brand%3AAPPLE%22%5D%5D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%223cb930f1763026b9a724d9867a77c7085731d1c4193806a9752db52bf44e3482%22%7D%2C%22pwa%22%3A%7B%22salesLine%22%3A%22Saturn%22%2C%22country%22%3A%22DE%22%2C%22language%22%3A%22de%22%2C%22ccr%22%3Atrue%7D%7D'
                    # url = 'https://www.saturn.de/api/v1/graphql?operationName=SearchV4&variables={"hasMarketplace":true,"isRequestSponsoredSearch":true,"maxNumberOfAds":2,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"categoryIds":"CAT_DE_SAT_66","experiment":"mp","filters":["brand:APPLE"],"page":1,"query":"MacBook+Pro -maus","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Search","productFilters":[["brand:APPLE"]]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"83b9064b116df6b3005cf26e456e99151aa2dc76533cfe4396fb919597eaeadf"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
                elif cat_row_id == 5:
                    url='https://www.saturn.de/api/v1/graphql?operationName=SearchV4&variables=%7B%22hasMarketplace%22%3Atrue%2C%22isRequestSponsoredSearch%22%3Atrue%2C%22maxNumberOfAds%22%3A2%2C%22isDemonstrationModelAvailabilityActive%22%3Afalse%2C%22withMarketingInfos%22%3Afalse%2C%22categoryIds%22%3A%22CAT_DE_SAT_66%22%2C%22experiment%22%3A%22mp%22%2C%22filters%22%3A%5B%22brand%3AAPPLE%22%5D%2C%22page%22%3A1%2C%22query%22%3A%22MacBook%2BAir%20-maus%22%2C%22sessionId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22customerId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22pageType%22%3A%22Search%22%2C%22productFilters%22%3A%5B%5B%22brand%3AAPPLE%22%5D%5D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%223cb930f1763026b9a724d9867a77c7085731d1c4193806a9752db52bf44e3482%22%7D%2C%22pwa%22%3A%7B%22salesLine%22%3A%22Saturn%22%2C%22country%22%3A%22DE%22%2C%22language%22%3A%22de%22%2C%22ccr%22%3Atrue%7D%7D'
                    # url = 'https://www.saturn.de/api/v1/graphql?operationName=SearchV4&variables={"hasMarketplace":true,"isRequestSponsoredSearch":true,"maxNumberOfAds":2,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"categoryIds":"CAT_DE_SAT_66","experiment":"mp","filters":["brand:APPLE"],"page":1,"query":"MacBook+Air -maus","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Search","productFilters":[["brand:APPLE"]]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"3cb930f1763026b9a724d9867a77c7085731d1c4193806a9752db52bf44e3482"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
                elif cat_row_id == 6:
                    url = 'https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_106","page":1,"experiment":"mp","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"be8d5bf908c10bee725d49531ef357bd55c44ff67d0eb9b8412b54b29f033919"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
                elif cat_row_id == 7:
                    url = 'https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_83","page":1,"experiment":"mp","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"be8d5bf908c10bee725d49531ef357bd55c44ff67d0eb9b8412b54b29f033919"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
                elif cat_row_id == 8:
                    url = 'https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_66","page":1,"experiment":"mp","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"be8d5bf908c10bee725d49531ef357bd55c44ff67d0eb9b8412b54b29f033919"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
                elif cat_row_id == 9:
                    url = 'https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_105","page":1,"experiment":"mp","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"be8d5bf908c10bee725d49531ef357bd55c44ff67d0eb9b8412b54b29f033919"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
                else:
                    print('id is not matching.....')
                    logger.error('id is not matching.....')
                    return None

                proxy_host = "proxy.zyte.com"
                proxy_port = "8011"
                proxy_auth =  "6500c987aae7435a90c249b35b1c9376:"
                # proxy_auth1 =  "836fd8e1edb54ecc8ff5231d5eaa9170:"

                proxies = {"https": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port),
                           "http": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port)}

                # luminati_proxy_us = {
                #     "https": f"lum-customer-c_11e7173f-zone-zone_us:33p04eaqxtpu@zproxy.lum-superproxy.io:22225",
                #     "http": f"lum-customer-c_11e7173f-zone-zone_us:33p04eaqxtpu@zproxy.lum-superproxy.io:22225"}

                # self.header['x-requested-with'] = "XMLHttpRequest"
                # self.header['X-Crawlera-Cookies'] = "disable"

                filename = f'/Cat_{cat_row_id}_Page_{page_no}.html'
                path = self.F_PATH + filename
                path = path.replace("\\", "/")
                if os.path.exists(path):
                    pass
                else:
                    # print(url_zipcode)
                    if cat_row_id==1:
                        re = requests.get(url=url, headers=header1,proxies=proxies,verify=False)
                    elif cat_row_id==2:
                        re = requests.get(url=url, headers=header2,proxies=proxies,verify=False)
                    elif cat_row_id == 3:
                        re = requests.get(url=url, headers=header3, proxies=proxies, verify=False)
                    elif cat_row_id == 4:
                        re = requests.get(url=url, headers=header4, proxies=proxies, verify=False)
                    elif cat_row_id == 5:
                        re = requests.get(url=url, headers=header5, proxies=proxies, verify=False)
                    elif cat_row_id == 6:
                        re = requests.get(url=url, headers=header6, proxies=proxies, verify=False)
                    elif cat_row_id == 7:
                        re = requests.get(url=url, headers=header7, proxies=proxies, verify=False)
                    elif cat_row_id == 8:
                        re = requests.get(url=url, headers=header8, proxies=proxies, verify=False)
                    elif cat_row_id == 9:
                        re = requests.get(url=url, headers=header9, proxies=proxies, verify=False)
                    else:
                        pass

                    while re.status_code != 200:
                        print("Review Response issue re-request ")
                        if cat_row_id == 1:
                            re = requests.get(url=url, headers=header1, proxies=proxies, verify=False)
                        elif cat_row_id == 2:
                            re = requests.get(url=url, headers=header2, proxies=proxies, verify=False)
                        elif cat_row_id == 3:
                            re = requests.get(url=url, headers=header3, proxies=proxies, verify=False)
                        elif cat_row_id == 4:
                            re = requests.get(url=url, headers=header4, proxies=proxies, verify=False)
                        elif cat_row_id == 5:
                            re = requests.get(url=url, headers=header5, proxies=proxies, verify=False)
                        elif cat_row_id == 6:
                            re = requests.get(url=url, headers=header6, proxies=proxies, verify=False)
                        elif cat_row_id == 7:
                            re = requests.get(url=url, headers=header7, proxies=proxies, verify=False)
                        elif cat_row_id == 8:
                            re = requests.get(url=url, headers=header8, proxies=proxies, verify=False)
                        elif cat_row_id == 9:
                            re = requests.get(url=url, headers=header9, proxies=proxies, verify=False)
                        else:
                            time.sleep(2)
                            re_text1 = re.text
                            with open(path, 'w', encoding="utf-8") as f:
                                f.write(re_text1)
                            time.sleep(2)
                    else:
                        if os.path.exists(path):
                            pass
                        else:
                            with open(path, 'w', encoding="utf-8") as f:
                                f.write(re.text)
                            time.sleep(2)

                if os.path.exists(path):
                    yield scrapy.FormRequest(url=f'file:///{path}', callback=self.parse,meta={'meta_dict': meta_dict}, dont_filter=True)

        except Exception as e:
            print(e)
            logger.error('exception in start requests method main: {}'.format(e))

    def parse(self, response, **kwargs):

        meta_d = response.meta.get('meta_dict')
        cat_rw_id = meta_d['cat_row_id']

        print(cat_rw_id)
        print("Status", response.status)

        try:
            meta_dict = response.meta.get('meta_dict')
            cat_row_id = meta_dict.get('cat_row_id')
            category_url = meta_dict.get('cat_url')
            page_no = meta_dict.get('page_no')
            counter = meta_dict.get('counter')

            if '{' in response.text and '}' in response.text:
                page_data = json.loads(response.text)

                """ Count """
                if 'searchV4' in response.text:
                    count = page_data['data']['searchV4']['totalProducts']
                else:
                    count = page_data['data']['categoryV4']['totalProducts']

                filename = f'/Cat_{cat_row_id}_Page_{page_no}.html'
                path = self.F_PATH + filename
                path = path.replace("\\", "/")
                if os.path.exists(path):
                    pass
                else:
                    with open(path, 'wb') as f:
                        f.write(response.body)

                Status_Flag = True

                # TODO -----check condition for search page or pagination page data is or not ----- """
                if 'data' in response.text:

                    Exit_Flag = True

                    # TODO -------get product link below for loop---------
                    if 'categoryV4' in response.text:
                        results = page_data['data']['categoryV4']['products']
                    else:
                        results = page_data['data']['searchV4']['products']

                    if 'categoryV4' or 'searchV4' in response.text:

                        for i in results:

                            counter += 1
                            product_url = 'https://www.saturn.de' + i['details']['url']

                            # product_name=i['details']['title']
                            # brand=i['details']['manufacturer']
                            # product_id=i['productId']
                            # ean=i['details']['ean']
                            # markdownprice=i['price']['price']
                            # lead_time=i['availability']['delivery']['latest']
                            # product_description=i['details']['description']

                            HtmlPath_search = str(path)
                            cursor = UgamSaturnCategoryPipeline.cursor
                            con = UgamSaturnCategoryPipeline.con
                            sql = f'INSERT INTO {db_data_table}(`Product URL`,`Category_URL`,`HtmlPath_search`,`cat_id`,`cat_rank`) values("{product_url}","{category_url}","{HtmlPath_search}","{cat_row_id}","{counter}")'
                            cursor.execute(sql)
                            con.commit()
                            print("inserted ..............",count, counter)

                    else:
                        Exit_Flag = False

                    # TODO ...pagination here.... """
                    print(counter)
                    try:
                        if Exit_Flag and counter < count:
                            page_no += 1
                            if cat_row_id == 1:
                                page_link = 'https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_2582","page":pageno,"experiment":"mp","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"be8d5bf908c10bee725d49531ef357bd55c44ff67d0eb9b8412b54b29f033919"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
                                url = page_link.replace('pageno', str(page_no))
                            elif cat_row_id == 2:
                                page_link = 'https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_5197","page":pageno,"experiment":"mp","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"be8d5bf908c10bee725d49531ef357bd55c44ff67d0eb9b8412b54b29f033919"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
                                url = page_link.replace('pageno', str(page_no))
                            elif cat_row_id == 3:
                                page_link = 'https://www.saturn.de/api/v1/graphql?operationName=SearchV4&variables={"hasMarketplace":true,"isRequestSponsoredSearch":true,"maxNumberOfAds":2,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"categoryIds":"CAT_DE_SAT_1","experiment":"mp","filters":["brand:APPLE"],"page":pageno,"query":"Mac","sessionId":"aa0c43f3-eefe-44ec-a270-852dae0dde21","customerId":"aa0c43f3-eefe-44ec-a270-852dae0dde21","pageType":"Search","productFilters":[["brand:APPLE"]]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"9fb05c43e35132d1652195e729b67ea5bffe51ed3f87338aeaceafd29004b150"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
                                url = page_link.replace('pageno', str(page_no))
                            elif cat_row_id == 4:
                                page_link = 'https://www.saturn.de/api/v1/graphql?operationName=SearchV4&variables=%7B%22hasMarketplace%22%3Atrue%2C%22isRequestSponsoredSearch%22%3Atrue%2C%22maxNumberOfAds%22%3A2%2C%22isDemonstrationModelAvailabilityActive%22%3Afalse%2C%22withMarketingInfos%22%3Afalse%2C%22categoryIds%22%3A%22CAT_DE_SAT_66%22%2C%22experiment%22%3A%22mp%22%2C%22filters%22%3A%5B%22brand%3AAPPLE%22%5D%2C%22page%22%3Apageno%2C%22query%22%3A%22MacBook%2BPro%20-maus%22%2C%22sessionId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22customerId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22pageType%22%3A%22Search%22%2C%22productFilters%22%3A%5B%5B%22brand%3AAPPLE%22%5D%5D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%223cb930f1763026b9a724d9867a77c7085731d1c4193806a9752db52bf44e3482%22%7D%2C%22pwa%22%3A%7B%22salesLine%22%3A%22Saturn%22%2C%22country%22%3A%22DE%22%2C%22language%22%3A%22de%22%2C%22ccr%22%3Atrue%7D%7D'
                                url = page_link.replace('pageno', str(page_no))
                            elif cat_row_id == 5:
                                page_link = 'https://www.saturn.de/api/v1/graphql?operationName=SearchV4&variables=%7B%22hasMarketplace%22%3Atrue%2C%22isRequestSponsoredSearch%22%3Atrue%2C%22maxNumberOfAds%22%3A2%2C%22isDemonstrationModelAvailabilityActive%22%3Afalse%2C%22withMarketingInfos%22%3Afalse%2C%22categoryIds%22%3A%22CAT_DE_SAT_66%22%2C%22experiment%22%3A%22mp%22%2C%22filters%22%3A%5B%22brand%3AAPPLE%22%5D%2C%22page%22%3Apageno%2C%22query%22%3A%22MacBook%2BAir%20-maus%22%2C%22sessionId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22customerId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22pageType%22%3A%22Search%22%2C%22productFilters%22%3A%5B%5B%22brand%3AAPPLE%22%5D%5D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%223cb930f1763026b9a724d9867a77c7085731d1c4193806a9752db52bf44e3482%22%7D%2C%22pwa%22%3A%7B%22salesLine%22%3A%22Saturn%22%2C%22country%22%3A%22DE%22%2C%22language%22%3A%22de%22%2C%22ccr%22%3Atrue%7D%7D'
                                # page_link = 'https://www.saturn.de/api/v1/graphql?operationName=SearchV4&variables={"hasMarketplace":true,"isRequestSponsoredSearch":true,"maxNumberOfAds":2,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"categoryIds":"CAT_DE_SAT_66","experiment":"mp","filters":["brand:APPLE"],"page":pageno,"query":"MacBook+Air -maus","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Search","productFilters":[["brand:APPLE"]]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"83b9064b116df6b3005cf26e456e99151aa2dc76533cfe4396fb919597eaeadf"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
                                url = page_link.replace('pageno', str(page_no))
                            elif cat_row_id == 6:
                                page_link = 'https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_106","page":pageno,"experiment":"mp","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"be8d5bf908c10bee725d49531ef357bd55c44ff67d0eb9b8412b54b29f033919"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
                                url = page_link.replace('pageno', str(page_no))
                            elif cat_row_id == 7:
                                page_link = 'https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_83","page":pageno,"experiment":"mp","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"be8d5bf908c10bee725d49531ef357bd55c44ff67d0eb9b8412b54b29f033919"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
                                url = page_link.replace('pageno', str(page_no))
                            elif cat_row_id == 8:
                                page_link = 'https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_66","page":pageno,"experiment":"mp","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"be8d5bf908c10bee725d49531ef357bd55c44ff67d0eb9b8412b54b29f033919"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
                                url = page_link.replace('pageno', str(page_no))
                            elif cat_row_id == 9:
                                page_link = 'https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_105","page":pageno,"experiment":"mp","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"be8d5bf908c10bee725d49531ef357bd55c44ff67d0eb9b8412b54b29f033919"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
                                url = page_link.replace('pageno', str(page_no))
                            else:
                                print('id is not matching.....')
                                logger.error('id is not matching.....')
                                return None

                            # filename = f'/Cat_{cat_row_id}_Page_{page_no}.html'
                            # path = self.F_PATH + filename
                            # path = path.replace("\\", "/")

                            meta_dict = {
                                'cat_row_id': cat_row_id,
                                'page_no': page_no,
                                'cat_url': category_url,
                                'counter': counter,
                            }

                            proxy_host = "proxy.zyte.com"
                            proxy_port = "8011"
                            proxy_auth = "6500c987aae7435a90c249b35b1c9376:"
                            proxies = {"https": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port),
                                       "http": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port)}

                            filename = f'/Cat_{cat_row_id}_Page_{page_no}.html'
                            path = self.F_PATH + filename
                            path = path.replace("\\", "/")
                            if os.path.exists(path):
                               pass
                            else:
                                # print(url_zipcode)
                                if cat_row_id == 1:
                                    re = requests.get(url=url, headers=header1, proxies=proxies, verify=False)
                                elif cat_row_id == 2:
                                    re = requests.get(url=url, headers=header2, proxies=proxies, verify=False)
                                elif cat_row_id == 3:
                                    re = requests.get(url=url, headers=header3, proxies=proxies, verify=False)
                                elif cat_row_id == 4:
                                    re = requests.get(url=url, headers=header4, proxies=proxies, verify=False)
                                elif cat_row_id == 5:
                                    re = requests.get(url=url, headers=header5, proxies=proxies, verify=False)
                                elif cat_row_id == 6:
                                    re = requests.get(url=url, headers=header6, proxies=proxies, verify=False)
                                elif cat_row_id == 7:
                                    re = requests.get(url=url, headers=header7, proxies=proxies, verify=False)
                                elif cat_row_id == 8:
                                    re = requests.get(url=url, headers=header8, proxies=proxies, verify=False)
                                elif cat_row_id == 9:
                                    re = requests.get(url=url, headers=header9, proxies=proxies, verify=False)
                                else:
                                    pass
                                time.sleep(2)
                                re_text1 = re.text
                                while re.status_code != 200:
                                    if count==counter:
                                        break
                                    else:
                                        print("Review Response issue re-request ")
                                        if cat_row_id == 1:
                                            re = requests.get(url=url, headers=header1, proxies=proxies, verify=False)
                                        elif cat_row_id == 2:
                                            re = requests.get(url=url, headers=header2, proxies=proxies, verify=False)
                                        elif cat_row_id == 3:
                                            re = requests.get(url=url, headers=header3, proxies=proxies, verify=False)
                                        elif cat_row_id == 4:
                                            re = requests.get(url=url, headers=header4, proxies=proxies, verify=False)
                                        elif cat_row_id == 5:
                                            re = requests.get(url=url, headers=header5, proxies=proxies, verify=False)
                                        elif cat_row_id == 6:
                                            re = requests.get(url=url, headers=header6, proxies=proxies, verify=False)
                                        elif cat_row_id == 7:
                                            re = requests.get(url=url, headers=header7, proxies=proxies, verify=False)
                                        elif cat_row_id == 8:
                                            re = requests.get(url=url, headers=header8, proxies=proxies, verify=False)
                                        elif cat_row_id == 9:
                                            re = requests.get(url=url, headers=header9, proxies=proxies, verify=False)
                                        time.sleep(3)
                                        re_text1 = re.text
                                        with open(path, 'w', encoding="utf-8") as f:
                                            f.write(re_text1)
                                        time.sleep(1)
                                else:
                                    if os.path.exists(path):
                                        pass
                                    else:
                                        with open(path, 'w', encoding="utf-8") as f:
                                            f.write(re_text1)
                                        time.sleep(1)

                            if os.path.exists(path):
                                yield scrapy.FormRequest(url=f"file:///{path}", callback=self.parse,
                                                         meta={'meta_dict': meta_dict}, dont_filter=True)
                        else:
                            Status_Flag = True
                    except Exception as e:
                        logger.error('exception in parse method for pagination:{}'.format(e))
                else:
                    Status_Flag = False

                # statas flag for brands "Done or Not found"
                cursor = UgamSaturnCategoryPipeline.cursor
                con = UgamSaturnCategoryPipeline.con
                if Status_Flag:
                    branch_sql = f'update {db_category_table} set Status = "Done", Count={counter} where id ="{cat_row_id}"'
                    cursor.execute(branch_sql)
                    con.commit()
                else:

                    branch_sql = f'update {db_category_table} set Status = "Not found", Count={counter} where id ="{cat_row_id}"'
                    cursor.execute(branch_sql)
                    con.commit()
            else:
                print("Wrong page response ..........")
                logger.info("Wrong page response..........")

        except Exception as e:
            print(e)
            logger.error('exception in parse method main: {}'.format(e))

    # def close(spider, reason):
    #     cursor = UgamSaturnDePipeline.cursor
    #     try:
    #         print('spider is close,...................')
    #         # print('going on QA and make csv..............')
    #         cursor.execute('select * from category where status="Pending"')
    #         rows = cursor.fetchall()
    #         if rows == ():
    #             print("Done with category..")
    #         else:
    #             print("Some remaining..")
    #             return None

    #     except Exception as e:
    #         print('close spider error:{}'.format(e))


if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute('scrapy crawl santurn_de_category'.split())






