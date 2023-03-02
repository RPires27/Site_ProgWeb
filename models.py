from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(80), nullable=False)
    created = db.Column(db.Date, default=datetime.utcnow)
    role_id = db.Column(db.String(80), db.ForeignKey("role.role"))

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(80), nullable=False)
    created = db.Column(db.Date, default=datetime.utcnow)
    modified = db.Column(db.Date, default=datetime.utcnow)
    user = db.relationship("User", backref="role")

class Morada(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(80), nullable=False)
    postal_code = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('addresses', lazy=True))

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Integer, nullable=False)

class Carrinho(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #product_id = db.Column(db.Integer, nullable=False)
    #product_name = db.Column(db.Integer, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('produto.id'), nullable=False)
    product_name = db.Column(db.Integer, db.ForeignKey('produto.name'), nullable=False)
    product_price = db.Column(db.Integer, db.ForeignKey('produto.price'), nullable=False)

