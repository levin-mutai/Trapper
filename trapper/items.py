# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class NewsItem(scrapy.Item):
    headline = Field()
    source = Field()
    link = Field()
    image_urls = Field()
    description = Field()
    category = Field()
    datetime = Field()
  
