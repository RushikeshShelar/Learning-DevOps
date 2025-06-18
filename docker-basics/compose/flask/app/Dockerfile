FROM python:3.12-alpine

WORKDIR /app
COPY app.py .
RUN pip install flask mysql-connector-python

CMD ["python", "app.py"]