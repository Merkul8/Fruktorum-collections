FROM python:3.9.13

COPY requirements.txt /temp/requirements.txt
RUN mkdir service
WORKDIR /service
ADD . /service

EXPOSE 8000
# Необходимая команда для корректного запуска бд
RUN apt-get update && apt-get install -y postgresql-client build-essential postgresql-server-dev-all

RUN pip install --upgrade pip

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password service-user

USER service-user