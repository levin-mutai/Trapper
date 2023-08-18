import scrapy
import datetime


class CnnGeneralSpider(scrapy.Spider):
    name = "cnn-general"
    allowed_domains = ["edition.cnn.com"]
    start_urls = ["https://edition.cnn.com"]

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
                "category": "general",
                "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),   
            }

class CnnBusinessSpider(scrapy.Spider):
    '''
    spider to scrap all business articles from cnn

    '''
    name = "cnn-business"
    allowed_domains = ["edition.cnn.com"]
    start_urls = ["https://edition.cnn.com/business"]

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
                "category": "business",
                "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),   
            }

class CnnSportsSpider(scrapy.Spider):
    '''
    spider to scrap all sports articles from cnn

    '''
    name = "cnn-sports"
    allowed_domains = ["edition.cnn.com"]
    start_urls = ["https://edition.cnn.com/sports"]

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
                "category": "sports",
                "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),   
            }

class CnnTechnologySpider(scrapy.Spider):
    '''
    spider to scrap all technology articles from cnn

    '''
    name = "cnn-technology"
    allowed_domains = ["edition.cnn.com"]
    start_urls = ["https://edition.cnn.com/technology"]

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
                "category": "technology",
                "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),   
            }

class CnnHealthSpider(scrapy.Spider):
    '''
    spider to scrap all health articles from cnn

    '''
    name = "cnn-health"
    allowed_domains = ["edition.cnn.com"]
    start_urls = ["https://edition.cnn.com/health"]

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
                "category": "health",
                "datetime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),   
            }