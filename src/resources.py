from src.models import Personne, User
from src.schemas import personne_schema, personnes_schema, user_schema, users_schema
from flask import request, jsonify  
from src import db
from flask_restful import Resource  # type:ignore
import json
from datetime import datetime


class PersonneResource(Resource):
    def get(self, eid=None):
        if eid:
            data = personne_schema.dump(Personne.query.get_or_404(eid))
        else:
            data = personnes_schema.dump(Personne.query.all())
        return jsonify(data)

    def post(self):
        json_data = json.loads(request.data.decode("utf-8"))
        nom = json_data.get("nom", "")
        ville = json_data.get("ville", "")
        eid = json_data.get("id_personne",0)
        
        if eid:  
            data=Personne.query.get_or_404(eid) 
        else:
            data = Personne(nom=nom, ville=ville)
            db.session.add(data)
            db.session.commit()
            
        return personne_schema.dump(data)

    def put(self):
        # For updates
        json_data = json.loads(request.data.decode("utf-8"))
        eid = json_data.get("id_personne",0)
        data={}
        if eid:
            data=Personne.query.get_or_404(eid)
            nom = json_data.get("nom", "")
            ville = json_data.get("ville", "")
            if nom:
                data.nom=nom
            if ville:
                data.ville=ville
            data.modified = datetime.now()
            db.session.commit()
        return personne_schema.dump(data)


class UserResource(Resource):
    def get(self, eid=None):
        if eid:
            data = user_schema.dump(User.query.get_or_404(eid))
        else:
            data = users_schema.dump(User.query.all())
        return jsonify(data)

    def post(self):
        json_data = json.loads(request.data.decode("utf-8"))
        id_personne = json_data.get("id_personne", 0)
        login = json_data.get("login", "")
        pass_hash = json_data.get("pass_hash", "")
        eid = json_data.get("id_user",0)
        
        if eid:
            data = User.query.get_or_404(eid)
        else:
            data = User(id_personne=id_personne,login=login, pass_hash=pass_hash)
            db.session.add(data)
            db.session.commit()
            
        return user_schema.dump(data)

    def put(self):
        # For updates
        json_data = json.loads(request.data.decode("utf-8"))
        eid = json_data.get("id_user",0)
        data={}
        if eid:
            data=User.query.get_or_404(eid)
            login = json_data.get("login", "")
            pass_hash = json_data.get("pass_hash", "")
            id_personne = json_data.get("id_personne", 0)
            if login:
                data.login=login
            if pass_hash:
                data.pass_hash=pass_hash
            if id_personne:
                data.id_personne=id_personne
            data.modified = datetime.now()
            db.session.commit()
        return user_schema.dump(data)
