```python
import pika
import json

class TaskQueue:

    def __init__(self, host='localhost'):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='task_queue', durable=True)

    def publish_task(self, task):
        self.channel.basic_publish(
            exchange='',
            routing_key='task_queue',
            body=json.dumps(task),
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            ))
        print(" [x] Sent %r" % task)

    def close_connection(self):
        self.connection.close()

if __name__ == "__main__":
    task_queue = TaskQueue()
    task = {"url": "http://example.com", "scraper": "example_scraper"}
    task_queue.publish_task(task)
    task_queue.close_connection()
```