#for wsgi.py

from main import db

#for main.py
'''
from src.main import db
'''

#for all py
import datetime
import uuid
import jwt  # type:ignore
from werkzeug.security import (  # type:ignore
    generate_password_hash, check_password_hash
)