# models.py
from app import db

class ExcelData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.JSON)

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    parameters = db.Column(db.JSON)
    generated_at = db.Column(db.DateTime, nullable=False)

class Chart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    parameters = db.Column(db.JSON)
    generated_at = db.Column(db.DateTime, nullable=False)

