# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field


class NewsItem(scrapy.Item):
    headline = scrapy.Field()
    source = scrapy.Field()
    link = scrapy.Field()
    category = scrapy.Field()
    postdate = scrapy.Field()
