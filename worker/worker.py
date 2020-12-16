import pika, sys, os
import json
import time
import logging
#logging.basicConfig(filename='error.log', level=logging.DEBUG)

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.environ['HOSTNAME']))
    channel = connection.channel()

    channel.queue_declare(queue='queue')

    def callback(ch, method, properties, body):
        message = body.decode()
        job = json.loads(message)
        print(" [x] Received Job ID ", job['job_id'], " , under Job name ", job['job_name'])
        #logging.debug(" [x] Received Job ID ", job['job_id'], " , under Job name ", job['job_name'])
        print(" Working...")
        #logging.debug("Working...")
        time.sleep(job['job_duration'])
        print(" [x] Done")
        #logging.debug(" [x] Done")
        ch.basic_ack(delivery_tag = method.delivery_tag)

    channel.basic_consume(queue='queue', on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    #logging.debug(' [*] Waiting for messages. To exit press CTRL+C')
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

