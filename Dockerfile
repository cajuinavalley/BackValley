FROM python:slim

LABEL Name=backvalley Version=0.0.1
EXPOSE 3000

WORKDIR /app
COPY . /app

RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt