import sys, pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# set queue to durable, so tasks won't be lost to server crash
channel.queue_declare(queue="task_queue", durable=True)
message = ' '.join(sys.argv[1:]) or "Hello World..."
channel.basic_publish(
    exchange="",
    routing_key="task_queue",
    body=message,
    
    # temporarily makes messages persistent
    properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE)
)
print(f"[x] sent {message}")