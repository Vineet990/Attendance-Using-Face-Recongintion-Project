# -*- encoding: utf-8 -*-

from sqlalchemy import false
from .. import db
from .._base_model_class import ModelClass

class Attendance(db.Model, ModelClass):

    __tablename__ = "attendance"

    ID    = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
    Name = db.Column(db.String(255), nullable = False)
    DOA = db.Column(db.Date,nullable = False)

    def __to_dict__(self):
        _original = super().__to_dict__()
        for c in ["DOA"]:
            _original[c] = str(_original[c])
        
        return _original
