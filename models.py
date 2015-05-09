from app import db

class Congregacao(db.Model):
    __tablename__ = 'congregacao'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String())

    def __repr__(self):
        return self.nome