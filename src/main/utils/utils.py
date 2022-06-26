from . import *


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            resp = returnRep(msgErr="Token is missing", codeErr=401,
                             isRealm=True, msgRealm="Login required!")
            return resp
        try:
            current_user = User.verify_token(token)
        except jwt.exceptions.InvalidSignatureError as e:
            resp = returnRep(msgErr=str(e), codeErr=401,
                             isRealm=True, msgRealm="Login required!")
            return resp
        except jwt.exceptions.ExpiredSignatureError as e:
            resp = returnRep(msgErr=str(e), codeErr=401,
                             isRealm=True, msgRealm="Login required!")
            return resp
        if current_user is None:
            resp = returnRep(msgErr="No matching user found",
                             codeErr=401, isRealm=True, msgRealm="Login required!")
            return resp
        return f(current_user, *args, **kwargs)
    return decorated


def returnRep(msgErr, codeErr, isRealm=False, msgRealm="Login required!"):
    resp = make_response({"message": msgErr}, codeErr)
    if isRealm:
        resp = make_response({"message": msgErr}, codeErr, {
                             'WWW-Authenticate': f'Basic realm="{msgRealm}"'})
    return resp

def sqlRequestFormatJSON(QueryObject):
    ch_r = []
    for r in QueryObject.fetchall():
        ch_r.append(dict(zip(QueryObject.keys(),r)))
    return ch_r  

def checkAdmin(current_user: User) -> bool:
    if not current_user:
        return False
    return current_user.is_admin()
