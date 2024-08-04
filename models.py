from datetime import datetime
from app import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    matric_number = db.Column(db.String(20), unique=True, nullable=False)
    department = db.Column(db.String(100), nullable=False)
    level = db.Column(db.String(10), nullable=False)
    role = db.Column(db.String(10), default="user")
    dates = db.Column(db.PickleType, default=[datetime.now().strftime("%Y-%m-%d")])