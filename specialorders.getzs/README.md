# Special Order System for Getz's

A modern, web-based order management system built with Flask and SQLAlchemy for tracking special orders with real-time status updates.

## Features

- **Order Management**: Create, edit, and track special orders
- **Advanced Search**: Filter orders by status, staff member, customer, brand, or style
- **Status Tracking**: Monitor orders through pending, on order, and completed states
- **Modern UI**: Responsive design with professional styling and intuitive navigation
- **Database Backend**: SQLite database with SQLAlchemy ORM for reliable data storage
- **Production Ready**: WSGI configuration for deployment


## Technology Stack

- **Backend**: Python 3.x with Flask framework
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Modern CSS with gradients, shadows, and responsive design

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone git@github.com:niclindb/Getzs.SpecialOrders.git
   cd specialorders.getzs
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**
   ```bash
   python init_db.py
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

## Usage

### Viewing Orders
- The main page displays all pending and on-order items by default
- Use the search bar to filter orders by various criteria
- Click on any order row to edit the order

### Creating Orders
- Click the "Create Order" button to add a new order
- Fill in all required fields
- Submit to save the order

### Editing Orders
- Click on any order in the table to edit
- Modify fields as needed
- Save changes to update the order

### Searching Orders
- Use the search form to filter orders by:
  - Status (pending, on order, completed, open)
  - Staff member
  - Customer name
  - Brand
  - Style

## Development

### Project Structure
```
specialorders.getzs/
├── app.py              # Main Flask application
├── config.py           # Configuration settings
├── models.py           # Database models
├── init_db.py          # Database initialization
├── requirements.txt    # Python dependencies
├── wsgi.py            # Production WSGI entry point
├── static/            # Static assets (CSS, images)
└── templates/         # HTML templates
    ├── display.html   # Main order display page
    ├── createOrder.html # Order creation form
    └── editOrder.html  # Order editing form
```

### Database Schema
The system uses a single `Order` table with the following fields:
- `id` (Primary Key)
- `staff_member`, `customer`, `brand`, `style`, `size`, `color` (Text fields)
- `status` (Enum: pending, on_order, completed)
- `notes` (Text field)
- `date_created`, `last_modified` (Date fields)

## Deployment

For production deployment, see `DEPLOYMENT.md` for detailed instructions on:
- Environment configuration
- Database setup
- WSGI server configuration
- Security considerations

## License

This project is proprietary software for Getz's business use. 
