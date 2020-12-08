FROM python:3.6-slim

EXPOSE 5000

COPY ./load_balancer.py /app/load_balancer.py
COPY ./config.cfg /app/config.cfg
COPY ./worker_config.yaml /app/worker_config.yaml
COPY ./Pipfile* /app/

ENV DEFAULT_CONFIG=/app/config.cfg

RUN pip install pipenv
RUN cd /app && pipenv lock --requirements > requirements.txt
RUN pip install -r /app/requirements.txt

CMD ["python", "/app/load_balancer.py"]
