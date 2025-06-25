from flask import Flask, redirect, render_template, request, flash, url_for
from datetime import datetime, date
import os
from config import config
from models import db, Order

def create_app(config_name=None):
    """Application factory pattern for production deployment"""
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'development')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    db.init_app(app)
    
    # Apply URL prefix if configured
    url_prefix = app.config.get('URL_PREFIX', '')
    
    # Register routes
    @app.route("/")
    def index():
        """Display all open orders"""
        orders = Order.query.filter(db.or_(Order.status == "pending", Order.status == "on_order")).order_by(Order.date_updated.desc()).all()
        return render_template("display.html", orders=orders, selected_status="open", search_text="")

    @app.route("/editOrder/<int:order_id>", methods=["GET", "POST"])
    def editOrder(order_id):
        """Edit an existing order"""
        order = Order.query.get_or_404(order_id)
        
        if request.method == "POST":
            # Update order from form data
            order.status = request.form.get("status", "pending")
            order.customer_name = request.form.get("customer_name")
            order.customer_phone = request.form.get("customer_phone")
            order.staff_member = request.form.get("staff_member")
            order.brand = request.form.get("brand")
            order.style = request.form.get("style")
            order.size = request.form.get("size")
            order.color = request.form.get("color")
            order.quantity = int(request.form.get("quantity", 1))
            order.notes = request.form.get("notes", "")
            order.date_updated = date.today()
            
            try:
                db.session.commit()
                flash("Order updated successfully!", "success")
            except Exception as e:
                db.session.rollback()
                flash("Error updating order. Please try again.", "error")
                print(f"Error updating order: {e}")
            
            return redirect(url_for('index'))
        
        return render_template("editOrder.html", order=order)

    @app.route("/createOrder", methods=["GET", "POST"])
    def createOrder():
        """Create a new order"""
        if request.method == "POST":
            try:
                new_order = Order.create_from_form(request.form)
                db.session.add(new_order)
                db.session.commit()
                flash("Order created successfully!", "success")
                return redirect(url_for('index'))
            except Exception as e:
                db.session.rollback()
                flash("Error creating order. Please try again.", "error")
                print(f"Error creating order: {e}")
        
        return render_template("createOrder.html")

    @app.route("/deleteOrder/<int:order_id>", methods=["GET"])
    def deleteOrder(order_id):
        """Delete an order"""
        order = Order.query.get_or_404(order_id)
        try:
            db.session.delete(order)
            db.session.commit()
            flash("Order deleted successfully!", "success")
        except Exception as e:
            db.session.rollback()
            flash("Error deleting order. Please try again.", "error")
            print(f"Error deleting order: {e}")
        
        return redirect(url_for('index'))

    @app.route("/search")
    def search():
        """Search orders by status and text"""
        status_filter = request.args.get("status", "")
        search_text = request.args.get("search", "")
        
        query = Order.query
        
        if status_filter:
            if status_filter == "open":
                # Open includes both pending and on_order
                query = query.filter(db.or_(Order.status == "pending", Order.status == "on_order"))
            else:
                query = query.filter(Order.status == status_filter)
                print(f"Applied status filter: {status_filter}")
    
        if search_text:
            search_filter = f"%{search_text}%"
            query = query.filter(
                db.or_(
                    Order.customer_name.ilike(search_filter),
                    Order.customer_phone.ilike(search_filter),
                    Order.brand.ilike(search_filter),
                    Order.style.ilike(search_filter),
                )
            )
            
        orders = query.order_by(Order.date_created.desc()).all()
        
        return render_template("display.html", orders=orders, 
                             selected_status=status_filter, search_text=search_text)
    
    # Configure application for URL prefix if needed
    if url_prefix:
        # Set the application root path
        app.config['APPLICATION_ROOT'] = url_prefix
        
        # Add a context processor to make url_prefix available in templates
        @app.context_processor
        def inject_url_prefix():
            return dict(url_prefix=url_prefix)
    
    return app

# For development server
if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=3001, debug=True)  