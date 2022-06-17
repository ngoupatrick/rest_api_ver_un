from . import *

class GroupResource(Resource):
    #method_decorators=[token_required]
    @token_required
    def get(current_user:User, self, guid=None):          
        if not checkAdmin(current_user):
            return jsonify({'message' : 'Cannot perform that function!'})
        if guid:            
            g=Groups.query.filter_by(guid=guid).first_or_404(description='Not Found!')
            data = group_schema.dump(g)
        else:
            g=Groups.query.all()
            data = groups_schema.dump(g) 
        return data if data else jsonify({"error": "Not found!"}, 404)
    
    @token_required
    def post(current_user:User,self):
        if not checkAdmin(current_user):
            return jsonify({'message' : 'Cannot perform that function!'})    
        json_data = request.get_json()
        guid = json_data.get("guid", "")
        
        if guid:  
            data=Groups.query.filter_by(guid=guid).first_or_404(description='Not Found!') 
        else:
            #TODO: CHECK INTITULE
            data = Groups(**json_data)
            data.save()    
        return group_schema.dump(data) if data else jsonify({"error": "Not found"}, 404)
    
    @token_required
    def put(current_user:User,self): 
        if not checkAdmin(current_user):
            return jsonify({'message' : 'Cannot perform that function!'}) 
        json_data = request.get_json()
        guid = json_data.get("guid","")
        data={}        
        if guid:
            data=Groups.query.filter_by(guid=guid)
            if data:                
                json_data['modified'] = datetime.now()
                #TODO: CHECK INTITULE
                data.update(json_data)
                db.session.commit()
        return group_schema.dump(data.first_or_404(description='Not Found!')) if data else jsonify({"error": "Not found"}, 404)
