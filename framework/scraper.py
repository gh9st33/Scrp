```python
import requests
from bs4 import BeautifulSoup
from data_storage import save_data

class ScraperTask:
    def __init__(self, task_id, url, data_type):
        self.task_id = task_id
        self.url = url
        self.data_type = data_type

    def execute_task(self):
        if self.data_type == 'html':
            self.scrape_html()
        elif self.data_type == 'image':
            self.scrape_image()
        else:
            raise ValueError('Invalid data type')

    def scrape_html(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        save_data(self.task_id, soup.prettify())

    def scrape_image(self):
        response = requests.get(self.url, stream=True)
        if response.status_code == 200:
            with open(f'{self.task_id}.jpg', 'wb') as out_file:
                out_file.write(response.content)
            save_data(self.task_id, f'{self.task_id}.jpg')
        else:
            raise ValueError('Unable to retrieve image')
```