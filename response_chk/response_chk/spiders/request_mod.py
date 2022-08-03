import requests
from random_user_agent.params import SoftwareName, OperatingSystem
from random_user_agent.user_agent import UserAgent
from random import choice


def get_useragent():
    l1 = [SoftwareName.CHROME.value, SoftwareName.FIREFOX.value, SoftwareName.OPERA.value]
    software_names = [choice(l1)]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value, OperatingSystem.SUNOS.value]
    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=1000)

    return user_agent_rotator.get_random_user_agent()

headers={
    'authority': 'www.saturn.de',
    'method': 'GET',
    # 'path': '/de/product/_msi-katana-gf76-11uc-698-gaming-notebook-mit-17-zoll-display-intelr-coretm-i5-prozessor-8-gb-ram-512-gb-ssd-geforce-rtxtm-3050-laptop-gpu-core-black-2784475.html',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'cookie': 'optid=0e26086e-b797-4ce7-b30a-c51085ddc0a7; pwaconsent=v:1.0~required:1&clf:1,cli:1,gfb:1,gtm:1,jot:1,ocx:1|comfort:1&baz:1,cne:1,fix:1,gfa:1,gfc:1,goa:1,gom:1,grc:1,grv:1,lob:1,opt:1,orc:1,ore:1,prd:1,sen:1,sis:1,spe:1,sst:1,swo:1,twi:1,usw:1,usz:1,yte:1|marketing:1&asm:1,cad:1,cma:1,eam:1,fab:1,fbn:1,gad:1,gam:1,gcm:1,gdv:1,gos:1,gse:1,gst:1,kru:1,msb:1,omp:1,pin:1,ttd:1,twt:1|; _gcl_au=1.1.2080703172.1654864663; NoCookie=true; _pin_unauth=dWlkPU5ERXhaVE5pWTJZdFpEaGtPQzAwTURVM0xXRTFZemt0WWpSalpXTTNZVEUyTW1SbQ; cf_clearance=SA_u608X7uLRJs_vMu6xpDUPoner9KWCF01LAfoUiEY-1655299743-0-1-3b6693ae.23026482.6c67cc4e-150; _gid=GA1.2.1270608410.1655882585; t_fpd=true; s_id=4e7ab6e4-c441-4cac-9107-d488bde7ba1f; MC_PS_SESSION_ID=4e7ab6e4-c441-4cac-9107-d488bde7ba1f; p_id=4e7ab6e4-c441-4cac-9107-d488bde7ba1f; MC_PS_USER_ID=4e7ab6e4-c441-4cac-9107-d488bde7ba1f; __cfruid=1f75fe3610e2936d54a94cee361e5d598cb481dd-1655956938; _clck=1vw2yro|1|f2k|0; a=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im8yc2lnbiJ9.eyJzdWIiOiJlZmYxNGY0NC1iZmYzLTRiMDMtOTY1Mi02YjUzMTMwYjA5YWEiLCJpc3MiOiJtbXNlIiwiaWF0IjoxNjU1OTY2OTYyLCJleHAiOjE2NTcxNzY1NjIsImF1ZCI6IndlYm1vYmlsZSIsInQiOiJ1IiwibyI6MTAxNX0.AL8qpjEkEiEuo20P67EsysB2oTrr_bOCNmw8hKz-I127-11AO3R4G2vcThwQsLjDmlI3HNW3dLuH1bcAxFGX_ybV2ZaTeUxd31HVgW89eKGXDkHEda8xU-lT8iADo6vrbErd6UN8RtyLDk3uhr_7KsWkVngyhbcLGFRtrs12dzuyH6Cdrl4oEbnql1-171nbKlJPexazt5Ea0j-XOnPYaTLfnpSufyb81zZMwKSNYxJPtPoFDz5YrWD84gV9ixfZIQ3lE4ICsn8CLY7_JlhjTOfnR5UbSFQ139EI7oH1APhWw1RY-U9l-VyoVUp3wS6CCiy-uh3neW2kB7jV0C3cTQ; r=SNNEXcEnxhvmK5iUOgWI73bkZ7RdPm6DnIEAxl9L66oRUN9l26wXWK0VWUQBAEam; ts_id=e88a4721-59ea-4edf-a71c-ade2b37a80e9; lux_uid=165597610834286177; _msbps=97; _ga_9ZJL7DLSGD=GS1.1.1655976101.28.1.1655977804.60; _uetsid=28915a40f1fc11eca7afb9eecc1c579a; _uetvid=24005d80e8ba11ec98bccb532996a8b6; BVBRANDID=aa7739b1-df48-4092-ab7f-754230de2162; BVBRANDSID=f7369d12-edbd-4fc9-ad72-9651a6ae44f9; _ga=GA1.2.69ecb800-76e8-4ca4-864b-aaae21efda0b; _clsk=k9kbj4|1655977807003|9|1|h.clarity.ms/collect; __cf_bm=v8.NVIgVfEdAPcV06CcyEHAF6QGg3HNDPOwOlFJB6zk-1655977859-0-AaQ974waeeUDUJWntUwUxclj++9gVn7Sionsi4gFblot/Ck5fqwnOW1c3rgZqr3aWekqlRCL7IU+Bx2vjKrg4UtJRXmAE4ws0Je4fTexxmAo',
    'pragma': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': get_useragent()
}

headers1={
    'authority': 'shop.barr-thorp.com',
    'method': 'GET',
    # 'path': '/products/LC1D25M7',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'cookie': 'cf_clearance=KyEDVVZiGgwgTKykomw.eXJuczZv2w1ecCCJZqSmaKw-1655968875-0-150; _kyklo-web_session=6ca3e6eacd4ef6a4d833ccdb7f0dcc36; _ga=GA1.3.437707213.1655968878; _gid=GA1.3.1332018629.1655968878; _gat=1; _hp2_id.2844502186=%7B%22userId%22%3A%227615546074688719%22%2C%22pageviewId%22%3A%222522312805199321%22%2C%22sessionId%22%3A%225750503972900668%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _hp2_ses_props.2844502186=%7B%22ts%22%3A1655980518586%2C%22d%22%3A%22shop.barr-thorp.com%22%2C%22h%22%3A%22%2Fproducts%2FLC1D25M7%22%7D',
    'pragma': 'no-cache',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    # 'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
}


proxy_host = "proxy.zyte.com"
proxy_port = "8011"
proxy_auth = "6500c987aae7435a90c249b35b1c9376:"

proxies = {"https": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port),
            "http": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port)}

proxyle={"https":"lum-customer-c_11e7173f-zone-zone_us:mqy4l03550gl@zproxy.lum-superproxy.io:22225",
         "http":"lum-customer-c_11e7173f-zone-zone_us:mqy4l03550gl@zproxy.lum-superproxy.io:22225"}

url='https://www.saturn.de/de/product/_msi-katana-gf76-11uc-698-gaming-notebook-mit-17-zoll-display-intelr-coretm-i5-prozessor-8-gb-ram-512-gb-ssd-geforce-rtxtm-3050-laptop-gpu-core-black-2784475.html'
url1="https://shop.barr-thorp.com/products/LC1D25M7"
re=requests.get(url=url1,headers=headers1)


print(re.status_code)
# with open('Satunr_pd__11_p.html','w',encoding='utf-8') as f:
#     f.write(re.text)










# import requests
# import json
# header={
#     'Accept': 'application/json; charset=utf-8',
#     # 'Accept-Encoding': 'gzip, deflate, br',
#     'Accept-Language': 'en-US,en;q=0.9',
#     'Connection': 'keep-alive',
#     'Content-Length': '183',
#     'Content-Type': 'application/json; charset=UTF-8',
#     'Cookie': 'JSESSIONID=CE69FA89EA51DD4C0B594C12BF9E75D2.appprd6-1; insight_locale=de_DE; VqVZpDrwmmPSREEOugGm+026cu0C48MYUYGU=v1AdjJgw__1nj; insight_current_locale=de_DE; at_check=true; cr_name=recentlyViewedProducts%3DCF226A; recent_views=%257B%2522recentViews%2522%253A%255B%2522CF226A%2522%255D%257D; _aimtellSubscriberID=b6e61fd5-71f1-ab8b-4a95-65e618d59d21; lastViewedMaterial=CF226A; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Jun+23+2022+15%3A07%3A12+GMT%2B0530+(India+Standard+Time)&version=6.34.0&isIABGlobal=false&hosts=&consentId=5ba8c4a5-9745-4c42-bd47-8f54a97e1ff0&interactionCount=0&landingPath=https%3A%2F%2Fde.insight.com%2Fde_DE%2Fshop%2Fproduct%2FCF226A%2FHEWLETT%2520PACKARD%2520(HP%2520INC)%2FCF226A%2FHP-26A--Schwarz--original--LaserJet--Tonerpatrone-CF226A%2F&groups=C0001%3A1%2CC0002%3A0%2CC0003%3A0%2CC0004%3A0',
#     'Host': 'de.insight.com',
#     'Origin': 'https://de.insight.com',
#     'Referer': 'https://de.insight.com/de_DE/shop/product/CF226A/HEWLETT%20PACKARD%20(HP%20INC)/CF226A/HP-26A--Schwarz--original--LaserJet--Tonerpatrone-CF226A/',
#     'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Microsoft Edge";v="102"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-origin',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44',
#     'X-Requested-With': 'XMLHttpRequest',
# }
#
# payload={"productId":"CF226A","categoryId":"C-EI","placementids":"item_page.rr_warranties|item_page.rr2_recommends|item_page.rr1_recommends|item_page.rr3_recommends|item_page.rr4_recommends"}
# re=requests.post('https://de.insight.com/insightweb/getRecommendations',headers=header,data=json.dumps(payload))
#
# print(re.status_code)
