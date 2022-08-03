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


class Amazon_Answer(scrapy.Spider):
    name = 'Amazon_Answer'
    F_PATH = HTML

    headers = {

        'authority':'www.amazon.in',
        'method':'GET',
        'path':'/ask/questions/asin/B09WRP2WXG/1/ref=ask_ql_psf_ql_hza?sort=SUBMIT_DATE&isAnswered=TRUE',
        'scheme':'https',
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language':'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7',
        'cookie':'session-id=262-0315199-9499465; i18n-prefs=INR; ubid-acbin=262-1385037-5259429; x-amz-captcha-1=1659016254848990; x-amz-captcha-2=nEZTMxdv8DMRI1Q2KkaeLg==; lc-acbin=en_IN; session-token=bPos5yGK7YM0WK1fpqS8azW8mt/6DMkGDCvWgB12PnkDAWJN5znB16uwVZ703GyLcuYws/OStAXFQbLKqMdyzc4nzmKzC7D7mwXNA21fj5hpd4JDBaQSCAz/1OxF7KaaHSIe+I+I9rD+2uo9XDhHtvw09VjcfiFoF4cY8Dqc8Dlmds9hHhm/MRoA9z64QSdMxeA3U7MRsKWVACu6zZ/kjqWa/uEMvgy9; csm-hit=tb:s-MBKT6RQ4KVV09MG2TD3C|1659339913018&t:1659339913268&adb:adblk_no; session-id-time=2082758401l',
        'sec-ch-ua':'".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-platform':'"Windows"',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',

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
                re = requests.get(url=url, headers=self.headers)

                filename = f'/{asin}.html'
                path = self.F_PATH + filename
                path = path.replace("\\", "/")

                with open(path, 'w', encoding='utf-8')as f:
                    f.write(re.text)

            yield scrapy.FormRequest(url=f'file:///{path}', callback=self.parse, dont_filter=True, meta={'asin': asin})

    def parse(self, response, **kwargs):
        print(response.status)

        asin = response.meta.get('asin')

        filename = f'/{asin}.html'
        path = self.F_PATH + filename
        path = path.replace("\\", "/")

        main_anser=response.xpath('')


