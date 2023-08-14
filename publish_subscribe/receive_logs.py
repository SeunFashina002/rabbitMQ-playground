import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# redeclare the exchange in the producer
channel.exchange_declare(exchange='logs', exchange_type='fanout')

"""
leaving the queue name empty tells RabbitMQ to auto generate a name
exclusive only allows access by the current connection
"""
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# binds the queue to the log 
channel.queue_bind(exchange='logs', queue=queue_name)

print('[*] Waiting for logs. To exist press CTRL + C')

def callback(ch, method, properties, body):
    print(f"[x] {body}")

channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
channel.start_consuming()