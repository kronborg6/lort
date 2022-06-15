import imp
import pika
import mysql.connector as database
import mariadb
from datetime import datetime

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')
for x in range(10000):
    dt = datetime.now()
    lortpaalort = dt.strftime('%y/%m/%d %H:%M:%S')
    # channel.basic_publish(exchange='', routing_key='hello', body="lort")
    channel.basic_publish(exchange='', routing_key='hello', body=str(lortpaalort))
    print(f" [{x}] Sent 'Hello World!'")
connection.close()