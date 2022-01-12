FROM centos:latest
MAINTAINER bragarg63@gmail.com
RUN yum install -y httpd
RUN systemctl start httpd
RUN service httpd start
RUN echo "this is my first server"> /var/www/html/index.html
EXPOSE 80
