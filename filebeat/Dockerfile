#https://www.elastic.co/guide/en/beats/filebeat/current/running-on-docker.html
FROM docker.elastic.co/beats/filebeat:7.4.0
COPY config/filebeat.yml /usr/share/filebeat/filebeat.yml
USER root
RUN chown root:filebeat /usr/share/filebeat/filebeat.yml
RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm
RUN yum update -y
RUN yum install -y python36u python36u-libs python36u-devel python36u-pip
USER filebeat

