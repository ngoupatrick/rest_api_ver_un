from . import *

class StructureResource(Resource):
    @token_required
    def get(current_user:User, self, pstid=None):  
        if not checkAdmin(current_user):
            return jsonify({'message' : 'Cannot perform that function!'})        
        if pstid:            
            u=Structure.query.filter_by(pstid=pstid).first_or_404(description='No Data Found!')
            data = structure_schema.dump(u)
        else:
            u=Structure.query.all()
            data = structures_schema.dump(u)
        return data if data else jsonify({"error": "No Data found!"}, 404)
    
    @token_required
    def post(current_user:User,self):
        if not checkAdmin(current_user):
            return jsonify({'message' : 'Cannot perform that function!'})    
        json_data = request.get_json()
        pstid = json_data.get("pstid", "")
        if pstid:  
            data=Structure.query.filter_by(pstid=pstid).first_or_404(description='Not Found!') 
        else:
            data = Structure(**json_data)
            data.save()
        return structure_schema.dump(data) if data else jsonify({"error": "Not found"}, 404)
    
    @token_required
    def put(current_user:User,self): 
        if not checkAdmin(current_user):
            return jsonify({'message' : 'Cannot perform that function!'}) 
        json_data = request.get_json()
        pstid = json_data.get("pstid","")
        data={}        
        if pstid:
            data=Structure.query.filter_by(pstid=pstid)
            if data:                
                json_data['modified'] = datetime.now()
                data.update(json_data)
                db.session.commit()
        return structure_schema.dump(data.first_or_404(description='Not Found!')) if data else jsonify({"error": "Not found"}, 404)

    