FROM python:3.13-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y libpq-dev gcc \
    && pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "backend/app.py"]