from . import *


class UserTypeResource(Resource):
    @token_required
    def get(current_user: User, self, putid=None):
        if not checkAdmin(current_user):
            return returnRep(msgErr='Cannot perform that function!', codeErr=401, isRealm=True, msgRealm="Login required!")
        if putid:
            u = User_Type.query.filter_by(putid=putid).first_or_404(
                description='No Data Found!')
            data = user_type_schema.dump(u)
        else:
            u = User_Type.query.all()
            data = user_types_schema.dump(u)
        return data if data else returnRep(msgErr='Data Not found!', codeErr=404)

    @token_required
    def post(current_user: User, self):
        if not checkAdmin(current_user):
            return returnRep(msgErr='Cannot perform that function!', codeErr=401, isRealm=True, msgRealm="Login required!")
        json_data = request.get_json()
        putid = json_data.get("putid", "")
        if putid:
            data = User_Type.query.filter_by(
                putid=putid).first_or_404(description='Not Found!')
        else:
            data = User_Type(**json_data)
            data.save()
        return user_type_schema.dump(data) if data else returnRep(msgErr='Data Not found!', codeErr=404)

    @token_required
    def put(current_user: User, self):
        if not checkAdmin(current_user):
            return returnRep(msgErr='Cannot perform that function!', codeErr=401, isRealm=True, msgRealm="Login required!")
        json_data = request.get_json()
        #TODO: update serveur
        json_data.pop("users", None)
        putid = json_data.get("putid", "")
        data = {}
        if putid:
            data = User_Type.query.filter_by(putid=putid)
            if data:
                json_data['modified'] = datetime.now()
                data.update(json_data)
                db.session.commit()
        return user_type_schema.dump(data.first_or_404(description='Not Found!')) if data else returnRep(msgErr='Data Not found!', codeErr=404)
