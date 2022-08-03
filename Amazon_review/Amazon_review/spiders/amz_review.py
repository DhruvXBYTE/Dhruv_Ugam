import hashlib
import time
import html
import datetime
import os
import scrapy
from scrapy.selector import Selector
import time
from datetime import date, timedelta, datetime
today = datetime.now()


from Amazon_review.config import *
from Amazon_review.pipelines import *
from Amazon_review.items import *
from mymodules._common_ import c_replace
import requests

class Amazon_Review(scrapy.Spider):

    name = 'AmazonReview'
    F_PATH=HTML

    headers={
        'authority': 'www.amazon.in',
        'method': 'GET',
        # 'path': '/OnePlus-Sierra-Black-Storage-SuperVOOC/dp/B09WRP2WXG/',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,hi;q=0.7',
        'cache-control': 'no-cache',
        'cookie': 'session-id=262-0315199-9499465; i18n-prefs=INR; ubid-acbin=262-1385037-5259429; x-amz-captcha-1=1659016254848990; x-amz-captcha-2=nEZTMxdv8DMRI1Q2KkaeLg==; lc-acbin=en_IN; session-token=qgsegkWjkwZIZdocO1qHG42039fIv5L8ZEIDmkqtlN7OmbHQKTILS+bKK/VzdscP2bW5Ik3fee11U2W9PYjpn0vZ8JHCe9XsGMOX6114vw5pH8NzF6sNXUBvpfrOpcvix+AsCYTJiWumFjHm4yeWwO3zZuxJWFAXZSoOfEygsBykweU9ih1Lorf2lFq6dJuBXU+PCtTHrjFhzs60ak7sW2KZD1xOGCRr; csm-hit=tb:AJNWSR2KGNAFF2KTNXC5+s-AJNWSR2KGNAFF2KTNXC5|1659351222329&t:1659351222329&adb:adblk_no; session-id-time=2082787201l',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-platform': '"Windows"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',

    }

    def __init__(self, start='', end=''):

        try:
            self.cursor = AmazonReviewPipeline.cursor
            self.con = AmazonReviewPipeline.con
            self.start = start
            self.end = end
        except Exception as e:
            logger.error('exception in __init__ method main:{}'.format(e))


    def start_requests(self):

        asin="SELECT Id,Product,asin from input_sku "

        self.cursor.execute(asin)
        asin = [column for column in self.cursor.fetchall()]
        for i in asin:
            id=i[0]
            product=i[1]
            asin=i[2]


            meta_dict = {
                'row_id': id,
                'url': product,
                'counter': 0,
                'page_no': 0,
                'asin':asin

            }

            # p_id = asin.split('dp/')[1].split('/')[0]
            filename = f'/{asin}.html'
            path = self.F_PATH + filename
            path = path.replace("\\", "/")

            if os.path.exists(path):
                pass
            else:
                # prd_rweview=f"https://www.amazon.in/product-reviews/{asin}"
                # prd_reviewn=f"https://www.amazon.in/product-reviews/{asin}/ref=cm_cr_arp_d_viewopt_fmt?reviewerType=all_reviews&sortBy=recent&pageNumber=1&formatType=current_format"
                re=requests.get(url=product,headers=self.headers)

                filename = f'/{asin}.html'
                path = self.F_PATH + filename
                path = path.replace("\\", "/")

                with open(path,'w',encoding='utf-8')as f:
                    f.write(re.text)

            yield scrapy.FormRequest(url=f'file:///{path}', callback=self.parse, dont_filter=True,meta={'meta_dict':meta_dict})

    def parse(self, response, **kwargs):

        print(response.status)
        # print(response.text)
        meta_dt=response.meta.get('meta_dict')
        product_url=meta_dt.get('url')
        counter=meta_dt.get('counter')
        page_no=meta_dt.get('page_no')
        row_id=meta_dt.get('row_id')
        asin=meta_dt.get('asin')

        # p_id = product_url.split('dp/')[1].split('/')[0]
        filename = f'/{asin}.html'
        path = self.F_PATH + filename
        path = path.replace("\\", "/")

        # Todo --------- ITEMS CALL ------------
        item=AmazonReviewItem()

        if page_no == 0:
            see_more_xpath = response.xpath('//link[@rel="canonical"]//@href').get()
            if see_more_xpath:
                # 'https://www.amazon.com/Airborne-Vitamin-750mg-Serving-Gluten-Free/dp/B08G9JLJ1Y'
                see_more_xpath = see_more_xpath.replace('dp', 'product-reviews')
                see_more_req = f'{see_more_xpath}/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&sortBy=recent&pageNumber=1'
                print(see_more_req)
            else:
                see_more_req = product_url
        else:
            see_more_req = product_url

        filename = f'/AmazonUs_{asin}_review_{page_no}.html'
        path = self.F_PATH + filename
        review_requests_path = path.replace("\\", "/")
        if os.path.exists(review_requests_path):
            with open(review_requests_path, 'r', encoding='utf-8') as f:
                review_rating = f.read()
        else:
            # with open(path, 'wb') as f:
            #     f.write(response.body)
            # scraper_url = 'http://api.scraperapi.com/?api_key=ec46668b42a54199b95f52ab3d9ba6f8&url=' + see_more_req + '&keep_headers=true&country_code=true'
            review_rating = requests.get(url=see_more_req,headers=self.headers)
            with open(review_requests_path, 'w', encoding='utf-8') as f:
                f.write(review_rating.text)
            with open(review_requests_path, 'r', encoding='utf-8') as f:
                review_rating=f.read()

        Status_Flag = True
        review_rating = Selector(text=review_rating)
        # start_date= datetime.today().strftime('%d/%m/%Y %H:%M:%S %p')
        capcha_page = review_rating.xpath('//h4[contains(text(),"Enter the characters you see below")]').get()
        if capcha_page:
            return None
        else:
            if review_rating.xpath('//div[@id="cm_cr-review_list"]'):
                # if review_rating.xpath('//div[@id="cm_cr-review_list"]') :
                #     Status_Flag = True
                Exit_Flag = True
                mainxpat = review_rating.xpath('//div[@id="cm_cr-review_list"]//div[@class="a-section review aok-relative"]')
                for i in mainxpat:

                    review_date = i.xpath('.//div//span[@data-hook="review-date"]//text()').get()
                    # end_date = today.strftime("%Y-%m-%d")
                    if review_date:
                        Status_Flag = True  # TODO : demo
                        Exit_Flag = True
                        review_date = review_date.replace('Reviewed in India on ', '').replace(',', '')
                        print(review_date)
                        import datetime
                        datetime_object = datetime.datetime.strptime(review_date, "%d %B %Y")
                        month_number = str(datetime_object.date())
                        start_date = today - timedelta(days=30)
                        end_date = today.strftime("%Y-%m-%d")
                        if month_number <= end_date and month_number >= str(start_date):
                            Time = "T00:00:00"
                            reviewdate = review_date + Time
                            print("date::", reviewdate)
                            Master_ASIN = asin
                            raiting = i.xpath('.//div[@class="a-row"]/a//span[@class="a-icon-alt"]//text()').get()
                            if raiting:
                                raiting = raiting.replace('.0 out of 5 stars', '')
                            else:
                                raiting = 'NA'
                            title = i.xpath('.//div[@class="a-row"]//a[@data-hook="review-title"]/span//text()').get()
                            web_review_ID = i.xpath('./@id').get()
                            profile_name = i.xpath('.//span[@class="a-profile-name"]//text()').get()
                            response_text = i.xpath('.//div[@class="a-row a-spacing-small review-data"]//span[@data-hook="review-body"]/span/text()').getall()

                            if response_text == []:
                                response_text = 'NA'
                            else:
                                response_text = ''.join(c_replace(response_text))
                            Response_Available = 'No'
                            Author = 'NA'
                            counter += 1
                            if counter <= 1000:
                                try:

                                    item['ASIN'] = c_replace(str(asin))
                                    item['HtmlPath'] = c_replace(str(path))
                                    item['Product_url'] = c_replace(str(product_url))
                                    item['star_rating'] = c_replace(str(raiting))
                                    item['review_title'] = c_replace(str(title))
                                    item['review_detail'] = c_replace(response_text)
                                    item['web_review_ID'] = c_replace(str(web_review_ID))
                                    item['reviewed_by'] = c_replace(str(profile_name))
                                    item['Review_Date'] = str(month_number)
                                    item['Response_Available'] = "No"
                                    item['Author'] = "NA"
                                    from datetime import datetime
                                    item['Scrape_date'] = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
                                    item['created_time'] = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
                                    item['Status'] = "Done"

                                    print(item)
                                    AmazonReviewPipeline.insert_into(self, item)
                                    # yield item
                                except Exception as e:
                                    logger.error('error in item yield get_product_url method in:{}'.format(e))
                        else:
                            Exit_Flag = False
                            Status_Flag = True
                            # branch_sql = f'update {db_brand_table} set `Reviews_status` = "Done" where id ={row_id}'
                            # self.cursor.execute(branch_sql)
                            # self.con.commit()
                            return None
                    else:

                        Exit_Flag = False
                        Status_Flag = False
                        break

                if Exit_Flag:

                    page_url_ = review_rating.xpath('//ul[@class="a-pagination"]//li[@class="a-last"]/a/@href').get()
                    # page_url_ = response.xpath('//link[@rel="next"]/@href')
                    if page_url_:
                        page_url = f'https://www.amazon.in{page_url_}'
                        Product_url = page_url
                        page_no += 1
                        page_no = page_no + 1

                        # filename = f'/AmazonUs_{ASIN}_Page_{page_no}.html'
                        # path = self.F_PATH + filename
                        # path = path.replace("\\", "/")

                        filename = f'/AmazonUs_{asin}_review_{page_no}.html'
                        path = self.F_PATH + filename
                        review_requests_path = path.replace("\\", "/")
                        # if os.path.exists(review_requests_path):
                        #     with open(review_requests_path, 'r', encoding='utf-8') as f:
                        #         review_rating = f.read()

                        meta_dict = {
                            'counter': counter,
                            'row_id': row_id,
                            'page_no': page_no,
                            'ASIN': asin,
                            'Product_url': Product_url
                        }

                        if os.path.exists(review_requests_path):
                            yield scrapy.FormRequest(url=f"file:///{review_requests_path}", callback=self.parse,
                                                     dont_filter=True, headers=self.headers,
                                                     meta={'meta_dict': meta_dict})
                        else:
                            yield scrapy.FormRequest(url=Product_url, callback=self.parse, dont_filter=True,
                                                     headers=self.headers,
                                                     meta={'meta_dict': meta_dict})
                            # return None
                    else:
                        Exit_Flag = False
                        Status_Flag = True

                # except Exception as e:
                #     logger.error('exception in parse method for pagination:{}'.format(e))

                else:
                    Status_Flag = False


            # rating=i.xpath('.//i[@data-hook="review-star-rating"]//span//text()').get()
            #
            # review_by=i.xpath('.//div[@class="a-profile-content"]//span[@class="a-profile-name"]//text()').get()
            #
            # review_title=i.xpath('.//a[@data-hook="review-title"]//span//text()').get()
            #
            # review_text=i.xpath('.//span[@data-hook="review-body"]//span/text()').get()
            #
            # if review_text==None:
            #     review_text=''
            # else:
            #     review_text=c_replace(review_text)
            # print(review_text)
            #
            #
            # review_id=i.xpath('./@id').get()
            # print(review_id)
            #
            # review_date=i.xpath('.//span[@data-hook="review-date"]//text()').get()
            #
            # product_url = "https://www.amazon.in/"+asin


if __name__ == '__main__':
    from scrapy.cmdline import execute
    execute('scrapy crawl AmazonReview'.split())