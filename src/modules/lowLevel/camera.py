import pika, sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

# channel.basic_qos(prefetch_count=1)

# channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

result = channel.queue_declare(queue='', exclusive=True)

channel.queue_bind(exchange='logs', queue=result.method.queue)

channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message,
                      properties= pika.BasicProperties(
                          delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
                      ))
print('[x] sent hello world')

connection.close()