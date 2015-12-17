FROM nginx:latest

ENTRYPOINT ["/bin/start.sh"]
EXPOSE 80
VOLUME /templates

ADD start.sh /bin/start.sh
RUN chmod 777 /bin/start.sh
RUN rm -v /etc/nginx/conf.d/*.conf

ADD consul-template /usr/bin/

