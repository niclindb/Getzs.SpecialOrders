from app import create_app, db
from models import Order
from datetime import datetime

def init_database():
    """Initialize the database with tables and sample data"""
    app = create_app()
    
    with app.app_context():
        # Create all tables
        db.create_all()
        print("Database tables created successfully!")
        
        # Check if we already have data
        if Order.query.first() is None:
            # Add sample data
            sample_orders = [
                Order(
                    customer_name="John Doe",
                    customer_phone="123-456-7890",
                    staff_member="John Doe",
                    brand="Nike",
                    style="shirt",
                    size="M",
                    color="red",
                    quantity=1,
                    notes="This is a note",
                    status="pending"
                ),
                Order(
                    customer_name="Jane Doe",
                    customer_phone="123-456-7890",
                    staff_member="John Doe",
                    brand="Adidas",
                    style="shirt",
                    size="M",
                    color="red",
                    quantity=1,
                    notes="This is a note",
                    status="on_order"
                )
            ]
            
            for order in sample_orders:
                db.session.add(order)
            
            db.session.commit()
            print("Sample data added successfully!")
        else:
            print("Database already contains data, skipping sample data creation.")

if __name__ == '__main__':
    init_database() 