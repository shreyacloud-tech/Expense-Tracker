FROM python:3.12-slim

WORKDIR /app

COPY main.py .
COPY expenses.json .

CMD ["python", "main.py"]