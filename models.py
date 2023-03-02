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
    role = db.relationship("Role")
     

    
class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(80), nullable=False)
    created = db.Column(db.Date, default=datetime.utcnow)
    modified = db.Column(db.Date, default=datetime.utcnow)



class Morada(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User')
    add_line1 = db.Column(db.String(80), nullable=False)
    add_line2 = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    postal_code = db.Column(db.String(80), nullable=False)
    created = db.Column(db.Date, default=datetime.utcnow)
    modified = db.Column(db.Date, default=datetime.utcnow)


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User')
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    created = db.Column(db.Date, default=datetime.utcnow)
    modified = db.Column(db.Date, default=datetime.utcnow)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    created = db.Column(db.Date, default=datetime.utcnow)
    modified = db.Column(db.Date, default=datetime.utcnow)
    inventory = db.Column(db.Integer, nullable=False)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    created = db.Column(db.Date, default=datetime.utcnow)
    modified = db.Column(db.Date, default=datetime.utcnow)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product = db.relationship('Product')
    image = db.Column(db.String(80), nullable=False)
    created = db.Column(db.Date, default=datetime.utcnow)
    modified = db.Column(db.Date, default=datetime.utcnow)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User')
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product = db.relationship('Product')
    payment_gateway_id = db.Column(db.Integer, db.ForeignKey('payment_gateway.id'), nullable=False)
    created = db.Column(db.Date, default=datetime.utcnow)
    modified = db.Column(db.Date, default=datetime.utcnow)


class PaymentGateway(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(80), nullable=False)
    created = db.Column(db.Date, default=datetime.utcnow)
    modified = db.Column(db.Date, default=datetime.utcnow)
    