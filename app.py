# this file is used by PythonAnywhere server
# base url: https://nanpson.pythonanywhere.com/
from src.main import create_app

app, db, bcrypt, ma = create_app()
