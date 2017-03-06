#!/bin/bash

NAME="testapp"                                   # Name of the application
DJANGODIR=/home/vagrant/testapp                  # Django project directory
SOCKFILE=/home/vagrant/testapp/run/gunicorn.sock # we will communicte using this unix socket
USER=vagrant                                     # the user to run as
NUM_WORKERS=1                                    # how many worker processes should Gunicorn spawn
DJANGO_SETTINGS_MODULE=testapp.settings          # which settings file should Django use
DJANGO_WSGI_MODULE=testapp.wsgi                  # WSGI module name

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $DJANGODIR
source /home/vagrant/.virtualenvs/testapp/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Create the run directory if it doesn't exist
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Start your Django Unicorn
# Programs meant to be run under supervisor should not daemonize themselves (do not use --daemon)
exec /home/vagrant/.virtualenvs/testapp/bin/gunicorn ${DJANGO_WSGI_MODULE}:application --name $NAME --workers $NUM_WORKERS --user=$USER -b 0.0.0.0:9000 --log-level=debug --log-file=-
