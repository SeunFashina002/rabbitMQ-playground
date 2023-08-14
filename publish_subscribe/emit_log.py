import pika, sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# delclare an exchange
# fanout exchange type broadcasts all messages to all known queues
channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ''.join(sys.argv[1:]) or "info: Hello World"

"""
without an exchage, messages are routed to the queue with the name specified by the routing_key.
With an exchange, messages are routed to the available queues.
Hence, routing_key can be left empty if an exchange is provided
"""
channel.basic_publish(
    exchange='logs',
    routing_key='',
    body=message
)
print(f"[x] Sent {message}")
connection.close()