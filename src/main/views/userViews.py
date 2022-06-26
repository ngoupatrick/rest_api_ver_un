from . import *


class UserResource(Resource):
    # method_decorators=[token_required]
    @token_required
    def get(current_user: User, self, puid=None):
        if not checkAdmin(current_user):
            return returnRep(msgErr='Cannot perform that function!', codeErr=401, isRealm=True, msgRealm="Login required!")
        if puid:
            u = User.query.filter_by(puid=puid).first_or_404(
                description='Not Found!')
            data = user_schema.dump(u)
        else:
            u = User.query.all()
            data = users_schema.dump(u)
        return data if data else returnRep(msgErr='Data Not found!', codeErr=404)

    @token_required
    def post(current_user: User, self):
        if not checkAdmin(current_user):
            return returnRep(msgErr='Cannot perform that function!', codeErr=401, isRealm=True, msgRealm="Login required!")
        json_data = request.get_json()
        puid = json_data.get("puid", "")
        if puid:
            data = User.query.filter_by(puid=puid).first_or_404(
                description='Not Found!')
        else:
            # TODO: CHECK GID
            data = User(**json_data)
            data.save()
        return user_schema.dump(data) if data else returnRep(msgErr='Data Not found!', codeErr=404)

    @token_required
    def put(current_user: User, self):
        if not checkAdmin(current_user):
            return returnRep(msgErr='Cannot perform that function!', codeErr=401, isRealm=True, msgRealm="Login required!")
        json_data = request.get_json()
        puid = json_data.get("puid", "")
        data = {}
        if puid:
            data = User.query.filter_by(puid=puid)
            if data:
                json_data['modified'] = datetime.now()
                # TODO: CHECK GID
                data.update(json_data)
                db.session.commit()
        return user_schema.dump(data.first_or_404(description='Not Found!')) if data else returnRep(msgErr='Data Not found!', codeErr=404)
