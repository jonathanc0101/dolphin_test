FROM python:3.9.1-buster

RUN export DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y
RUN apt-get install make build-essential curl wget git python-dev python-pip  libxml2-dev libxmlsec1-dev -y

# set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

COPY . /usr/src/app
RUN mkdir -p /usr/src/app/static
RUN rm -rf /usr/src/app/static

COPY ./scripts/wait-for-it.sh /root
COPY ./scripts/start_app.sh /usr/src/app/start_app.sh

WORKDIR "/usr/src/app"
RUN pip install -r requirements.txt
