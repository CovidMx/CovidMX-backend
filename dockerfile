FROM python:3.7

RUN mkdir /code

WORKDIR /code

RUN apt-get update
RUN apt-get --yes install python3-dev default-libmysqlclient-dev build-essential

RUN pip install asgiref==3.2.10
RUN pip install Django==3.1.1
RUN pip install djangorestframework==3.11.1
RUN pip install pytz==2020.1
RUN pip install sqlparse==0.3.1
RUN pip install mysqlclient
RUN pip install django-cors-headers

COPY . /code/
