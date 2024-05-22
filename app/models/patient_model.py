from database import db

class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    ci = db.Column(db.String(20), nullable=False)
    birth_date = db.Column(db.String(20), nullable=False)

    def __init__(self, name, lastname, ci, birth_date):
        self.name = name
        self.lastname = lastname
        self.ci = ci
        self.birth_date = birth_date

    @staticmethod
    def get_all():
        return Patient.query.all()

    @staticmethod
    def get_by_id(id):
        return Patient.query.get(id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
