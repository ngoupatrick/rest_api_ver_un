from src import ma
from src import models


class PersonneSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.Personne
        
class UserSchema(ma.SQLAlchemyAutoSchema):  # type:ignore
    class Meta:
        model = models.User

personne_schema = PersonneSchema()
personnes_schema = PersonneSchema(many=True)
user_schema = UserSchema()
users_schema = UserSchema(many=True)
