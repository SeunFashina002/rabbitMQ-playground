import pika, time, sys, os

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # set queue to durable, so tasks won't be lost to server crash
    channel.queue_declare(queue="task_queue", durable=True)
    print(' [*] Waiting for messages. To exist press CTRL + C')

    def callback(ch, method, properties, body):
        print(f" [x] Received {body.decode()}")
        time.sleep(body.count(b"."))
        print("[x] Done")

        # send an acknoledgement
        channel.basic_ack(delivery_tag=method.delivery_tag)


    #prevent rabbitMQ from dispatching a new message to a worker until previous one has been processed and acknowledged 
    channel.basic_qos(prefetch_count=1)

    channel.basic_consume(queue="new_task_queue", on_message_callback=callback)    
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)