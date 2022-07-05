from . import *


class GroupResource(Resource):
    # method_decorators=[token_required] 
    @token_required
    def get(current_user, self, guid=None):
        if not checkAdmin(current_user):
            return returnRep(msgErr='Cannot perform that function!', codeErr=401, isRealm=True, msgRealm="Login required!")
        if guid:
            g = Groups.query.filter_by(guid=guid).first_or_404(
                description='Not Found!')
            data = group_schema.dump(g)
        else:
            g = Groups.query.all()
            data = groups_schema.dump(g)  
        return data if data else returnRep(msgErr='Data Not found!', codeErr=404)

    @token_required
    def post(current_user, self):
        if not checkAdmin(current_user):
            return returnRep(msgErr='Cannot perform that function!', codeErr=401, isRealm=True, msgRealm="Login required!")
        json_data = request.get_json()
        guid = json_data.get("guid", "")

        if guid:
            data = Groups.query.filter_by(
                guid=guid).first_or_404(description='Data Not Found!')
        else:
            # TODO: CHECK INTITULE
            data = Groups(**json_data)
            data.save()
        return group_schema.dump(data) if data else returnRep(msgErr='Data Not found!', codeErr=404)

    @token_required
    def put(current_user, self):
        if not checkAdmin(current_user):
            return returnRep(msgErr='Cannot perform that function!', codeErr=401, isRealm=True, msgRealm="Login required!")
        json_data = request.get_json()
        guid = json_data.get("guid", "")
        data = {}
        if guid:
            data = Groups.query.filter_by(guid=guid)
            if data:
                json_data['modified'] = datetime.now()
                # TODO: CHECK INTITULE
                data.update(json_data)
                db.session.commit()
        return group_schema.dump(data.first_or_404(description='Not Found!')) if data else returnRep(msgErr='Data Not found!', codeErr=404)
