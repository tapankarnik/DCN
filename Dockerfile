FROM python:3.6-slim

RUN pip install flask
COPY ./app.py /app/app.py
COPY ./config.cfg /app/config.cfg

CMD ["python", "/app/app.py"]
