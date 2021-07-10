FROM python:3.9-slim

RUN apt-get update

RUN mkdir app
RUN mkdir static

ADD . /app
WORKDIR /app

RUN mkdir static

RUN pip3 install -r requirements.txt
EXPOSE 8000

ENTRYPOINT ["./start_server.sh"]