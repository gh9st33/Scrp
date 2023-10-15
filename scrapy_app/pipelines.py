```python
# Import necessary modules
from scrapy.exceptions import DropItem
from pymongo import MongoClient

class DuplicatesPipeline(object):
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['id'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['id'])
            return item

class MongoDBPipeline(object):
    def __init__(self):
        connection = MongoClient('localhost', 27017)
        db = connection["ScraperDB"]
        self.collection = db["scraped_items"]

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
```