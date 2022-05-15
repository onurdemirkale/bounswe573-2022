# Dockerfile for the NGINX reverse proxy

# This base image runs as unpriviledged user, meaning that the root
# user does not have root user priviledges. This hardens the security
# by limiting the locations the attacker can access in case this
# container is comprimised.
FROM nginxinc/nginx-unprivileged:1-alpine

# Copies the files into the docker container
COPY ./default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./uwsgi_params /etc/nginx/uwsgi_params
COPY ./run.sh /run.sh

ENV LISTEN_PORT=8000
ENV APP_HOST=web
ENV APP_PORT=9000

USER root

# Creates a static directory, gives the owner of the directory read
# and write permissions, creates an empty file using touch,
# chown changes the ownership of the created empty file
# to nginx user, finally executable permissions are given to 
# the run script. 
RUN mkdir -p /vol/static && \
    chmod 755 /vol/static && \
    touch /etc/nginx/conf.d/default.conf && \
    chown nginx:nginx /etc/nginx/conf.d/default.conf && \
    chmod +x /run.sh

VOLUME /vol/static

USER nginx

CMD ["/run.sh"]


