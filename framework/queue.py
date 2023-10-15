```python
import pika
from scraper import ScraperTask

class TaskQueue:
    def __init__(self, host='localhost'):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='task_queue', durable=True)

    def add_task(self, task: ScraperTask):
        self.channel.basic_publish(
            exchange='',
            routing_key='task_queue',
            body=task.serialize(),
            properties=pika.BasicProperties(
                delivery_mode=2,  # make message persistent
            ))
        print(" [x] Task added to queue")

    def consume_tasks(self, callback):
        def callback_wrapper(ch, method, properties, body):
            task = ScraperTask.deserialize(body)
            callback(task)
            ch.basic_ack(delivery_tag=method.delivery_tag)

        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue='task_queue', on_message_callback=callback_wrapper)
        self.channel.start_consuming()

    def close(self):
        self.connection.close()
```