```python
import unittest
from scrapy.http import Request, HtmlResponse
from scrapy_app.spiders.my_spider import MySpider

class TestMySpider(unittest.TestCase):

    def setUp(self):
        self.spider = MySpider()

    def test_parse(self):
        url = 'http://example.com'
        request = Request(url=url)
        response = HtmlResponse(url=url, request=request, body='<html></html>', encoding='utf-8')

        result = self.spider.parse(response)
        self.assertIsInstance(result, dict)

    def test_start_requests(self):
        requests = list(self.spider.start_requests())
        self.assertTrue(len(requests) > 0)
        for request in requests:
            self.assertIsInstance(request, Request)

    def test_parse_item(self):
        url = 'http://example.com/item/1'
        request = Request(url=url)
        response = HtmlResponse(url=url, request=request, body='<html></html>', encoding='utf-8')

        result = self.spider.parse_item(response)
        self.assertIsInstance(result, dict)

if __name__ == '__main__':
    unittest.main()
```