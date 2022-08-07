FROM amazonlinux:latest

MAINTAINER Yash Indane

EXPOSE 80

COPY ./requirements.txt / 

RUN yum install python3 -y && \
    pip3 install -r requirements.txt && \
    yum install httpd -y

COPY ./mysql-save.py /var/www/cgi-bin/

RUN chmod +x /var/www/cgi-bin/mysql-save.py

CMD /usr/sbin/httpd -DFOREGROUND 
