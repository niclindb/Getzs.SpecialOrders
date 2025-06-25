from app import create_app
from models import db, Order

def test_database():
    app = create_app()
    
    with app.app_context():
        # Check total orders
        total_orders = Order.query.count()
        print(f"Total orders in database: {total_orders}")
        
        # List all orders
        orders = Order.query.all()
        for order in orders:
            print(f"Order {order.id}: {order.customer_name} - {order.status}")
        
        # Test search by status
        pending_orders = Order.query.filter(Order.status == "pending").all()
        print(f"Pending orders: {len(pending_orders)}")
        
        # Test search by text
        john_orders = Order.query.filter(Order.customer_name.ilike("%John%")).all()
        print(f"Orders with 'John' in name: {len(john_orders)}")

if __name__ == "__main__":
    test_database() 