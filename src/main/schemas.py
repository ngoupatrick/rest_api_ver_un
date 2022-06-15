from . import ma
from main import models


class PersonneSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.Personne
        
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
        
class StructueSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.Structue
        
class ResultatSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.Resultat
        
class UserSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.User

personne_schema = PersonneSchema()
personnes_schema = PersonneSchema(many=True)
user_schema = UserSchema()
users_schema = UserSchema(many=True)
group_schema = GroupsSchema()
groups_schema = GroupsSchema(many=True)
type_Symptome_schema = Type_SymptomeSchema()
types_Symptome_schema = Type_SymptomeSchema(many=True)
symptome_schema = SymptomeSchema()
symptome_schema = SymptomeSchema(many=True)
