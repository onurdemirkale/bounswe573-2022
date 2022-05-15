#!/bin/sh

set -e

# Wait for the database to launch.
python ./swe573/manage.py wait_for_db

# Collect static files added for each Django application and places them
# in the static file directory which can then be sent to the proxy
# to be served directly.  
python ./swe573/manage.py collectstatic --noinput 

# Run migrations to ensure that database is updated to the latest version.
python ./swe573/manage.py migrate

# Run the uwsgi command, run it on a socket on port 9000 so that nginx 
# can connect. Specify uwsgi service workers for concurrent requests,
# run it as the master daemon so that it runs on the foreground, enable
# multi-threading and run the wsgi module provided by the Django command
# that creates the project. 
uwsgi --socket :9000 --workers 4 --master --enable-threads --chdir ./swe573 --module swe573.wsgi
