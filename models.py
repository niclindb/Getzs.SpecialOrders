from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

db = SQLAlchemy()

class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.Date, default=date.today, nullable=False)
    date_updated = db.Column(db.Date, default=date.today, onupdate=date.today, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pending')
    customer_name = db.Column(db.String(100), nullable=False)
    customer_phone = db.Column(db.String(20), nullable=False)
    staff_member = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(50), nullable=False)
    style = db.Column(db.String(50), nullable=False)
    size = db.Column(db.String(10), nullable=False)
    color = db.Column(db.String(30), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    notes = db.Column(db.Text)
    
    def __repr__(self):
        return f'<Order {self.id}: {self.customer_name} - {self.style}>'
    
    def to_dict(self):
        """Convert order to dictionary for JSON serialization"""
        return {
            'id': self.id,
            'date_created': self.date_created.strftime('%m-%d-%Y'),
            'date_updated': self.date_updated.strftime('%m-%d-%Y'),
            'status': self.status,
            'customer_name': self.customer_name,
            'customer_phone': self.customer_phone,
            'staff_member': self.staff_member,
            'brand': self.brand,
            'style': self.style,
            'size': self.size,
            'color': self.color,
            'quantity': self.quantity,
            'notes': self.notes
        }
    
    @classmethod
    def create_from_form(cls, form_data):
        """Create a new order from form data"""
        return cls(
            customer_name=form_data.get('customer_name'),
            customer_phone=form_data.get('customer_phone'),
            staff_member=form_data.get('staff_member'),
            brand=form_data.get('brand'),
            style=form_data.get('style'),
            size=form_data.get('size'),
            color=form_data.get('color'),
            quantity=int(form_data.get('quantity', 1)),
            notes=form_data.get('notes', ''),
            status=form_data.get('status', 'pending')
        ) 