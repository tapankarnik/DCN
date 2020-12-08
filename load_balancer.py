from flask import Flask, request
import json, yaml
import pika

load_balancer = Flask(__name__)
load_balancer.config.from_envvar('DEFAULT_CONFIG')

def load_configuration(path):
    with open(path) as config_file:
        config = yaml.load(config_file, Loader=yaml.FullLoader)
    return config

config = load_configuration('/app/worker_config.yaml')
print(config)

#EXCHANGE_LIST = [5672, 5673]
i = 0

@load_balancer.route('/first_hello', methods=['POST'])
def router():
    return b"OK"

@load_balancer.route('/DCN', methods=['POST'])
def loadbalancer():
    job = request.json
    global i

    EXCHANGE_PORTS = config['EXCHANGE_PORTS']
    CONTAINER_NAME = ['rabbitmq', 'rabbitmq2']
    print(CONTAINER_NAME[i])
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=CONTAINER_NAME[i]) # Round-Robin Algorithm
        )
    i = (i+1)%len(EXCHANGE_PORTS)

    channel = connection.channel()

    channel.queue_declare(queue='queue')

    channel.basic_publish(
            exchange='',
            routing_key='queue',
            body=json.dumps(job)
            )

    print(" [x] Sent Job ID ", job['job_id'], " under Job name ", job['job_name'])
    #print(" [x] Sent dummy message")

    connection.close()
    return b'OK'


if __name__=="__main__":
    load_balancer.run(host='0.0.0.0')

