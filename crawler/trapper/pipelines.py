# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter.adapter import ItemAdapter
import psycopg2
from dataclasses import field
from trapper.settings import DATABASE


class SaveToDatabsePipeline:
    def __init__(self) -> None:
        self.conn = psycopg2.connect(
            host=DATABASE["host"],
            database=DATABASE["database"],
            user=DATABASE["username"],
            password=DATABASE["password"],
        )

        self.cur = self.conn.cursor()  # cursor object to execute SQL commands

        ## Create news Table if none exist .
        self.cur.execute(
            """
            CREATE TABLE IF NOT EXISTS news (
                id SERIAL PRIMARY KEY,
                headline VARCHAR(255) NOT NULL,
                link VARCHAR(255) NOT NULL,
                source VARCHAR(255) NOT NULL,
                category VARCHAR(255) NOT NULL,
                postdate DATE NOT NULL,
                created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(headline, link)
            );
                
            """
        )

    def process_item(self, item, spider):
        self.cur.execute(
            """
            INSERT INTO news (headline, link, source, category, postdate)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (headline, link) DO NOTHING;
            """,
            (
                item["headline"],
                item["link"],
                item["source"],
                item["category"],
                item["postdate"],
            ),
        )

        self.conn.commit()

        return item

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

class DeduplicationPipeline:
    def __init__(self):
        self.seen_headlines = set()

    def process_item(self, item, spider):
        headline = item['headline']
        if headline not in self.seen_headlines:
            self.seen_headlines.add(headline)
            return item
        else:
            raise DropItem(f'Duplicate item found: {headline}')
