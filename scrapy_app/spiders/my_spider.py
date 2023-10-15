```python
import scrapy
from scrapy_app.items import MyItem

class MySpider(scrapy.Spider):
    name = 'my_spider'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com']

    def parse(self, response):
        item = MyItem()
        item['url'] = response.url
        yield item

        for link in response.css('a::attr(href)').getall():
            yield response.follow(link, self.parse)
```