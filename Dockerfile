FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
COPY delete.py delete.py
COPY .env .env

RUN pip install -r requirements.txt

CMD ["python", "delete.py"]
