# for wsgi.py

from main.models.models import User


#for main.py
'''
from src.main.models.models import User
'''

#for all py
from flask import request, make_response  # type:ignore
import jwt  # type:ignore
from functools import wraps