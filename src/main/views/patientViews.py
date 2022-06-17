from . import *

class PatientResource(Resource):
    #method_decorators=[token_required]
    @token_required
    def get(current_user:User, self, ppid=None):          
        if not checkAdmin(current_user):
            return jsonify({'message' : 'Cannot perform that function!'})        
        if ppid:            
            u=Patient.query.filter_by(ppid=ppid).first_or_404(description='No Data Found!')
            data = patient_schema.dump(u)
        else:
            u=Patient.query.all()
            data = patients_schema.dump(u)  
        return data if data else jsonify({"error": "No Data Found!"}, 404)
    
    @token_required
    def post(current_user:User,self):
        if not checkAdmin(current_user):
            return jsonify({'message' : 'Cannot perform that function!'})    
        json_data = request.get_json()
        ppid = json_data.get("ppid", "")
        if ppid:  
            data=Patient.query.filter_by(ppid=ppid).first_or_404(description='No Data Found!') 
        else:
            data = Patient(**json_data)
            data.save()
        return patient_schema.dump(data) if data else jsonify({"error": "No Data Found"}, 404)
    
    @token_required
    def put(current_user:User,self): 
        if not checkAdmin(current_user):
            return jsonify({'message' : 'Cannot perform that function!'}) 
        json_data = request.get_json()
        ppid = json_data.get("ppid","")
        data={}        
        if ppid:
            data=Patient.query.filter_by(ppid=ppid)
            if data:                
                json_data['modified'] = datetime.now()
                data.update(json_data)
                db.session.commit()
        return patient_schema.dump(data.first_or_404(description='No Data Found!')) if data else jsonify({"error": "No Data Found"}, 404)

    