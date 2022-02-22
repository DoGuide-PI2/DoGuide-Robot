import pika

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

    channel = connection.channel()

    

    channel.queue_declare(queue='task_queue', durable=True)

if __name__ == '__main__':
    main()
