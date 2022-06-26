from . import *


class SQLResource(Resource):
    @token_required
    def post(current_user: User, self):
        if not checkAdmin(current_user):
            return returnRep(msgErr='Cannot perform that function!', codeErr=401, isRealm=True, msgRealm="Login required!")        
        query = request.get_json().get("query", "")
        if not query:
            return returnRep(msgErr='Give a valid query', codeErr=404)
        return sqlRequestFormatJSON(db.engine.execute(query))
