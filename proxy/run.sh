#!/bin/sh

set -e 

# envsubst takes a file and substitues all variables within the dollar 
# sign and open and close bracket syntax with environment variables
# matching the name within.
envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/default.conf

# starts the nginx service running it in foreground in the docker container
nginx -g 'daemon off;'