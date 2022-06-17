from main import ma
from main.models import models


class Type_SymptomeSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.Type_Symptome
        
class SymptomeSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.Symptome
        
class Consultation_SymptomeSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.Consultation_Symptome
        
class ConsultationSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.Consultation
        
class PatientSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.Patient
        
class User_TypeSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.User_Type
        
class GroupsSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.Groups
        
class ResultatSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.Resultat
        
class UserSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.User

class StructureSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.Structure

group_schema = GroupsSchema()
groups_schema = GroupsSchema(many=True)
user_schema = UserSchema()
users_schema = UserSchema(many=True)
structure_schema = StructureSchema()
structures_schema = StructureSchema(many=True)
user_type_schema = User_TypeSchema()
user_types_schema = User_TypeSchema(many=True)
patient_schema = PatientSchema()
patients_schema = PatientSchema(many=True)
type_Symptome_schema = Type_SymptomeSchema()
type_Symptomes_schema = Type_SymptomeSchema(many=True)
symptome_schema = SymptomeSchema()
symptomes_schema = SymptomeSchema(many=True)
consultation_symptome_schema = Consultation_SymptomeSchema()
consultation_symptomes_schema = Consultation_SymptomeSchema(many=True)
resultat_schema = ResultatSchema()
resultats_schema = ResultatSchema(many=True)
consultation_schema = ConsultationSchema()
consultations_schema = ConsultationSchema(many=True)

