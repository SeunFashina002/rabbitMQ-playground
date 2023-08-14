import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# create a hello queue
channel.queue_declare(queue='hello')


# routing_key -> queue name
# send a message to the queue
channel.basic_publish(
    exchange="",
    routing_key="hello",
    body="Hello World"
)

print("[x] Sent 'Hello World'")
connection.close()