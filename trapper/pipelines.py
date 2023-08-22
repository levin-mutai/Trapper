# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter.adapter import ItemAdapter
import psycopg2


class TrapperPipeline:
    def process_item(self, item, spider):
        # Loop through item fields and convert lists to single values
        for key in item.fields:
            print(key)
        # return item
        # pass


class SaveToDatabsePipeline:
    def __init__(self) -> None:
        self.conn = psycopg2.connect(
            host="localhost",
            database="trapper_db",
            user="postgres",
            password="lkm13464",
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
                UNIQUE(headline, link),
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
