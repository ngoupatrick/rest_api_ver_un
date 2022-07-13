from click import password_option
from flask import make_response, request, jsonify, Blueprint  # type:ignore

from src.main.models.models import User  
from src.main.utils.utils import token_required, checkAdmin


auth = Blueprint('auth', __name__)

@auth.route('/data/<pubid>', methods=['GET'])
def data(pubid):
    return jsonify({'message' : f'This data is readable by anybody; {pubid}'})

@auth.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        resp = make_response(
            {"message": "Could not verif"}, 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'}
        )
        resp.headers['WWW-Authenticate'] = 'Basic realm="Login required!"'
        return resp
    user = User.query.filter_by(login=auth.username).first()
    if not user:
        resp = make_response(
            {"message": "No matching user found"}, 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'}
        )
        resp.headers['WWW-Authenticate'] = 'Basic realm="Login required!"'
        return resp
    if user.verify_password(auth.password):
        token = user.generate_token()
        return jsonify({'token' : token.decode('utf-8'),'puid':user.puid})
    resp = make_response(
        {"message": "No auth, no user, nothing"}, 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'}
    )
    resp.headers['WWW-Authenticate'] = 'Basic realm="Login required!"'
    return resp