#!/bin/sh
export FLASK_APP=./src/application.py
export FLASK_ENV="development"
flask run --port=8000 -h 0.0.0.0 --reload
