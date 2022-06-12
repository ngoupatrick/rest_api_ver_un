from main.models import Personne, User
from main.schemas import personne_schema, personnes_schema, user_schema, users_schema
from flask import request, jsonify  
from . import db
from flask_restful import Resource  # type:ignore
import json
from datetime import datetime

from main.views.utils import token_required

@token_required
class PersonneResource(Resource):
    def get(self, eid=None):
        p=None
        if eid:
            p=Personne.query.get_or_404(eid)
            data = personne_schema.dump(p)
        else:
            p=Personne.query.all()
            data = personnes_schema.dump(p)
        breakpoint()
        return jsonify(data) if data else jsonify({"error": "Not found"}, 404)

    def post(self):
        json_data = json.loads(request.data.decode("utf-8"))
        nom = json_data.get("nom", "")
        ville = json_data.get("ville", "")
        eid = json_data.get("pid",0)
        
        if eid:  
            data=Personne.query.get_or_404(eid) 
        else:
            data = Personne(nom=nom, ville=ville)
            db.session.add(data)
            db.session.commit()
            
        return personne_schema.dump(data) if data else jsonify({"error": "Not found"}, 404)

    def put(self):
        # For updates
        json_data = json.loads(request.data.decode("utf-8"))
        eid = json_data.get("pid",0)
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
        return personne_schema.dump(data) if data else jsonify({"error": "Not found"}, 404)


class UserResource(Resource):
    def get(self, eid=None):
        if eid:
            data = user_schema.dump(User.query.get_or_404(eid))
        else:
            data = users_schema.dump(User.query.all())
        return jsonify(data) #if data else jsonify({"error": "Not found"}, 404)

    def post(self):
        json_data = json.loads(request.data.decode("utf-8"))
        pid = json_data.get("pid", 0)
        login = json_data.get("login", "")
        pass_hash = json_data.get("pass_hash", "")
        eid = json_data.get("uid",0)
        
        if eid:
            data = User.query.get_or_404(eid)
        else:
            data = User(pid=pid,login=login, pass_hash=pass_hash)
            db.session.add(data)
            db.session.commit()
            
        return user_schema.dump(data) if data else jsonify({"error": "Not found"}, 404)

    def put(self):
        # For updates
        json_data = json.loads(request.data.decode("utf-8"))
        eid = json_data.get("uid",0)
        data={}
        if eid:
            data=User.query.get_or_404(eid)
            login = json_data.get("login", "")
            pass_hash = json_data.get("pass_hash", "")
            pid = json_data.get("pid", 0)
            if login:
                data.login=login
            if pass_hash:
                data.pass_hash=pass_hash
            if pid:
                data.pid=pid
            data.modified = datetime.now()
            db.session.commit()
        return user_schema.dump(data) if data else jsonify({"error": "Not found"}, 404)
