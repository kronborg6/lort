import pika, sys, os
import mysql.connector as database
from datetime import datetime
import time

def main():
    conn = database.connect(
    user="admin",
    password="lort",
    host="localhost",
    database="test"
    )
    cur = conn.cursor()
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')
    def callback(ch, method, properties, body):
        # time.sleep(.02)
        print(" [x] Received %r" % body.decode())
        now = datetime.now()
        statment = "INSERT INTO table1 (send_time, receive_time) VALUES (%s, %s)"


        date = datetime.strptime(body.decode(), '%y/%m/%d %H:%M:%S')
        # date2 = datetime.strptime(str(now), '%y/%m/%d %H:%M:%S')
        date2 = now.strftime('%y/%m/%d %H:%M:%S')


        # date = body.decode()
        cur.execute(statment, (date,date2,))
        conn.commit()
    
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)



    print(' [*] Waiting for messages. To exit press CTRL+C')
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