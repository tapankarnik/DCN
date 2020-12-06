# Data Center Network

## Python
Install pipenv to install the required packages, flask and pytest

    pip3 install pipenv

Once pipenv is working run the following

    pipenv shell
    pipenv install

Now your virtual environment is ready

Set an environment variable called DEFAULT_CONFIG to config.cfg

    export DEFAULT_CONFIG=config.cfg

run the following to launch the server

    python app.py

## Docker
Build the docker file if you want to run the server in a docker container

    docker build -t server .

To run the server in a docker container run the following

    docker run -e DEFAULT_CONFIG='/app/config.cfg' -p 5000:5000 --rm server

