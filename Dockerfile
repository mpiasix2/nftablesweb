FROM python:3.8-slim-buster

RUN apt-get update && apt-get upgrade -y

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir
COPY . .

EXPOSE 80
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]
