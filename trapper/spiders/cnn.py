import scrapy
import datetime
from .utils import get_category

class CnnGeneralSpider(scrapy.Spider):
    name = "cnn"
    allowed_domains = ["edition.cnn.com"]
    start_urls = [
        "https://edition.cnn.com",
        "https://edition.cnn.com/world",
        "https://edition.cnn.com/us",
        "https://edition.cnn.com/business",
        "https://edition.cnn.com/technology",
        "https://edition.cnn.com/entertainment",
        "https://edition.cnn.com/sport",
        "https://edition.cnn.com/health",
        "https://edition.cnn.com/opinion",
        "https://edition.cnn.com/travel",
        "https://edition.cnn.com/specials",
        "https://edition.cnn.com/politics",
        "https://edition.cnn.com/style",
        "https://edition.cnn.com/weather",
        ]

    def parse(self, response):
        articles = response.css("a.container__link")
        
        for article in articles:
            headline = article.css("span::text").get()
            link = article.css("a").attrib["href"]  
            yield {
                "headline": headline,
                "link": link,
                "source": "CNN",
                "category": get_category(response.url),
                "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),   
            }