import scrapy
from random_user_agent.params import SoftwareName, OperatingSystem
from random_user_agent.user_agent import UserAgent
from random import choice


def get_useragent():
    l1 = [SoftwareName.CHROME.value, SoftwareName.FIREFOX.value, SoftwareName.OPERA.value]
    software_names = [choice(l1)]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value, OperatingSystem.SUNOS.value]
    user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=1000)

    return user_agent_rotator.get_random_user_agent()


header = {
    'authority': 'shop.barr-thorp.com',
    'method': 'GET',
    # 'path': '/products/GV2ME08',
    'scheme': 'https',
    # 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    # 'cookie': 'cf_chl_2=a4c2e488721ed1c; cf_chl_prog=x13; cf_clearance=KyEDVVZiGgwgTKykomw.eXJuczZv2w1ecCCJZqSmaKw-1655968875-0-150; _kyklo-web_session=6ca3e6eacd4ef6a4d833ccdb7f0dcc36; _ga=GA1.3.437707213.1655968878; _gid=GA1.3.1332018629.1655968878; _hp2_id.2844502186=%7B%22userId%22%3A%227615546074688719%22%2C%22pageviewId%22%3A%222352021571237761%22%2C%22sessionId%22%3A%227396096363349017%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _hp2_ses_props.2844502186=%7B%22r%22%3A%22https%3A%2F%2Fshop.barr-thorp.com%2Fproducts%2FGV2ME08%3F__cf_chl_tk%3DddhnQ1cbESyeOcAg4PtjUiKreDS0L9OK_e.Jqn_8yQ0-1655968871-0-gaNycGzNCJE%22%2C%22ts%22%3A1655968877857%2C%22d%22%3A%22shop.barr-thorp.com%22%2C%22h%22%3A%22%2Fproducts%2FGV2ME08%22%7D',
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


class Response_chk(scrapy.Spider):
    name = 'response'

    handle_httpstatus_list = [503, 429]
    RETRY_HTTP_CODES = [429, 403]


    def start_requests(self):
        url = 'https://shop.barr-thorp.com/products/GV2ME08'
        url1='https://www.saturn.de/de/product/_msi-katana-gf76-11uc-698-gaming-notebook-mit-17-zoll-display-intelr-coretm-i5-prozessor-8-gb-ram-512-gb-ssd-geforce-rtxtm-3050-laptop-gpu-core-black-2784475.html'
        yield scrapy.Request(url=url1, callback=self.parse,headers=header)

    def parse(self, response, **kwargs):
        re = response.status
        # print("Status", re)


        # with open('Index.html','w',encoding='utf-8') as f:
        #     f.write(response.text)


from scrapy.cmdline import execute
execute('scrapy crawl response'.split())


