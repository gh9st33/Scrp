```python
import scrapy

class ScraperItem(scrapy.Item):
    # define the fields for your item here like:
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    images = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)
```