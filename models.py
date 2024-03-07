from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy

class TableModel (db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    table_number = db.Column(db.Integer)
    capacity = db.Column(db.Integer)
    status = db.Column(db.String)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'))

class CustomerModel(db.Model): 
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    phone_number = db.Column(db.Integer, unique=True)
    # status = db.Column(db.String, nullable=False)

class OrderModel(db.Model):
    __tablename__= 'orders'

    id = db.Column(db.Integer, primary_key=True)
    order_date = db.Column(db.DateTime, server_default=db.func.now())
    total_amount = db.Column(db.Integer)
    status = db.Column(db.String, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    table_id = db.Column(db.Integer, db.ForeignKey('tables.id'))

class MenuItemsModel(db.Model):
    __tablename__ = 'menuItems'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    description = db.Column(db.String)
    price = db.Column(db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

class CategoryModel(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    image_url=db.Column(db.String, nullable=False)
    
class StaffModel(db.Model):
    __tablename__= 'staff'

    id = db.Column(db.Integer, primary_key=True)
    first_name=db.Column(db.String(50),nullable=False)
    last_name=db.Column(db.String(50),nullable=False)
    role=db.Column(db.String(50),nullable=False)
    hire_date = db.Column(db.DateTime, server_default=db.func.now())

class ReservationModel(db.Model):
    __tablename__ = 'reservations'

    id = db.Column(db.Integer, primary_key=True)
    reservation_date = db.Column(db.DateTime, server_default=db.func.now())
    reservation_time = db.Column(db.DateTime, server_default=db.func.now())
    party_size = db.Column(db.Integer)
    customer_id= db.Column(db.Integer, db.ForeignKey('customers.id'))
    table_id= db.Column(db.Integer, db.ForeignKey('tables.id'))


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
    


