#!/bin/sh

set -e

# Collect static files added for each Django application and places them
# in the static file directory which can then be sent to the proxy
# to be served directly.  
 python ./swe573/manage.py collectstatic --noinput 

# Run migrations to ensure that database is updated to the latest version.
python ./swe573/manage.py makemigrations &&
python ./swe573/manage.py migrate &&

python ./swe573/manage.py runserver 0.0.0.0:8000

