import hashlib
import time
import html
import datetime
import os
import scrapy
from ugam_Amazon_QA.config import *
from ugam_Amazon_QA.pipelines import *
from ugam_Amazon_QA.items import *
from mymodules._common_ import c_replace
import requests


class Amazon_Question(scrapy.Spider):
    name = 'Amazon_Question'
    F_PATH = HTML

    headers = {

        'authority': 'www.amazon.in',
        'method': 'GET',
        # 'path': '/Apple-iPhone-13-128GB-Product/product-reviews/B09G99CW2N/ref=cm_cr_arp_d_paging_btm_next_4?reviewerType=all_reviews&sortBy=helpful&pageNumber=4&formatType=current_format',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'no-cache',
        'cookie': 'session-id=262-0315199-9499465; i18n-prefs=INR; ubid-acbin=262-1385037-5259429; x-amz-captcha-1=1659006985710052; x-amz-captcha-2=oRs4aSCeGMhr0Pwy1T3ekA==; session-token="NP8IjrDzIQaLyNYmCME+Vo3KrGxCzGlHtmFwnLF91lTLTSzylt6w2zmqgrG2X1glaqo3NvL14pPPuhXzZNBUUoVVcNy/tKPr3LRTn7WlU4deUzA9J00ilOoI+wUWXRImSaEKFVCCbtDohEA1eXAmt+EDjsdIKnR0jLEtJOTP8IZSgS+tDgX5NhAaWm1zoe8T3RAJrW44vfOQP1+eixhjUw=="; session-id-time=2082787201l; csm-hit=tb:FGW8KM391HJR93R2TEYR+s-3SJ5VQSHYB9WP2WPE9QJ|1659000687189&t:1659000687189&adb:adblk_no',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-platform': '"Windows"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }

    def __init__(self, start='', end=''):

        try:
            self.cursor = UgamAmazonQaPipeline.cursor
            self.con = UgamAmazonQaPipeline.con
            self.start = start
            self.end = end
        except Exception as e:
            logger.error('exception in __init__ method main:{}'.format(e))

    def start_requests(self):
        asin = "SELECT Id,asin from input_sku "

        self.cursor.execute(asin)
        asin = [column for column in self.cursor.fetchall()]
        for i in asin:
            id = i[0]
            asin = i[1]

            filename = f'/{asin}.html'
            path = self.F_PATH + filename
            path = path.replace("\\", "/")

            if os.path.exists(path):
                pass
            else:
                prd_rweview = f"https://www.amazon.in/product-reviews/{asin}"
                url = f"https://www.amazon.in/ask/questions/asin/{asin}/1/ref=ask_ql_psf_ql_hza?sort=SUBMIT_DATE&isAnswered=TRUE"
                filename = f'/{asin}.html'
                path = self.F_PATH + filename
                path = path.replace("\\", "/")
                re = requests.get(url=url, headers=self.headers)

                with open(path, 'w', encoding='utf-8')as f:
                    f.write(re.text)

            yield scrapy.FormRequest(url=f'file:///{path}', callback=self.parse, dont_filter=True, meta={'asin': asin})

    def parse(self, response, **kwargs):
        print(response.status)
        asin = response.meta.get('asin')

        filename = f'/{asin}.html'
        path = self.F_PATH + filename
        path = path.replace("\\", "/")

        main_q=response.xpath('//div[@class="a-fixed-left-grid a-spacing-base"]')
        for i in main_q:

            id_q=i.xpath('//div[@class="a-fixed-left-grid a-spacing-base"]//div/@id').get()

            questions_text=i.xpath('//div[@class="a-fixed-left-grid a-spacing-base"]//div[@class="a-fixed-left-grid-col a-col-right"]//a[@class="a-link-normal"]//span/text()').get()






