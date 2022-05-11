from src import db


class Personne(db.Model):  # type:ignore    
    id_personne = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    modified = db.Column(db.DateTime, server_default=db.func.now())
    nom = db.Column(db.String(128), unique=True, nullable=False)
    ville = db.Column(db.String(128), default="")

    def __repr__(self):
        rslt = {
            "id_personne": self.id_personne,
            "created":self.created,
            "modified":self.modified,
            "nom": self.nom,
            "ville":self.ville
            }
        return f'<Personne: {rslt}>'

class User(db.Model):  # type:ignore    
    id_user = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    modified = db.Column(db.DateTime, server_default=db.func.now())
    id_personne = db.Column(db.Integer, default=0)
    login = db.Column(db.String(60), unique=True, nullable=False)
    pass_hash = db.Column(db.String(128), nullable=False)
    def __repr__(self):
        rslt = {
            "id_user": self.id_personne,
            "created":self.created,
            "modified":self.modified,
            "id_personne": self.id_personne,
            "login":self.login,
            "pass_hash":self.pass_hash
            }
        return f'<User: {rslt}>'

db.create_all()
