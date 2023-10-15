```python
import unittest
from scrapy.http import Request, Response
from scrapy.spiders import Spider
from scrapy_app.middlewares import MyCustomMiddleware

class TestMyCustomMiddleware(unittest.TestCase):

    def setUp(self):
        self.middleware = MyCustomMiddleware()
        self.spider = Spider('foo')
        self.request = Request('http://www.example.com')
        self.response = Response('http://www.example.com')

    def test_process_request(self):
        result = self.middleware.process_request(self.request, self.spider)
        self.assertIsNone(result, "Middleware should return None for process_request")

    def test_process_response(self):
        result = self.middleware.process_response(self.request, self.response, self.spider)
        self.assertEqual(result, self.response, "Middleware should return the original response for process_response")

    def test_process_exception(self):
        result = self.middleware.process_exception(self.request, ValueError('Test'), self.spider)
        self.assertIsNone(result, "Middleware should return None for process_exception if not handling the exception")

if __name__ == '__main__':
    unittest.main()
```