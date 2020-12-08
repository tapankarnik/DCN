# Data Center Network

## Docker
Build the Docker file for the load balancer and the worker. 

    docker build -t load_balancer .
    docker build -t worker worker/.

Use docker compose to set up the network

    docker-compose up

Run the following to take down the network

    docker-compose down

## Testing

Send a POST request to localhost:5000/DCN, where the load balancer is accepting requests.
Send a JSON message with 4 parameters, job_name, job_id, num_jobs and job_duration.
