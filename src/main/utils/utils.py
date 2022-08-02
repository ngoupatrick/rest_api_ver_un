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


def returnRepJSON(JsonErr, codeErr, isRealm=False, msgRealm="Login required!"):
    resp = make_response(JsonErr, codeErr)
    if isRealm:
        resp = make_response(JsonErr, codeErr, {
                             'WWW-Authenticate': f'Basic realm="{msgRealm}"'})
    return resp


def sqlRequestFormatJSON(QueryObject):
    ch_r = []
    for r in QueryObject.fetchall():
        ch_r.append(dict(zip(QueryObject.keys(), r)))
    return ch_r


def checkAdmin(current_user: User) -> bool:
    if not current_user:
        return False
    return current_user.is_admin()

# En fonction du sexe, retourne F ou M


def transformSexe(sexe_):
    sexe = None
    if sexe_:
        if sexe_.lower() in ["f", "femme", "feminin", "féminin"]:
            sexe = "F"
        if sexe_.lower() in ["m", "homme", "masculin"]:
            sexe = "M"
    return sexe

# transformons la date(jour, mois, année) en date python


def transformDate(jour_, mois_, annee_):
    from datetime import date
    date_naiss = None
    if (mois_ and annee_ and jour_):  # une date a été spécifiée
        try:
            mois = int(mois_)
            annee = int(annee_)
            jour = int(jour_)
            date_naiss = date(year=annee, month=mois, day=jour)
        except Exception as e:
            print(e)
            date_naiss = None
    return date_naiss
