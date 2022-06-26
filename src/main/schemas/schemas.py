
from . import *


class Consultation_SymptomeSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.Consultation_Symptome
        include_fk = True


class SymptomeSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.Symptome
    symptomes = ma.Nested(Consultation_SymptomeSchema(many=True))


class Type_SymptomeSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.Type_Symptome
    symptomes = ma.Nested(SymptomeSchema(many=True))


class ResultatSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.Resultat
        include_fk = True


class ConsultationSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.Consultation
        include_fk = True
    consultation_symptomes = ma.Nested(Consultation_SymptomeSchema(many=True))
    resultats = ma.Nested(ResultatSchema(many=True))


class PatientSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.Patient
    consultations = ma.auto_field()
    #consultations = ma.Nested(ConsultationSchema(many=True))


class UserSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.User
        include_fk = True
    consultations = ma.Nested(ConsultationSchema(many=True))
    resultats = ma.Nested(ResultatSchema(many=True))


class User_TypeSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.User_Type
    users = ma.Nested(UserSchema(many=True))


class GroupsSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.Groups
    #users = ma.auto_field()
    users = ma.Nested(UserSchema(many=True))


class StructureSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.Structure
    users = ma.Nested(UserSchema(many=True))


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
