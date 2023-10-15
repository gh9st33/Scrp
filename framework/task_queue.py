```python
import pika
import json

class TaskQueue:

    def __init__(self, host='localhost', queue='task_queue'):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()
        self.queue = queue
        self.channel.queue_declare(queue=self.queue, durable=True)

    def add_task(self, task):
        task_json = json.dumps(task)
        self.channel.basic_publish(exchange='',
                                   routing_key=self.queue,
                                   body=task_json,
                                   properties=pika.BasicProperties(
                                       delivery_mode=2,  # make message persistent
                                   ))
        print(" [x] Task added to the queue")

    def get_task(self):
        method_frame, header_frame, body = self.channel.basic_get(self.queue)
        if method_frame:
            print(" [x] Received task from the queue")
            self.channel.basic_ack(method_frame.delivery_tag)
            return json.loads(body)
        else:
            print("No message returned")
            return None

    def close_connection(self):
        self.connection.close()
```