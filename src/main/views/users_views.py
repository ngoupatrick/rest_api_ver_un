from click import password_option
from flask import make_response, request, jsonify, Blueprint  # type:ignore
from main.models import User  
from main.views.utils import token_required, checkAdmin

auth = Blueprint('auth', __name__)

@auth.route('/data/<pubid>', methods=['GET'])
def data(pubid):
    return jsonify({'message' : f'This data is readable by anybody; {pubid}'})

@auth.route('/login')
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
        return jsonify({'token' : token.decode('utf-8')})
    resp = make_response(
        {"message": "No auth, no user, nothing"}, 401, {'WWW-Authenticate' : 'Basic realm="Login required!"'}
    )
    resp.headers['WWW-Authenticate'] = 'Basic realm="Login required!"'
    return resp

@auth.route('/user', methods=['GET'])
@token_required
def get_all_users(current_user):
    if not checkAdmin(current_user):
        return jsonify({'message' : 'Cannot perform that function!'})
    users = User.query.all()
    output = []
    for user in users:
        user_data = {}
        user_data['puid'] = user.puid
        user_data['login'] = user.login
        user_data['is_admin'] = user.is_admin()
        output.append(user_data)
    return jsonify({'users' : output})

@auth.route('/user/<pubid>', methods=['GET'])
@token_required
def get_one_user(current_user, puid):
    if not checkAdmin(current_user):
        return jsonify({'message' : 'Cannot perform that function!'})
    user = User.query.filter_by(puid=puid).first()
    if not user:
        return jsonify({'message' : 'No user found!'})
    user_data = {}
    user_data['puid'] = user.puid
    user_data['login'] = user.login
    user_data['is_admin'] = user.is_admin()
    return jsonify({'user' : user_data})

@auth.route('/user', methods=['POST'])
@token_required
def create_user(current_user):
    if not checkAdmin(current_user):
        return jsonify({'message' : 'Cannot perform that function!'})
    json_data = request.get_json()
    password = json_data.get("password", "")
    login=json_data.get("login", "")
    nom=json_data.get("nom", "")
    gid=json_data.get("gid",0)
    new_user = User(login=login, password=password, nom=nom, gid=gid)
    new_user.save()
    return jsonify({'message' : 'New user created!'}), 201
