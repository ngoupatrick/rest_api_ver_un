
from . import *

#TODO: update serveur
class Consultation_SymptomeSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.Consultation_Symptome
        fields = ("pcsid", "description", "sid","cid")
        include_fk = True


class SymptomeSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.Symptome
        fields = ("psid", "intitule", "tsid","consultation_symptomes")
    symptomes = ma.Nested(Consultation_SymptomeSchema(many=True))


class Type_SymptomeSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.Type_Symptome
        fields = ("ptsid", "intitule", "symptomes")
    symptomes = ma.Nested(SymptomeSchema(many=True))


class ResultatSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.Resultat
        fields = ("prid", "code_resultat", "date_resultat","cid","uid")
        include_fk = True


class ConsultationSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.Consultation
        fields = ("pcid", "code_consul", "date_consul","motif","age_patient_annee","age_patient_mois","pid","uid","consultation_symptomes","resultats")
        include_fk = True
    consultation_symptomes = ma.Nested(Consultation_SymptomeSchema(many=True))
    resultats = ma.Nested(ResultatSchema(many=True))


class PatientSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.Patient
        fields = ("ppid", "patient_code", "nom","prenom","lieu_naiss","date_naiss","village","hameau","chef_de_concession","nom_mere","sexe","consultations")
    consultations = ma.auto_field()
    #consultations = ma.Nested(ConsultationSchema(many=True))


class UserSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.User
        fields = ("puid", "user_code", "login","etat","nom","prenom","lieu_naiss","date_naiss","sexe","adresse","tel","utid","stid","gid","consultations","resultats")
        include_fk = True
    consultations = ma.Nested(ConsultationSchema(many=True))
    resultats = ma.Nested(ResultatSchema(many=True))


class User_TypeSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.User_Type
        fields = ("putid", "intitule", "users")
    users = ma.Nested(UserSchema(many=True))


class GroupsSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.Groups
        fields = ("guid", "intitule", "description","access_perm","users")
    #users = ma.auto_field()
    users = ma.Nested(UserSchema(many=True))


class StructureSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.Structure
        fields = ("pstid", "immatriculation", "intitule","type_structure","users")
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
