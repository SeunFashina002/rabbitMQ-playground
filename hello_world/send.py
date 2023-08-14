import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# create a hello queue
channel.queue_declare(queue='hello')


message = "hello world!"
# routing_key -> queue name
# send a message to the queue
channel.basic_publish(
    exchange="",
    routing_key="hello",
    body=message
)

print(f"[x] Sent {message}")
connection.close()