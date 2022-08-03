# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UgamAmazonQaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class questions(scrapy.Item):

    def __setitem__(self, key, value):
        if key not in self.fields:
            self.fields[key] = scrapy.Field()
        self._values[key] = value
        super().__setitem__(key, value)

class answers(scrapy.Item):
    def __setitem__(self, key, value):
        if key not in self.fields:
            self.fields[key] = scrapy.Field()
        self._values[key] = value
        super().__setitem__(key, value)
