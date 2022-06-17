from . import *

class ConsultationResource(Resource):
    #method_decorators=[token_required]
    @token_required
    def get(current_user:User, self, pcid=None):          
        if not checkAdmin(current_user):
            return jsonify({'message' : 'Cannot perform that function!'})
        if pcid:            
            g=Consultation.query.filter_by(pcid=pcid).first_or_404(description='Not Found!')
            data = consultation_schema.dump(g)
        else:
            g=Consultation.query.all()
            data = consultations_schema.dump(g) 
        return data if data else jsonify({"error": "Not found!"}, 404)
    
    @token_required
    def post(current_user:User,self):
        if not checkAdmin(current_user):
            return jsonify({'message' : 'Cannot perform that function!'})    
        json_data = request.get_json()
        pcid = json_data.get("pcid", "")
        
        if pcid:  
            data=Consultation.query.filter_by(pcid=pcid).first_or_404(description='Not Found!') 
        else:
            data = Consultation(**json_data)
            data.save()    
        return consultation_schema.dump(data) if data else jsonify({"error": "Not found"}, 404)
    
    @token_required
    def put(current_user:User,self): 
        if not checkAdmin(current_user):
            return jsonify({'message' : 'Cannot perform that function!'}) 
        json_data = request.get_json()
        pcid = json_data.get("pcid","")
        data={}        
        if pcid:
            data=Consultation.query.filter_by(pcid=pcid)
            if data:                
                json_data['modified'] = datetime.now()
                data.update(json_data)
                db.session.commit()
        return consultation_schema.dump(data.first_or_404(description='Not Found!')) if data else jsonify({"error": "Not found"}, 404)
