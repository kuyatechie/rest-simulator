FROM 10.12.14.138:9002/python:3.5-slim

LABEL

COPY apt.conf /etc/apt

RUN echo "deb http://http.debian.net/debian jessie-backports main" > /etc/apt/sources.list.d/jessie-backports.list

RUN pip install --proxy=http://87.254.212.120:8080 --upgrade pip flask

RUN mkdir /app
WORKDIR /app