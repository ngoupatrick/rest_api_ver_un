from . import *


class ResultatResource(Resource):
    # method_decorators=[token_required]
    @token_required
    def get(current_user: User, self, prid=None):
        if not checkAdmin(current_user):
            return returnRep(msgErr='Cannot perform that function!', codeErr=401, isRealm=True, msgRealm="Login required!")
        if prid:
            g = Resultat.query.filter_by(
                prid=prid).first_or_404(description='Not Found!')
            data = resultat_schema.dump(g)
        else:
            g = Resultat.query.all()
            data = resultats_schema.dump(g)
        return data if data else returnRep(msgErr='Data Not found!', codeErr=404)

    @token_required
    def post(current_user: User, self):
        if not checkAdmin(current_user):
            return returnRep(msgErr='Cannot perform that function!', codeErr=401, isRealm=True, msgRealm="Login required!")
        json_data = request.get_json()
        prid = json_data.get("prid", "")

        if prid:
            data = Resultat.query.filter_by(
                prid=prid).first_or_404(description='Not Found!')
        else:
            # TODO: CHECK DATE_RESULTAT
            mois = json_data.pop("mois", None)
            annee = json_data.pop("annee", None)
            jour = json_data.pop("jour", None)
            date_resultat = transformDate(jour_=jour, mois_=mois, annee_=annee)
            if date_resultat:
                json_data["date_resultat"] = date_resultat
            data = Resultat(**json_data)
            data.save()
        return resultat_schema.dump(data) if data else returnRep(msgErr='Data Not found!', codeErr=404)

    @token_required
    def put(current_user: User, self):
        if not checkAdmin(current_user):
            return returnRep(msgErr='Cannot perform that function!', codeErr=401, isRealm=True, msgRealm="Login required!")
        json_data = request.get_json()
        prid = json_data.get("prid", "")
        data = {}
        if prid:
            data = Resultat.query.filter_by(prid=prid)
            if data:
                json_data['modified'] = datetime.now()
                # TODO: CHECK DATE_NAISS
                mois = json_data.pop("mois", None)
                annee = json_data.pop("annee", None)
                jour = json_data.pop("jour", None)
                date_resultat = transformDate(jour_=jour, mois_=mois, annee_=annee)
                if date_resultat:
                    json_data["date_resultat"] = date_resultat
                data.update(json_data)
                db.session.commit()
        return resultat_schema.dump(data.first_or_404(description='Not Found!')) if data else returnRep(msgErr='Data Not found!', codeErr=404)
