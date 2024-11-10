from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.Enum('Pending', 'Approved', 'Rejected', name='status_enum'), default='Pending')
    club_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class Room(db.Model):
    __tablename__ = 'rooms'
    id = db.Column(db.Integer, primary_key=True)
    room_name = db.Column(db.String(50), nullable=False)
    is_booked = db.Column(db.Boolean, default=False)

class Budget(db.Model):
    __tablename__ = 'budgets'
    id = db.Column(db.Integer, primary_key=True)
    club_name = db.Column(db.String(100), nullable=False)
    amount_requested = db.Column(db.Numeric(10, 2))
    status = db.Column(db.Enum('Pending', 'Approved', 'Rejected', name='budget_status_enum'), default='Pending')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class Communication(db.Model):
    __tablename__ = 'communications'
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(100), nullable=False)
    receiver = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())