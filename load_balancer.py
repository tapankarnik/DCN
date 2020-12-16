from flask import Flask, request
import json, yaml, os
import pika
import docker

load_balancer = Flask(__name__)
#load_balancer.config.from_envvar('DEFAULT_CONFIG')

def load_configuration(path):
    with open(path) as config_file:
        config = yaml.load(config_file, Loader=yaml.FullLoader)
    return config

#config = load_configuration(os.environ['WORKER_CONFIG'])

i = 0

@load_balancer.route('/first_hello', methods=['POST'])
def router():
    return b"OK"

@load_balancer.route('/DCN', methods=['POST'])
def loadbalancer():
    if request.is_json:
        job = request.json

        try:
            if len(job['job_name'])>20 or len(job['job_name'])==0 or job['job_name'] == None:
                raise Exception('Invalid Job Name')
            if job['num_jobs']<0 or job['num_jobs']==0 or job['num_jobs']>100:
                raise Exception('Invalid Number of Jobs')
            if job['job_id']<0 or job['job_id']>=job['num_jobs']:
                raise Exception('Invalid Job ID')
            if job['job_duration']<=0 or job['job_duration']>30:
                raise Exception('Invalid Job Duration')

        except Exception:
            return "Invalid Input", 400

        global i

        
        client = docker.from_env()
        containers = client.containers.list()
        CONTAINER_NAME = [container.name for container in containers if 'rabbitmq' in container.name]
        #CONTAINER_NAME = ['dcn_rabbitmq_1', 'dcn_rabbitmq2_1']
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=CONTAINER_NAME[i]) # Round-Robin Algorithm
            )
        i = (i+1)%len(CONTAINER_NAME)

        channel = connection.channel()

        channel.queue_declare(queue='queue')

        channel.basic_publish(
                exchange='',
                routing_key='queue',
                body=json.dumps(job)
                )

        print(" [x] Sent Job ID ", job['job_id'], " under Job name ", job['job_name'])

        connection.close()
        return b'OK\n'
    else:
        return b'Input not JSON', 400

if __name__=="__main__":
    load_balancer.run(host='0.0.0.0')

