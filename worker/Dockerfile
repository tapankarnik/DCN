FROM python:3.6-slim

COPY ./worker.py /app/worker.py
RUN pip install pika

CMD ["python", "/app/worker.py"]
