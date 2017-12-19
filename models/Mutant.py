from mutantDetector import db
from datetime import datetime

class Mutant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dna = db.Column(db.String(41), unique=False, nullable=False)
    isMutant = db.Column(db.Boolean, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, dna):
        self.dna = "-".join(dna)

    def __repr__(self):
        return '<Mutant %r>' % self.dna
