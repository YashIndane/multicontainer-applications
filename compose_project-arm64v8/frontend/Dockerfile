FROM arm64v8/amazonlinux:latest

MAINTAINER Yash Indane

EXPOSE 3499

COPY . /

RUN yum install python3 -y && \
    pip3 install -r requirements.txt

WORKDIR /

ENTRYPOINT ["python3", "app.py"] 
