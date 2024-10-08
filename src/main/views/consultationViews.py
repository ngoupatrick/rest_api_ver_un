from . import *

class ConsultationResource(Resource):
    #method_decorators=[token_required]
    @token_required
    def get(current_user:User, self, pcid=None):          
        if not checkAdmin(current_user):
            return returnRep(msgErr='Cannot perform that function!', codeErr=401, isRealm=True, msgRealm="Login required!")
        if pcid:            
            g=Consultation.query.filter_by(pcid=pcid).first_or_404(description='Not Found!')
            data = consultation_schema.dump(g)
        else:
            g=Consultation.query.all()
            data = consultations_schema.dump(g) 
        return data if data else returnRep(msgErr='Data Not found!', codeErr=404)
    
    @token_required
    def post(current_user:User,self):
        if not checkAdmin(current_user):
            return returnRep(msgErr='Cannot perform that function!', codeErr=401, isRealm=True, msgRealm="Login required!")    
        json_data = request.get_json()
        pcid = json_data.get("pcid", "")
        
        if pcid:  
            data=Consultation.query.filter_by(pcid=pcid).first_or_404(description='Not Found!') 
        else:
            # TODO: CHECK DATE_CONSUL
            mois = json_data.pop("mois", None)
            annee = json_data.pop("annee", None)
            jour = json_data.pop("jour", None)
            date_consul = transformDate(jour_=jour, mois_=mois, annee_=annee)
            if date_consul:
                json_data["date_consul"] = date_consul
            # TODO: Ajout des données
            data = Consultation(**json_data)
            data.save()    
        return consultation_schema.dump(data) if data else returnRep(msgErr='Data Not found!', codeErr=404)
    
    @token_required
    def put(current_user:User,self): 
        if not checkAdmin(current_user):
            return returnRep(msgErr='Cannot perform that function!', codeErr=401, isRealm=True, msgRealm="Login required!") 
        json_data = request.get_json()
        #TODO: update serveur
        json_data.pop("consultation_symptomes", None)
        json_data.pop("resultats", None)
        json_data.pop("date_consul", None)
        pcid = json_data.get("pcid","")
        data={}        
        if pcid:
            data=Consultation.query.filter_by(pcid=pcid)
            if data:                
                json_data['modified'] = datetime.now()
                # TODO: CHECK DATE_CONSUL
                mois = json_data.pop("mois", None)
                annee = json_data.pop("annee", None)
                jour = json_data.pop("jour", None)
                date_consul = transformDate(jour_=jour, mois_=mois, annee_=annee)
                if date_consul:
                    json_data["date_consul"] = date_consul
                # TODO: MAJ des données
                data.update(json_data)
                db.session.commit()
        return consultation_schema.dump(data.first_or_404(description='Not Found!')) if data else returnRep(msgErr='Data Not found!', codeErr=404)
