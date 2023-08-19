import scrapy
import datetime
from .utils import get_category, get_date_from_url


class SkynewsSpider(scrapy.Spider):
    name = "skynews"
    allowed_domains = ["news.sky.com"]
    start_urls = [
        "https://news.sky.com",
        "https://news.sky.com/uk",
        "https://news.sky.com/us",
        "https://news.sky.com/politics",
        "https://news.sky.com/business",
        "https://news.sky.com/technology",
        "https://news.sky.com/world",
        "https://news.sky.com/entertainment",
        "https://news.sky.com/strangenews",
        "https://news.sky.com/climate",
        "https://news.sky.com/weather",
        "https://news.sky.com/data-and-forensics",
        "https://www.skysports.com",
    ]

    def parse(self, response):
        articles = response.css("div.sdc-site-tiles__item")

        for article in articles:
            check = article.css("span.sdc-site-tile__headline-text::text").get()
            if check is None:
                continue

            headline = check
            link = article.css("h3 a").attrib["href"]
            yield {
                "headline": headline,
                "link": response.urljoin(link),
                "source": "skysports" if "skysports" in response.url else self.name,
                "category": "sports"
                if "skysports" in response.url
                else get_category(response.url),
                "postdate": get_date_from_url(response.urljoin(link), self.name)
                if get_date_from_url(response.urljoin(link), self.name)
                else datetime.date.today().strftime("%Y-%m-%d"),
            }
