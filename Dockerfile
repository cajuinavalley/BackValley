FROM python:3

LABEL Name=backvalley Version=0.0.1
EXPOSE 3000

WORKDIR /app
ADD . /app

RUN python3 -m pip install -r requirements.txt