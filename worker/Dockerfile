FROM python:3.6-slim

COPY ./worker.py /app/worker.py
RUN pip install pika
RUN pip install requests

CMD ["python", "/app/worker.py"]
