#!/bin/sh

#FOR DEFAULT FLASK SERVER
default_server(){
    export FLASK_APP=./main.py #./src/wsgi.py
    export FLASK_ENV="development"
    flask run --port=8000 -h 0.0.0.0 --reload
}

#FOR GUNICORN SERVER
gunicorn_server(){
    export FLASK_APP="src.wsgi:app"
    export FLASK_ENV="development"
    WORKER=2
    gunicorn -w $WORKER -b 0.0.0.0:8000 $FLASK_APP --reload
}

#FOR WSGI SERVER
wsgi_server(){
    export FLASK_APP="src.wsgi:app"
    export FLASK_ENV="development"
    flask run -h 0.0.0.0:8000  #$FLASK_APP --reload
}

case $1 in
    "wsgi") wsgi_server
    ;;
    "gunicorn") gunicorn_server
    ;;
    "default") default_server
    ;;
    *) default_server
    ;;
esac

