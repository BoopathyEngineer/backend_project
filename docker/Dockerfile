ARG NAME=latest
FROM ubuntu:${NAME}
LABEL maintainer="Boopathy <boopathitraders@gmail.com>"
RUN apt-get  update && apt install -y apache2  && service apache2 restart && echo " hai am boopathy , i am a devops engineer" > /var/www/html/index.html && echo "  i will earn 10 lpa this year" > /var/www/html/earn.html && echo "ServerName localhost" >> /etc/apache2/apache2.conf
RUN service apache2 restart
