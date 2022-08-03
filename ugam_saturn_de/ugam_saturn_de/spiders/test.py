from random import random

import requests



header = {
    'authority': 'www.saturn.de',
    'method': 'GET',
    'path': '/api/v1/graphql?operationName=CategoryV4&variables=%7B%22hasMarketplace%22%3Atrue%2C%22maxNumberOfAds%22%3A2%2C%22isRequestSponsoredSearch%22%3Atrue%2C%22isDemonstrationModelAvailabilityActive%22%3Afalse%2C%22withMarketingInfos%22%3Afalse%2C%22filters%22%3A%5B%5D%2C%22pimCode%22%3A%22CAT_DE_SAT_60%22%2C%22page%22%3A1%2C%22experiment%22%3A%22mp%22%2C%22sessionId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22customerId%22%3A%2269ecb800-76e8-4ca4-864b-aaae21efda0b%22%2C%22pageType%22%3A%22Category%22%2C%22productFilters%22%3A%5B%5D%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%22e32ccad3bd5aa0781a4e27cf31af311d7936e6513719045adc070371710afa4c%22%7D%2C%22pwa%22%3A%7B%22salesLine%22%3A%22Saturn%22%2C%22country%22%3A%22DE%22%2C%22language%22%3A%22de%22%2C%22ccr%22%3Atrue%7D%7D',
    'scheme': 'https',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'apollographql-client-name':'pwa-client',
    'apollographql-client-version':'1.79.0',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'cookie': 'optid=0e26086e-b797-4ce7-b30a-c51085ddc0a7; pwaconsent=v:1.0~required:1&clf:1,cli:1,gfb:1,gtm:1,jot:1,ocx:1|comfort:1&baz:1,cne:1,fix:1,gfa:1,gfc:1,goa:1,gom:1,grc:1,grv:1,lob:1,opt:1,orc:1,ore:1,prd:1,sen:1,sis:1,spe:1,sst:1,swo:1,twi:1,usw:1,usz:1,yte:1|marketing:1&asm:1,cad:1,cma:1,eam:1,fab:1,fbn:1,gad:1,gam:1,gcm:1,gdv:1,gos:1,gse:1,gst:1,kru:1,msb:1,omp:1,pin:1,ttd:1,twt:1|; _gcl_au=1.1.2080703172.1654864663; NoCookie=true; _pin_unauth=dWlkPU5ERXhaVE5pWTJZdFpEaGtPQzAwTURVM0xXRTFZemt0WWpSalpXTTNZVEUyTW1SbQ; cf_clearance=SA_u608X7uLRJs_vMu6xpDUPoner9KWCF01LAfoUiEY-1655299743-0-1-3b6693ae.23026482.6c67cc4e-150; _gid=GA1.2.1270608410.1655882585; a=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im8yc2lnbiJ9.eyJzdWIiOiJlZmYxNGY0NC1iZmYzLTRiMDMtOTY1Mi02YjUzMTMwYjA5YWEiLCJpc3MiOiJtbXNlIiwiaWF0IjoxNjU1OTY2OTYyLCJleHAiOjE2NTcxNzY1NjIsImF1ZCI6IndlYm1vYmlsZSIsInQiOiJ1IiwibyI6MTAxNX0.AL8qpjEkEiEuo20P67EsysB2oTrr_bOCNmw8hKz-I127-11AO3R4G2vcThwQsLjDmlI3HNW3dLuH1bcAxFGX_ybV2ZaTeUxd31HVgW89eKGXDkHEda8xU-lT8iADo6vrbErd6UN8RtyLDk3uhr_7KsWkVngyhbcLGFRtrs12dzuyH6Cdrl4oEbnql1-171nbKlJPexazt5Ea0j-XOnPYaTLfnpSufyb81zZMwKSNYxJPtPoFDz5YrWD84gV9ixfZIQ3lE4ICsn8CLY7_JlhjTOfnR5UbSFQ139EI7oH1APhWw1RY-U9l-VyoVUp3wS6CCiy-uh3neW2kB7jV0C3cTQ; r=SNNEXcEnxhvmK5iUOgWI73bkZ7RdPm6DnIEAxl9L66oRUN9l26wXWK0VWUQBAEam; BVBRANDID=d6ed1941-5d54-4cc5-b733-73b53a05572a; t_fpd=true; s_id=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; MC_PS_SESSION_ID=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; p_id=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; MC_PS_USER_ID=0b893bdd-f2b3-42f3-9bb4-def45ef9cb7f; _clck=1vw2yro|1|f2l|0; __cf_bm=cNyU_4t73y1ggzY6HmCPOFyoTrNX05Z0BQMaX7spVj4-1656065414-0-AbHmPGWpGw75Dod8io9XXS4BlxMvbDxfHE6RUKNrJ/N/IMUsyuiQIeXnVQZtvpqZEtO1eqWruHNY9IJYCfrZ6PPc1uAveAD7bujzmjhFkVLp; ts_id=93987c6c-8f1a-4290-9e87-fdfbf492683b; _msbps=92; lux_uid=165606575196243814; __cfruid=4f39bfab2a05ff01ac87f5c3fa49b0e3c141494f-1656065750; _ga=GA1.2.69ecb800-76e8-4ca4-864b-aaae21efda0b; _uetsid=28915a40f1fc11eca7afb9eecc1c579a; _uetvid=24005d80e8ba11ec98bccb532996a8b6; _clsk=1mqdmzk|1656065823753|1|0|f.clarity.ms/collect; _ga_9ZJL7DLSGD=GS1.1.1656065753.34.0.1656065992.60',
    'pragma': 'no-cache',
    'referer': 'https://www.saturn.de/de/category/monitore-60.html',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'x-cacheable': 'true',
    'x-flow-id': 'b1895905-d4df-4a33-9943-eac0778517bb',
    'x-mms-country': 'DE',
    'x-mms-language': 'de',
    'x-mms-salesline': 'Saturn',
    'x-operation': 'CategoryV4',
}

proxy_host = "proxy.zyte.com"
proxy_port = "8011"
proxy_auth = "6500c987aae7435a90c249b35b1c9376:"
proxies = {"https": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port),
           "http": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port)}

# blazing_seo_us2 = {
#     "http": f"anilprajapatixbyteio:tuen4r0o1il-country-vi@la.residential.blazingseollc.com:8000",
#     "https": f"anilprajapatixbyteio:tuen4r0o1il@la.residential.blazingseollc.com:8000"
# }
# blazing_seo_us = {
#     "http": f"anilprajapatixbyteio:tuen4r0o1il-country-us@la.residential.blazingseollc.com:8000",
#     "https": f"anilprajapatixbyteio:tuen4r0o1il@la.residential.blazingseollc.com:8000"
# }
# blazing_seo_us_session = {
#     "http": f"anilprajapatixbyteio:TueN4r0O1Il-country-US-session-ec1fab19@139.180.226.114:8000",
#     "https": f"anilprajapatixbyteio:tuen4r0o1il@la.residential.blazingseollc.com:8000"
# }
# blazing_seo_us2_session = {
#     "http": f"anilprajapatixbyteio:TueN4r0O1Il-country-UM-session-2473d303@139.180.226.114:8000",
#     "https": f"anilprajapatixbyteio:tuen4r0o1il@la.residential.blazingseollc.com:8000"
# }

from random import choice
# proxycoice_ls = [blazing_seo_us2, blazing_seo_us, blazing_seo_us_session, blazing_seo_us2_session]
# proxie = random.choice(proxycoice_ls)

url='https://www.saturn.de/api/v1/graphql?operationName=CategoryV4&variables={"hasMarketplace":true,"maxNumberOfAds":2,"isRequestSponsoredSearch":true,"isDemonstrationModelAvailabilityActive":false,"withMarketingInfos":false,"filters":[],"pimCode":"CAT_DE_SAT_60","page":1,"experiment":"mp","sessionId":"639b70cf-d794-475c-8297-dba226e2f1b7","customerId":"639b70cf-d794-475c-8297-dba226e2f1b7","pageType":"Category","productFilters":[]}&extensions={"persistedQuery":{"version":1,"sha256Hash":"6d8e4ac5962c0673f5df27e5e8939e2fcd4270227dffc0ff2772c5337a149192"},"pwa":{"salesLine":"Saturn","country":"DE","language":"de","ccr":true}}'

luminati_proxy_us = {
    "https": f"lum-customer-c_11e7173f-zone-zone_us:33p04eaqxtpu@zproxy.lum-superproxy.io:22225",
    "http": f"lum-customer-c_11e7173f-zone-zone_us:33p04eaqxtpu@zproxy.lum-superproxy.io:22225"}

#
#
# re=requests.get(url=url,headers=header,proxies=proxies,verify=False)
# print(re.status_code)
