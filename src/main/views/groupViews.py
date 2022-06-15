from main.models import Groups,User
from main.schemas import group_schema, groups_schema
from flask import request, jsonify
from main import db
from flask_restful import Resource  # type:ignore
import json
from datetime import datetime

from main.views.utils import token_required, checkAdmin

class GroupResource(Resource):
    @token_required
    def get(current_user:User, self, guid=None):          
        if not checkAdmin(current_user):
            return jsonify({'message' : 'Cannot perform that function!'})
        g=None
        if guid:
            g=Groups.query.get_or_404(guid)
            data = group_schema.dump(g)
        else:
            g=Groups.query.all()
            data = groups_schema.dump(g)        
        return jsonify(data) if data else jsonify({"error": "Not found!"}, 404)
    
    @token_required
    def post(current_user:User,self):
        if not checkAdmin(current_user):
            return jsonify({'message' : 'Cannot perform that function!'})    
        json_data = request.get_json()
        guid = json_data.get("guid", "")
        intitule = json_data.get("intitule", "")
        description = json_data.get("description", "")
        access_perm = json_data.get("access_perm","")
        
        if guid:  
            data=Groups.query.get_or_404(guid) 
        else:
            data = Groups(intitule=intitule, description=description,access_perm=access_perm)
            db.session.add(data)
            db.session.commit()
            
        return group_schema.dump(data) if data else jsonify({"error": "Not found"}, 404)
    
    @token_required
    def put(current_user:User,self):        
        # For updates
        if not checkAdmin(current_user):
            return jsonify({'message' : 'Cannot perform that function!'}) 
        json_data = request.get_json()
        guid = json_data.get("guid","")
        data={}
        if guid:
            data=Groups.query.get_or_404(guid)
            intitule = json_data.get("intitule", "")
            description = json_data.get("description", "")
            access_perm = json_data.get("access_perm", "")
            
            if intitule: data.intitule=intitule
            if description: data.ville=description
            if access_perm: data.ville=access_perm
            
            data.modified = datetime.now()
            db.session.commit()
        return group_schema.dump(data) if data else jsonify({"error": "Not found"}, 404)
