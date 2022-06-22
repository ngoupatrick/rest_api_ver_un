from . import *


class SymptomeResource(Resource):
    @token_required
    def get(current_user: User, self, psid=None):
        if not checkAdmin(current_user):
            return returnRep(msgErr='Cannot perform that function!', codeErr=401, isRealm=True, msgRealm="Login required!")
        if psid:
            u = Symptome.query.filter_by(psid=psid).first_or_404(
                description='No Data Found!')
            data = symptome_schema.dump(u)
        else:
            u = Symptome.query.all()
            data = symptomes_schema.dump(u)
        return data if data else returnRep(msgErr='Data Not found!', codeErr=404)

    @token_required
    def post(current_user: User, self):
        if not checkAdmin(current_user):
            return returnRep(msgErr='Cannot perform that function!', codeErr=401, isRealm=True, msgRealm="Login required!")
        json_data = request.get_json()
        psid = json_data.get("psid", "")
        if psid:
            data = Symptome.query.filter_by(
                psid=psid).first_or_404(description='Not Found!')
        else:
            data = Symptome(**json_data)
            data.save()
        return symptome_schema.dump(data) if data else returnRep(msgErr='Data Not found!', codeErr=404)

    @token_required
    def put(current_user: User, self):
        if not checkAdmin(current_user):
            return returnRep(msgErr='Cannot perform that function!', codeErr=401, isRealm=True, msgRealm="Login required!")
        json_data = request.get_json()
        psid = json_data.get("psid", "")
        data = {}
        if psid:
            data = Symptome.query.filter_by(psid=psid)
            if data:
                json_data['modified'] = datetime.now()
                data.update(json_data)
                db.session.commit()
        return SymptomeSchema.dump(data.first_or_404(description='Not Found!')) if data else returnRep(msgErr='Data Not found!', codeErr=404)
