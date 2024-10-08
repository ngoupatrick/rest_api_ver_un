from . import *


class PatientResource(Resource):
    # method_decorators=[token_required]
    @token_required
    def get(current_user: User, self, ppid=None):
        if not checkAdmin(current_user):
            return returnRep(msgErr='Cannot perform that function!', codeErr=401, isRealm=True, msgRealm="Login required!")
        if ppid:
            u = Patient.query.filter_by(ppid=ppid).first_or_404(
                description='No Data Found!')
            data = patient_schema.dump(u)
        else:
            u = Patient.query.all()
            data = patients_schema.dump(u)
        return data if data else returnRep(msgErr='Data Not found!', codeErr=404)

    @token_required
    def post(current_user: User, self):  
        #breakpoint()      
        if not checkAdmin(current_user):
            return returnRep(msgErr='Cannot perform that function!', codeErr=401, isRealm=True, msgRealm="Login required!")
        try:
            json_data = request.get_json()
        except Exception as e:
            return returnRep(msgErr=e, codeErr=404) 
        ppid = json_data.get("ppid", "")
        if ppid:
            data = Patient.query.filter_by(ppid=ppid).first_or_404(
                description='No Data Found!')
        else:
            # TODO: CHECK DATE_NAISS
            mois = json_data.pop("mois", None)
            annee = json_data.pop("annee", None)
            jour = json_data.pop("jour", None)
            date_naiss = transformDate(jour_=jour, mois_=mois, annee_=annee)
            if date_naiss:
                json_data["date_naiss"] = date_naiss
            # TODO: CHECK SEXE
            sexe = json_data.pop("sexe", None)
            sexe = transformSexe(sexe_=sexe)
            if sexe:
                json_data["sexe"] = sexe
            # TODO: Ajout des données
            data = Patient(**json_data)
            data.save()
        return patient_schema.dump(data) if data else returnRep(msgErr='Data Not found!', codeErr=404)

    @token_required
    def put(current_user: User, self):
        if not checkAdmin(current_user):
            return returnRep(msgErr='Cannot perform that function!', codeErr=401, isRealm=True, msgRealm="Login required!")
        json_data = request.get_json()
        #TODO: update serveur
        json_data.pop("consultations", None)
        json_data.pop("date_naiss", None) # TODO: A SUPPRIMER       
        ppid = json_data.get("ppid", "")
        data = {}
        if ppid:
            data = Patient.query.filter_by(ppid=ppid)
            if data:
                json_data['modified'] = datetime.now()
                # TODO: CHECK DATE_NAISS
                mois = json_data.pop("mois", None)
                annee = json_data.pop("annee", None)
                jour = json_data.pop("jour", None)
                date_naiss = transformDate(jour_=jour, mois_=mois, annee_=annee)
                if date_naiss:
                    json_data["date_naiss"] = date_naiss
                # TODO: CHECH SEXE
                sexe = json_data.pop("sexe", None)
                sexe = transformSexe(sexe_=sexe)
                if sexe:
                    json_data["sexe"] = sexe
                # TODO: MAJ des données
                data.update(json_data)
                db.session.commit()
        return patient_schema.dump(data.first_or_404(description='No Data Found!')) if data else returnRep(msgErr='Data Not found!', codeErr=404)
    
   
