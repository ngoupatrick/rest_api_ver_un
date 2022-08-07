from . import *

# Class type of symptom


class Type_Symptome(db.Model):
    __tablename__ = "type_symptome"
    tsid = db.Column(db.Integer, primary_key=True)
    ptsid = db.Column(db.String(50), unique=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    modified = db.Column(db.DateTime, server_default=db.func.now())
    intitule = db.Column(db.String, unique=True, nullable=False)
    symptomes = db.relationship(
        'Symptome', backref='Type_Symptome', lazy=True, uselist=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ptsid = str(uuid.uuid4())

    def __repr__(self):
        rslt = {
            "tsid": self.tsid,
            "ptsid": self.ptsid,
            "created": self.created,
            "modified": self.modified,
            "intitule": self.intitule,
            "symptomes": self.symptomes
        }
        return f'<Type_Symptome: {rslt}>'

    def save(self):
        db.session.add(self)
        db.session.commit()


class Symptome(db.Model):
    __tablename__ = "symptome"
    sid = db.Column(db.Integer, primary_key=True)
    psid = db.Column(db.String(50), unique=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    modified = db.Column(db.DateTime, server_default=db.func.now())
    intitule = db.Column(db.String, nullable=False)
    tsid = db.Column(db.Integer, db.ForeignKey(
        'type_symptome.tsid'), nullable=False)
    consultation_symptomes = db.relationship(  # au vu de la definition, est-ce utile?
        'Consultation_Symptome', backref='Symptome', lazy=True, uselist=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.psid = str(uuid.uuid4())

    def __repr__(self):
        rslt = {
            "sid": self.sid,
            "psid": self.psid,
            "tsid": self.tsid,
            "created": self.created,
            "modified": self.modified,
            "intitule": self.intitule,
            "symptomes": self.consultation_symptomes
        }
        return f'<Symptome: {rslt}>'

    def save(self):
        db.session.add(self)
        db.session.commit()


class Consultation_Symptome(db.Model):
    __tablename__ = "consultation_symptome"
    csid = db.Column(db.Integer, primary_key=True)
    pcsid = db.Column(db.String(50), unique=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    modified = db.Column(db.DateTime, server_default=db.func.now())
    description = db.Column(db.Text, default='')
    sid = db.Column(db.Integer, db.ForeignKey('symptome.sid'), nullable=False)
    cid = db.Column(db.Integer, db.ForeignKey(
        'consultation.cid'), nullable=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pcsid = str(uuid.uuid4())

    def __repr__(self):
        rslt = {
            "csid": self.csid,
            "pcsid": self.pcsid,
            "sid": self.sid,
            "cid": self.cid,
            "created": self.created,
            "modified": self.modified,
            "description": self.description
        }
        return f'<Consultation_Symptome: {rslt}>'

    def save(self):
        db.session.add(self)
        db.session.commit()


class Consultation(db.Model):  # NOT YET FINISHED!!!
    __tablename__ = "consultation"
    cid = db.Column(db.Integer, primary_key=True)
    pcid = db.Column(db.String(50), unique=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    modified = db.Column(db.DateTime, server_default=db.func.now())
    code_consul = db.Column(db.String, unique=True, nullable=False)
    date_consul = db.Column(db.DateTime, server_default=db.func.now())
    motif = db.Column(db.Text, default='')
    age_patient_annee = db.Column(db.Integer, default=0)
    age_patient_mois = db.Column(db.Integer, default=0)
    # Foreignkeys
    pid = db.Column(db.Integer, db.ForeignKey('patient.pid'), nullable=False)
    uid = db.Column(db.Integer, db.ForeignKey('user.uid'), nullable=False)
    # liste des symptomes recensés lors de cette consultation
    consultation_symptomes = db.relationship(
        'Consultation_Symptome', backref='Consultation', lazy=True, uselist=True)
    # liste des resultats associés à cette consultation
    resultats = db.relationship(
        'Resultat', backref='Consultation', lazy=True, uselist=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pcid = str(uuid.uuid4())
        self.code_consul = str(uuid.uuid4())

    def __repr__(self):
        rslt = {
            "cid": self.cid,
            "pid": self.pid,
            "created": self.created,
            "modified": self.modified,
            "motif": self.motif,
            "age_patient_annee": self.age_patient_annee,
            "age_patient_mois": self.age_patient_mois,
            "consultation_symptomes": self.consultation_symptomes,
            "resultats": self.resultats,
        }
        return f'<Consultation: {rslt}>'

    def save(self):
        db.session.add(self)
        db.session.commit()


class Patient(db.Model):
    __tablename__ = "patient"
    pid = db.Column(db.Integer, primary_key=True)
    ppid = db.Column(db.String(50), unique=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    modified = db.Column(db.DateTime, server_default=db.func.now())
    patient_code = db.Column(db.String, unique=True, nullable=False)
    nom = db.Column(db.String, nullable=False)
    prenom = db.Column(db.String, default='')
    lieu_naiss = db.Column(db.String, default='')
    date_naiss = db.Column(db.Date, server_default=db.func.now())
    village = db.Column(db.String, default='')
    hameau = db.Column(db.String, default='')
    chef_de_concession = db.Column(db.String, default='')
    nom_mere = db.Column(db.String, default='')
    sexe = db.Column(db.String, default='M', nullable=False)
    # listes des consultations associées à ce patient
    consultations = db.relationship(
        'Consultation', backref='Patient', lazy=True, uselist=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ppid = str(uuid.uuid4())
        self.patient_code = str(uuid.uuid4())

    def __repr__(self):

        rslt = {
            "pid": self.pid,
            "ppid": self.ppid,
            "created": self.created,
            "modified": self.modified,
            "patient_code": self.patient_code,
            "nom": self.nom,
            "prenom": self.prenom,
            "lieu_naiss": self.lieu_naiss,
            "date_naiss": self.date_naiss,
            "village": self.village,
            "hameau": self.hameau,
            "chef_de_concession": self.chef_de_concession,
            "nom_mere": self.nom_mere,
            "sexe": self.sexe,
            "consultations": self.consultations,
        }
        return f'<Patient: {rslt}>'

    def save(self):
        db.session.add(self)
        db.session.commit()


class User_Type(db.Model):
    __tablename__ = "user_type"
    utid = db.Column(db.Integer, primary_key=True)
    putid = db.Column(db.String(50), unique=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    modified = db.Column(db.DateTime, server_default=db.func.now())
    intitule = db.Column(db.String, unique=True, nullable=False)
    # list of all users of this type
    users = db.relationship(
        'User', backref='User_Type', lazy=True, uselist=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.putid = str(uuid.uuid4())

    def __repr__(self):
        rslt = {
            "utid": self.utid,
            "created": self.created,
            "modified": self.modified,
            "intitule": self.intitule,
            "users": self.users,
        }
        return f'<User_Type: {rslt}>'

    def save(self):
        db.session.add(self)
        db.session.commit()


class Groups(db.Model):
    __tablename__ = "groups"
    gid = db.Column(db.Integer, primary_key=True)
    guid = db.Column(db.String(50), unique=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    modified = db.Column(db.DateTime, server_default=db.func.now())
    intitule = db.Column(db.String, unique=True, nullable=False)
    description = db.Column(db.Text, default='')
    access_perm = db.Column(db.Text, default='')
    # list of all users of this group
    users = db.relationship(
        'User', backref='Groups', lazy=True, uselist=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.guid = str(uuid.uuid4())

    def __repr__(self):
        rslt = {
            "guid": self.guid,
            "created": self.created,
            "modified": self.modified,
            "intitule": self.intitule,
            "description": self.description,
            "access_perm": self.access_perm,
            "users": self.users,
        }
        return f'<Groups: {rslt}>'

    def save(self):
        db.session.add(self)
        db.session.commit()


class Structure(db.Model):
    __tablename__ = "structure"
    stid = db.Column(db.Integer, primary_key=True)
    pstid = db.Column(db.String(50), unique=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    modified = db.Column(db.DateTime, server_default=db.func.now())
    immatriculation = db.Column(db.String, unique=True, nullable=False)
    intitule = db.Column(db.String, unique=True, nullable=False)
    type_structure = db.Column(db.String, default='', nullable=False)
    # list of all users of this structure
    users = db.relationship(
        'User', backref='Structure', lazy=True, uselist=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pstid = str(uuid.uuid4())

    def generate_immatriculation():
        return str(uuid.uuid4())

    def __repr__(self):
        rslt = {
            "stid": self.stid,
            "pstid": self.pstid,
            "created": self.created,
            "modified": self.modified,
            "intitule": self.intitule,
            "immatriculation": self.immatriculation,
            "type_structure": self.type_structure,
            "users": self.users,
        }
        return f'<Structue: {rslt}>'

    def save(self):
        db.session.add(self)
        db.session.commit()


class User(db.Model):
    __tablename__ = "user"
    uid = db.Column(db.Integer, primary_key=True)
    puid = db.Column(db.String(50), unique=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    modified = db.Column(db.DateTime, server_default=db.func.now())
    user_code = db.Column(db.String, unique=True, nullable=False)
    # au cas où certains users n'aient paas acces au systeme
    login = db.Column(db.String(60), default="", nullable=False)
    # ici, user est confondu avec une personne
    pass_hash = db.Column(db.String(128), default="", nullable=False)
    etat = db.Column(db.Boolean, default=True, nullable=False)
    nom = db.Column(db.String, nullable=False)
    prenom = db.Column(db.String, default='')
    lieu_naiss = db.Column(db.String, default='')
    date_naiss = db.Column(db.DateTime, server_default=db.func.now())
    sexe = db.Column(db.String, default='M', nullable=False)
    adresse = db.Column(db.Text, default='')
    tel = db.Column(db.String, default='')

    # Foreignkeys
    utid = db.Column(db.Integer, db.ForeignKey(
        'user_type.utid'), default=0, nullable=True)
    stid = db.Column(db.Integer, db.ForeignKey(
        'structure.stid'), default=0, nullable=True)
    gid = db.Column(db.Integer, db.ForeignKey('groups.gid'), nullable=False)

    # listes des consultations édités par cet user
    consultations = db.relationship(
        'Consultation', backref='User', lazy=True, uselist=True)
    # listes des resultats édités à cet user
    resultats = db.relationship(
        'Resultat', backref='User', lazy=True, uselist=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pass_hash = generate_password_hash(kwargs.get('pass_hash'))
        self.puid = str(uuid.uuid4())
        self.user_code = str(uuid.uuid4())

    def save(self):
        db.session.add(self)
        db.session.commit()

    @property
    def password(self):
        raise AttributeError("password is not readable attribute")

    @password.setter
    def password(self, password):
        self.pass_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_hash, password)

    def is_active(self):
        return self.etat

    def activate(self):
        self.etat = True

    def is_admin(self):
        return True

    def generate_token(self, minutes=600):
        from flask import current_app as app  # type:ignore
        content = {
            'puid': self.puid,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=minutes)
        }
        token = jwt.encode(
            content, app.config['SECRET_KEY']
        )
        return token

    @staticmethod
    def verify_token(token):
        from flask import current_app as app  # type:ignore
        try:
            data = jwt.decode(
                token, app.config['SECRET_KEY'], algorithms=['HS256']
            )
        except jwt.exceptions.InvalidSignatureError as e:
            raise e
        except jwt.exceptions.ExpiredSignatureError as e:
            raise e
        except:
            return None
        current_user = User.query.filter_by(puid=data['puid']).first()
        return current_user

    def __repr__(self):
        rslt = {
            "uid": self.uid,
            "utid": self.utid,
            "stid": self.stid,
            "gid": self.gid,
            "created": self.created,
            "modified": self.modified,
            "user_code": self.user_code,
            "login": self.login,
            "pass_hash": self.pass_hash,
            "etat": self.etat,
            "nom": self.nom,
            "prenom": self.prenom,
            "lieu_naiss": self.lieu_naiss,
            "date_naiss": self.date_naiss,
            "sexe": self.sexe,
            "adresse": self.adresse,
            "tel": self.tel,
            "resultats": self.resultats,
            "consultations": self.consultations,
        }
        return f'<User: {rslt}>'


class Resultat(db.Model):  # NOT YET FINISHED!!!
    __tablename__ = "resultat"
    rid = db.Column(db.Integer, primary_key=True)
    prid = db.Column(db.String(50), unique=True)
    created = db.Column(db.DateTime, server_default=db.func.now())
    modified = db.Column(db.DateTime, server_default=db.func.now())
    code_resultat = db.Column(db.String, unique=True, nullable=False)
    date_resultat = db.Column(db.DateTime, server_default=db.func.now())
    # Foreignkeys
    cid = db.Column(db.Integer, db.ForeignKey(
        'consultation.cid'), nullable=False)
    uid = db.Column(db.Integer, db.ForeignKey('user.uid'), nullable=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.prid = str(uuid.uuid4())
        self.code_resultat = str(uuid.uuid4())

    def __repr__(self):
        rslt = {
            "rid": self.rid,
            "prid": self.prid,
            "cid": self.cid,
            "uid": self.uid,
            "created": self.created,
            "modified": self.modified,
            "code_resultat": self.code_resultat,
            "date_resultat": self.date_resultat,
        }
        return f'<Resultat: {rslt}>'

    def save(self):
        db.session.add(self)
        db.session.commit()
