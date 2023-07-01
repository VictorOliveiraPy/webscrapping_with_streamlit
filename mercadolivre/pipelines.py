# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from repository.database import TransactionsTable

# useful for handling different item types with a single interface

repository = TransactionsTable()


class MercadolivrePipeline:
    def process_item(self, item, spider):
        repository.insert_items(item)
        return item
