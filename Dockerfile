FROM python:3.7
MAINTAINER Qubo Tecnologia

ENV PYTHONUNBUFFERED 1

# Setup locale settings
RUN apt-get clean && apt-get update && apt-get install git
WORKDIR /IOT/
COPY . /IOT/

RUN pip install -r requirements.txt
CMD ["/bin/bash"]