from . import *

class SymptomesTypeResource(Resource):
    @token_required
    def get(current_user:User, self, ptsid=None):  
        if not checkAdmin(current_user):
            return jsonify({'message' : 'Cannot perform that function!'})        
        if ptsid:            
            u=Type_Symptome.query.filter_by(ptsid=ptsid).first_or_404(description='No Data Found!')
            data = type_Symptome_schema.dump(u)
        else:
            u=Type_Symptome.query.all()
            data = type_Symptomes_schema.dump(u)
        return data if data else jsonify({"error": "No Data found!"}, 404)
    
    @token_required
    def post(current_user:User,self):
        if not checkAdmin(current_user):
            return jsonify({'message' : 'Cannot perform that function!'})    
        json_data = request.get_json()
        ptsid = json_data.get("ptsid", "")
        if ptsid:  
            data=Type_Symptome.query.filter_by(ptsid=ptsid).first_or_404(description='Not Found!') 
        else:
            data = Type_Symptome(**json_data)
            data.save()
        return type_Symptome_schema.dump(data) if data else jsonify({"error": "Not found"}, 404)
    
    @token_required
    def put(current_user:User,self): 
        if not checkAdmin(current_user):
            return jsonify({'message' : 'Cannot perform that function!'}) 
        json_data = request.get_json()
        ptsid = json_data.get("ptsid","")
        data={}        
        if ptsid:
            data=Type_Symptome.query.filter_by(ptsid=ptsid)
            if data:                
                json_data['modified'] = datetime.now()
                data.update(json_data)
                db.session.commit()
        return Type_SymptomeSchema.dump(data.first_or_404(description='Not Found!')) if data else jsonify({"error": "Not found"}, 404)
