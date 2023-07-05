from sqlalchemy import Column, Integer, String
from app import db


class Pegawai(db.Model):
    __tablename__ = "pegawai"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    date = Column(String(50))
    created_at = db.Column(db.String(10))

    def __repr__(self):
        return "<Pegawai {}>".format(self.name)
