# # import requests
# # import json
# # import scrapy
# #
# #
# #
# #
# # class Test_resepnes(scrapy.Spider):
# #     name = 'test_file'
# #     header = {
# #         'authority': 'www.saturn.de',
# #         'method': 'GET',
# #         'path': '/api/v1/graphql?operationName=CategoryV4&variables=%7B%22hasMarketplace%22%3Atrue%2C%22maxNumberOfAds%22%3A2%2C%22isRequestSponsoredSearch%22%3Atrue%2C%22isDemonstrationModelAvailabilityActive%22%3Afalse%2C%22withMarketingInfos%22%3Afalse%2C%22filters%22%3A%5B%5D%2C%22pimCode%22%3A%22CAT_DE_SAT_66%22%2C%22page%22%3A1%2C%22experiment%22%3A%22mp%22%2C%22sessionId%22%3A%22639b70cf-d794-475c-8297-dba226e2f1b7%22%2C%22customerId%22%3A%22639b70cf-d794-475c-8297-dba226e2f1b7%22%2C%22pageType%22%3A%22Category%22%2C%22productFilters%22%3A%5B%5D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%226d8e4ac5962c0673f5df27e5e8939e2fcd4270227dffc0ff2772c5337a149192%22%7D%2C%22pwa%22%3A%7B%22salesLine%22%3A%22Saturn%22%2C%22country%22%3A%22DE%22%2C%22language%22%3A%22de%22%7D%7D',
# #         'scheme': 'https',
# #         'accept': '*/*',
# #         # 'accept-encoding': 'gzip, deflate, br',
# #         'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
# #         'apollographql-client-name': 'pwa-client',
# #         'apollographql-client-version': '1.79.0',
# #         'content-type': 'application/json',
# #         'cookie': 'optid=3d8c3824-eb71-4464-86e3-06285ac19494; a=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im8yc2lnbiJ9.eyJzdWIiOiI2MjM0ZDc5MS00ODBiLTQ1OWQtYmZmYi01ZDdkOTJhMzkxZmIiLCJpc3MiOiJtbXNlIiwiaWF0IjoxNjUzOTE0OTU2LCJleHAiOjE2NTUxMjQ1NTYsImF1ZCI6IndlYm1vYmlsZSIsInQiOiJ1IiwibyI6MTAxNX0.Be1A4HOFRAUp550_K4KL-PZSeh7hQkz_xVsATBqCM7Lm2800tDuOrIPflLW1I-88Kt_VD-VnizK_xVN1Mb4gAojpTVGqSQFhB9_E8gSYdgr97IJ8JPAx6OoMdIa2K4Qrg_IU64fYw4O06eZXlW8WOtqX-WAWggQrOEMyWACmq21nvFwawYM1Jrp6MB2MupKQZ9wCEPiTAa-rjq6ggVSAHr3OSEQGbXlLvMCCRkLp4AvT3JRWOcEBEeq35XDnOdqMLaZPPuFf5yy6nQwPZT8jwTzQi0qOdWPARjIAKcnEXLgpBQqokQFjc13YKIYpaXzXCVcRMl5HSSy01AJ7MqOv1Q; r=yDpWJidQZ+sAySIePPU7VppmdgMRCG8SqQ+xHQgAgcWZ0LDtS1taxiCf7EDV9E1d; pwaconsent=v:1.0~required:1&clf:1,cli:1,gfb:1,gtm:1,jot:1,ocx:1|comfort:1&baz:1,cne:1,fix:1,gfa:1,gfc:1,goa:1,gom:1,grc:1,grv:1,lob:1,opt:1,orc:1,ore:1,prd:1,sen:1,sis:1,spe:1,sst:1,swo:1,twi:1,usw:1,usz:1,yte:1|marketing:1&asm:1,cad:1,cma:1,eam:1,fab:1,fbn:1,gad:1,gam:1,gcm:1,gdv:1,gos:1,gse:1,gst:1,kru:1,msb:1,omp:1,pin:1,ttd:1,twt:1|; _gcl_au=1.1.774652435.1653914961; _gid=GA1.2.541576144.1653914961; _pin_unauth=dWlkPU56azJZVGs0WXpjdFpqVXhOaTAwTlRVekxXRmhZbUl0TVRGa04yRXpOamxsTW1WbA; __cf_bm=nC.KeDREtIq0CxYIHSInxhV_84MbsvUsXXQaXUqDqPA-1653970033-0-AW06xZCbiIVaU7ZgDC36R1Eu6qBzkcZRZR260zxWeYe1HtKIO/pkwiNWuggvTA7MUVqC+zmCxCb5qsQlRvQ7OwmIvY4L/aPSTAtpZyPPAOAG; ts_id=68be962d-2906-47b4-82c1-13903b48064b; abhomeab=B; s_id=58ba4561-c122-48f4-b3d5-a0e2ea87dc7d; MC_PS_SESSION_ID=58ba4561-c122-48f4-b3d5-a0e2ea87dc7d; p_id=58ba4561-c122-48f4-b3d5-a0e2ea87dc7d; MC_PS_USER_ID=58ba4561-c122-48f4-b3d5-a0e2ea87dc7d; t_fpd=true; __cfruid=1a5cda8ed42dc9c35762d5646377d4bd0c7fd7ae-1653970038; lux_uid=165397003906229078; NoCookie=true; BVBRANDID=4273feeb-df0a-4fe1-ab57-884a32c2add2; BVBRANDSID=4524fb21-3e50-4ee4-8920-0ae933a45fb7; _clck=16zo6gw|1|f1x|0; _msbps=98; _ga=GA1.2.639b70cf-d794-475c-8297-dba226e2f1b7; _uetsid=ecea1860e01611ec90c8b763030d21d4; _uetvid=ecea33f0e01611ec901847a194851ed5; _clsk=1cxfqbu|1653970107569|1|0|e.clarity.ms/collect; _ga_9ZJL7DLSGD=GS1.1.1653970040.9.1.1653970115.60',
# #         'referer': 'https://www.saturn.de/de/category/laptops-66.html?ga_query=laptop&ga_queryHash=5eec0dc419aa8337bf725f026fda9c78c1cb1c642eeaff9d6e1112f37783e942&ga_queryRequestId=5eec0dc419aa8337bf725f026fda9c78c1cb1c642eeaff9d6e1112f37783e942',
# #         'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
# #         'sec-ch-ua-mobile': '?0',
# #         'ec-ch-ua-platform': '"Windows"',
# #         'sec-fetch-dest': 'empty',
# #         'ec-fetch-mode': 'cors',
# #         'sec-fetch-site': 'same-origin',
# #         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
# #         'x-cacheable': 'true',
# #         'x-flow-id': '84091fd5-796c-45dd-9b51-c7708d79caa2',
# #         'x-mms-country': 'DE',
# #         'x-mms-language': 'de',
# #         'x-mms-salesline': 'Saturn',
# #         'x-operation': 'CategoryV4'
# #     }
# #
# #     def start_requests(self):
# #
# #
# #         page_no=1
# #         for i in range(1,11):
# #             url='https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_5197","page":pageno,"experiment":"mp","sessionId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","customerId":"69ecb800-76e8-4ca4-864b-aaae21efda0b","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"be8d5bf908c10bee725d49531ef357bd55c44ff67d0eb9b8412b54b29f033919"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'
# #             url1 = url.replace('pageno', str(page_no))
# #             page_no += 1
# #
# #         proxy_host = "proxy.zyte.com"
# #         proxy_port = "8011"
# #         proxy_auth = "6500c987aae7435a90c249b35b1c9376:"
# #         proxies = {"https": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port),
# #                     "http": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port)}
# #
# #         re=requests.get(url=url1,
# #                         headers=self.header,
# #                         proxies=proxies,
# #                         verify=False
# #                         )
# #         with open('page1.html','w')as f:
# #             f.write(re.text)
# #
# #
# #     def parse(self, response, **kwargs):
# #         print(response.status)
# #
# #
# # if __name__ == '__main__':
# #     from scrapy.cmdline import execute
# #     execute('scrapy crawl test_file'.split())
#
# if re.reuest.get=="STATUS==200":
#     GET==="dONE"
# else:
#     GET=="Not Done"
#
