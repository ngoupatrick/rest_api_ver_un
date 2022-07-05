#!/bin/sh

#FOR DEFAULT FLASK SERVER
default_server(){
    export FLASK_APP=./wsgi.py #./main.py
    export FLASK_ENV="development"
    flask run --port=8000 -h 0.0.0.0 --reload
}

#FOR GUNICORN SERVER
gunicorn_server(){
    export FLASK_APP="wsgi:app"
    export FLASK_ENV="development"
    WORKER=2
    gunicorn -w $WORKER -b 0.0.0.0:8000 $FLASK_APP --reload
}

#FOR WSGI SERVER
uwsgi_server(){
    export FLASK_APP="wsgi:app"
    export FLASK_ENV="development"
    WORKER=2
    uwsgi --http 0.0.0.0:8000 --master -p $WORKER -w $FLASK_APP  --py-autoreload 1
}

case $1 in
    "uwsgi") uwsgi_server
    ;;
    "gunicorn") gunicorn_server
    ;;
    "default") default_server
    ;;
    *) default_server
    ;;
esac

