# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class NewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    headline = Field()
    date = Field()
    source = Field()
    link = Field()
    image_urls = Field()


class TrapperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
