import scrapy
from .utils import get_category,get_date_from_url
import datetime

class AljazeeraSpider(scrapy.Spider):
    name = "aljazeera"
    allowed_domains = ["www.aljazeera.com"]
    start_urls = [
        "https://www.aljazeera.com/sports",
        "https://www.aljazeera.com/economy",
        "https://www.aljazeera.com/features",
        "https://www.aljazeera.com/investigations",
        "https://www.aljazeera.com/interactives",
        "https://www.aljazeera.com/interactives",
        "https://www.aljazeera.com/middle-east",
        "https://www.aljazeera.com/africa",
        "https://www.aljazeera.com/asia",
        "https://www.aljazeera.com/europe",
        "https://www.aljazeera.com/asia-pacific",
        "https://www.aljazeera.com/latin-america",  
        ]

    def parse(self, response):

        articles = response.css('div.gc__content')
        
        for article in articles:    
            headline = article.css('h3 a span::text').get()
            link =  article.css('h3 a').attrib["href"] 
            yield {
                "headline": headline.encode('ascii', 'ignore').decode('ascii'),
                "link": response.urljoin(link),
                "source": self.name,
                "category": get_category(response.url),
                "datetime": get_date_from_url(response.urljoin(link),self.name) if get_date_from_url(response.urljoin(link),self.name) else datetime.date.today().strftime("%Y-%m-%d"),   
            }
