import scrapy
import datetime
from .utils import get_category, get_date_from_url

class SkynewsSpider(scrapy.Spider):
    name = "skynews"
    allowed_domains = ["news.sky.com"]
    start_urls = ["https://news.sky.com"]

    def parse(self, response):
        articles = response.css('div.sdc-site-tiles__item')
        
        for article in articles:  
            if  article.css('span.sdc-site-tile__headline-text::text').get() == None:
                continue
            
            headline = article.css('span.sdc-site-tile__headline-text::text').get()
            link =  article.css('h3 a').attrib["href"] 
            yield {
                "headline": headline,
                "link": response.urljoin(link),
                "source": self.name,
                "category": get_category(response.url),
                "datetime": get_date_from_url(response.urljoin(link),'reuters') if get_date_from_url(response.urljoin(link),'reuters') else datetime.date.today().strftime("%Y-%m-%d"),   
            }