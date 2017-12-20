from config.database import Base
from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime



class Mutant(Base):
    __tablename__ = 'mutant'
    id = Column(Integer, primary_key=True)
    dna = Column(String(41), unique=False, nullable=False)
    isMutant = Column(Boolean, nullable=False)
    date = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, dna):
        self.dna = "-".join(dna)

    def __repr__(self):
        return '<Mutant %r>' % self.dna
