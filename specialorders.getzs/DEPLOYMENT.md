# Production Deployment Guide

## URL Prefix Configuration

To run the application under a specific path (e.g., `websites.com/specialOrders`):

### Environment Variable Setup

Set the `URL_PREFIX` environment variable:

```bash
export URL_PREFIX=/specialOrders
```

Or add to your `.env` file:
```env
URL_PREFIX=/specialOrders
```

### Web Server Configuration

#### Nginx Configuration Example

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location /specialOrders {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header X-Script-Name /specialOrders;
    }
}
```

#### Apache Configuration Example

```apache
<VirtualHost *:80>
    ServerName your-domain.com
    
    ProxyPreserveHost On
    ProxyPass /specialOrders http://127.0.0.1:8000/
    ProxyPassReverse /specialOrders http://127.0.0.1:8000/
    
    RequestHeader set X-Script-Name /specialOrders
</VirtualHost>
```

### Application Behavior

With `URL_PREFIX=/specialOrders` configured:
- The app will be accessible at `your-domain.com/specialOrders`
- All internal redirects will automatically include the prefix
- Static assets and templates will work correctly
- The app will handle the prefix transparently

## Database Setup

### Option 1: PostgreSQL (Recommended for Production)

1. Install PostgreSQL on your server
2. Create a database and user
3. Set environment variables:
```bash
export FLASK_ENV=production
export DATABASE_URL=postgresql://username:password@localhost/dbname
export SECRET_KEY=your-super-secret-production-key
```

### Option 2: MySQL

1. Install MySQL on your server
2. Create a database and user
3. Set environment variables:
```bash
export FLASK_ENV=production
export DATABASE_URL=mysql://username:password@localhost/dbname
export SECRET_KEY=your-super-secret-production-key
```

### Option 3: SQLite (Simple Deployment)

For simple deployments, SQLite works fine:
```bash
export FLASK_ENV=production
export DATABASE_URL=sqlite:///prod.db
export SECRET_KEY=your-super-secret-production-key
```

## Installation Steps

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Initialize the database:**
```bash
python init_db.py
```

3. **Run the application:**
```bash
python app.py
```

## Production Server Setup

### Using Gunicorn (Recommended)

1. Install Gunicorn:
```bash
pip install gunicorn
```

2. Create a WSGI entry point (wsgi.py):
```python
from app import create_app

app = create_app('production')
```

3. Run with Gunicorn:
```bash
gunicorn -w 4 -b 0.0.0.0:8000 wsgi:app
```

### Using uWSGI

1. Install uWSGI:
```bash
pip install uwsgi
```

2. Run with uWSGI:
```bash
uwsgi --http 0.0.0.0:8000 --module wsgi:app --processes 4
```

## Environment Variables

Create a `.env` file in your production directory:

```env
FLASK_ENV=production
DATABASE_URL=your-production-database-url
SECRET_KEY=your-super-secret-production-key
```

## Database Migration

To migrate from SQLite to PostgreSQL/MySQL:

1. Export data from SQLite:
```bash
python -c "
from app import create_app
from models import db, Order
app = create_app('development')
with app.app_context():
    orders = Order.query.all()
    for order in orders:
        print(order.to_dict())
"
```

2. Import to new database using the same structure

## Security Considerations

1. **Change the SECRET_KEY** in production
2. **Use HTTPS** in production
3. **Set up proper database permissions**
4. **Use environment variables** for sensitive data
5. **Enable database backups**

## Monitoring

Consider adding:
- Logging configuration
- Health check endpoints
- Database connection pooling
- Error monitoring (Sentry, etc.) 