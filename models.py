from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import check_password_hash

db=SQLAlchemy

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number=db.Column(db.String(),unique=True)
    address = db.Column(db.String(64))
    role=db.Column(db.String(30), default='member')
    password = db.Column(db.String(64))
    created_at=db.Column(db.TIMESTAMP(),default=db.func.now())
    updated_at=db.Column(db.TIMESTAMP(),onupdate=db.func.now())
    products=db.relationship("ProductModel", backref="users",lazy=True) 
    reviews=db.relationship("ReviewModel", backref="users", lazy=True)
    orders=db.relationship("OrderModel",backref="users",lazy=True)
 
    def check_password(self, plain_password):
        return check_password_hash(self.password, plain_password)

    def to_json(self):
        return {
            'id': self.id,
            'role': self.role,
        }
    
class OrderModel(db.Model):
    __tablename__= 'orders'

    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, server_default=db.func.now())
    total_amount = db.Column(db.Integer)
    status = db.Column(db.String, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))

class ProductModel(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.Text)
    price = db.Column(db.Integer)
    image_url=db.Column(db.String, nullable=False)
    stock_quantity = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    reviews = db.relationship("ReviewModel", backref="products", lazy=True)

class CategoryModel(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    image_url=db.Column(db.String, nullable=False)
    

class ReviewModel(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)
    comment = db.Column(db.String)
    customer_id= db.Column(db.Integer, db.ForeignKey('customers.id'))
    table_id= db.Column(db.Integer, db.ForeignKey('tables.id'))


class PaymentModel(db.Model):
    __tablename__ = 'payments'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float)
    payment_type = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    


