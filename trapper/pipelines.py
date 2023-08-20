# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter.adapter import ItemAdapter


class TrapperPipeline:
    def process_item(self, item, spider):
        # Loop through item fields and convert lists to single values
        # for key in item.fields:
        #     if isinstance(item[key], list):
        #         item[key] = item[key][0]
        # return item
        pass
