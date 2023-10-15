```python
import pika
from scraper_manager import ScraperTask

class TaskQueue:
    def __init__(self, host='localhost'):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='task_queue', durable=True)

    def callback(self, ch, method, properties, body):
        task = ScraperTask.from_json(body)
        task.execute()
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def consume(self):
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue='task_queue', on_message_callback=self.callback)
        self.channel.start_consuming()

    def publish(self, task):
        self.channel.basic_publish(
            exchange='',
            routing_key='task_queue',
            body=task.to_json(),
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            ))
        print(" [x] Sent %r" % task)

    def close(self):
        self.connection.close()
```