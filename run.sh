#!/bin/sh

#FOR DEFAULT FLASK SERVER
default_server(){
    export FLASK_APP=./src/main.py
    export FLASK_ENV="development"
    flask run --port=8000 -h 0.0.0.0 --reload
}

#FOR GUNICORN SERVER
gunicorn_server(){
    export FLASK_APP="src.main:app"
    export FLASK_ENV="development"
    WORKER=2
    gunicorn -w $WORKER -b 0.0.0.0:8000 $FLASK_APP --reload
}

#CHOOSE SERVER TO RUN
case $1 in
    "gunicorn") gunicorn_server
    ;;
    "default") default_server
    ;;
    *) default_server
    ;;
esac

