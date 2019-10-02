FROM python:3.7
MAINTAINER Iure Brandao

ENV PYTHONUNBUFFERED 1

# Setup locale settings
RUN apt-get clean && apt-get update && apt-get install git
ADD client.py /
ADD requirements.txt /

RUN pip install -r requirements.txt
CMD [ "python", "./client.py" ]