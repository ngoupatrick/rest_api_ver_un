from . import *

class ConsultationSymptomeResource(Resource):
    @token_required
    def get(current_user:User, self, pcsid=None):  
        if not checkAdmin(current_user):
            return returnRep(msgErr='Cannot perform that function!', codeErr=401, isRealm=True, msgRealm="Login required!")       
        if pcsid:            
            u=Consultation_Symptome.query.filter_by(pcsid=pcsid).first_or_404(description='No Data Found!')
            data = consultation_symptome_schema.dump(u)
        else:
            u=Consultation_Symptome.query.all()
            data = consultation_symptomes_schema.dump(u)
        return data if data else returnRep(msgErr='Data Not found!', codeErr=404)
    
    @token_required
    def post(current_user:User,self):
        if not checkAdmin(current_user):
            return returnRep(msgErr='Cannot perform that function!', codeErr=401, isRealm=True, msgRealm="Login required!")
        json_data = request.get_json()
        pcsid = json_data.get("pcsid", "")
        if pcsid:  
            data=Consultation_Symptome.query.filter_by(pcsid=pcsid).first_or_404(description='Not Found!') 
        else:
            data = Consultation_Symptome(**json_data)
            data.save()
        return consultation_symptome_schema.dump(data) if data else returnRep(msgErr='Data Not found!', codeErr=404)
    
    @token_required
    def put(current_user:User,self): 
        if not checkAdmin(current_user):
            return returnRep(msgErr='Cannot perform that function!', codeErr=401, isRealm=True, msgRealm="Login required!")
        json_data = request.get_json()        
        pcsid = json_data.get("pcsid","")
        data={}        
        if pcsid:
            data=Consultation_Symptome.query.filter_by(pcsid=pcsid)
            if data:                
                json_data['modified'] = datetime.now()
                data.update(json_data)
                db.session.commit()
        return consultation_symptome_schema.dump(data.first_or_404(description='Not Found!')) if data else returnRep(msgErr='Data Not found!', codeErr=404)
