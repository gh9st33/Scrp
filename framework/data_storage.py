```python
import psycopg2
from psycopg2 import Error
from scraper import ScraperTaskSchema

class DataStorage:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                user="username",
                password="password",
                host="127.0.0.1",
                port="5432",
                database="scraper_db"
            )
            self.cursor = self.connection.cursor()
        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def save_scraper_task(self, scraper_task: ScraperTaskSchema):
        try:
            postgres_insert_query = """ INSERT INTO scraper_tasks (task_id, task_type, task_status, task_data) VALUES (%s,%s,%s,%s)"""
            record_to_insert = (scraper_task.task_id, scraper_task.task_type, scraper_task.task_status, scraper_task.task_data)
            self.cursor.execute(postgres_insert_query, record_to_insert)
            self.connection.commit()
            count = self.cursor.rowcount
            print(count, "Record inserted successfully into scraper_tasks table")
        except (Exception, Error) as error:
            print("Failed to insert record into scraper_tasks table", error)

    def get_scraper_task(self, task_id):
        try:
            postgres_select_query = """ SELECT * FROM scraper_tasks WHERE task_id = %s"""
            self.cursor.execute(postgres_select_query, (task_id,))
            task_data = self.cursor.fetchone()
            return task_data
        except (Exception, Error) as error:
            print("Failed to get record from scraper_tasks table", error)

    def close_connection(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("PostgreSQL connection is closed")
```