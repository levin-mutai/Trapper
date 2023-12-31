import scrapy

from trapper.items import NewsItem
from .utils import get_category, get_date_from_url
import datetime


class ReutersSpider(scrapy.Spider):
    name = "reuters"
    allowed_domains = ["www.reuters.com"]
    start_urls = [
        "https://www.reuters.com",
        "https://www.reuters.com/world",
        "https://www.reuters.com/technology",
        "https://www.reuters.com/business",
        "https://www.reuters.com/finance",
        "https://www.reuters.com/markets",
        "https://www.reuters.com/legal",
        "https://www.reuters.com/sports",
        "https://www.reuters.com/lifestyle",
        "https://www.reuters.com/breakingviews",
    ]

    def parse(self, response):
        articles = response.css('div[data-testid="MediaStoryCard"]')
        news = NewsItem()
        for article in articles:
            headline = article.css(
                'h3[data-testid="Heading"] a[data-testid="Link"]::text'
            ).get()
            link = article.css(
                'h3[data-testid="Heading"] a[data-testid="Link"]'
            ).attrib["href"]
            news["headline"] = headline.encode("ascii", "ignore").decode("ascii")
            news["link"] = response.urljoin(link)
            news["source"] = self.name
            news["category"] = get_category(response.url)
            news["postdate"] = (
                get_date_from_url(response.urljoin(link), self.name)
                if get_date_from_url(response.urljoin(link), self.name)
                else datetime.date.today().strftime("%Y-%m-%d"),
            )
            yield news
