import scrapy


class NewsspiderSpider(scrapy.Spider):
    name = "NewsSpider"
    allowed_domains = ["edition.cnn.com"]
    start_urls = ["https://edition.cnn.com/world"]

    def parse(self, response):
        pass
