import scrapy
import datetime


class CnnSpider(scrapy.Spider):
    name = "cnn"
    allowed_domains = ["edition.cnn.com"]
    start_urls = ["https://edition.cnn.com/world"]

    def parse(self, response):
        articles = response.css("a.container__link")
        
        for article in articles:
            headline = article.css("span::text").get()
            print(headline)
            link = article.css("a").attrib["href"]  
            yield {
                "headline": headline,
                "link": link,
                "source": "CNN",
                "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),   
            }
