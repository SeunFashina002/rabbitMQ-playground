import pika, sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


# direct exchange type determines which queue receive a message based on the routing and binding key
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else "info"
message = ''.join(sys.argv[1:]) or "Hello World"


channel.basic_publish(
    exchange='direct_logs',
    routing_key=severity,
    body=message
)
print(f"[x] Sent {severity} : {message}")
connection.close()