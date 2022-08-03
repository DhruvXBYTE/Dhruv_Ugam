# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class UgamSaturnDeSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class UgamSaturnDeDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.
        from w3lib.http import basic_auth_header
        proxy = [
            # '66b18fe5e75149d8b42fa081d35da7da:',
            # 'b2f2f933db0e49419b78a7414dbb340a:',
            # 'cf81ef6615b94fac98b52b70c28ed1de:',
            # '1a4ad5a11de54f78957254a095fe4f90:',
            # '6a00ddf079da4a2cb95cbbbba20f27de:',
            # 'bd0a18e4767e4115afcbb04f1083c439:',
            # '6be1eaf4d0eb43c9a1acbed03671eb54:',
            # 'a95d25a6de4048d2931a0dc08d6f6d7e:',
            # '3d312f274bb24164b95a5805adad3458:',
            # 'f940087357164ef7abe464b230d22397:',
            # '8a8dfbb1bf0d48d686f0acbe3c401bb7:',
            # '1e54d2378d2a49e3a199083741f8b389:',
            # '91cde569d403483fab622483b9f6ffae:',
            # 'a08430c980c048f195791a8cc832eb77:',
            # '1ba5dbdc9d574b4384af1ca80729c7e4:',
            # '534108d7f6954cd09b303b91d07af3fd:',
            # 'fda0d32bbf6b4770a80e75c446760111:',
            # 'ecc2e44a1c12410b89b765f543e6c3d1:',
            # '8d2450bd4e7346bdba74530890dd7814:',
            # 'f5018837e5dc4c1bba034ab0eb9d9c63:',
            # '6eb77d9ed6a545fd9293208c87b7a4eb:',
            # 'c6cf20757f2c478fb761e7ac22111957:',
            # '3827a6cb855e4e14b749ccc3a0b2d8a6:',
            # 'd0e63531a7e44e43a3c4d043f154de5f:',
            # '968cb62a269541f38995d62e8329a2ec:',
            # 'abf15f7e1db747748f6751c4c18ac6fd:',
            # 'c175f786313f47b4a9b4848246ffbb08:',
            # '46475df7034d4227826b398f1963e4c4:',
            # '295076252cfd4c6785db5845825ed279:',
            # '6f27185b65554aafbc7a1dca8c2f8f21:',
            '295076252cfd4c6785db5845825ed279:',
            # '3628e867a071480097cff6152acf095:',
            # '5c57a79ae7b54a1a8cb5552464ca3a10:',
            # '126428ac12674457ac7319f095c01a1e:',
        ]

        # current_proxy = str('6500c987aae7435a90c249b35b1c9376:')
        # request.meta['proxy'] = "http://proxy.zyte.com:8011"
        # request.headers['Proxy-Authorization'] = basic_auth_header(current_proxy, "")
        # request.headers['X-Crawlera-Cookies'] = "disable"
        # request.headers['x-requested-with'] = "XMLHttpRequest"

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
