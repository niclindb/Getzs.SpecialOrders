from app import create_app
import os

def create_wsgi_app():
    """Create WSGI app with URL prefix support"""
    app = create_app('production')
    url_prefix = app.config.get('URL_PREFIX', '')
    
    if url_prefix:
        # Apply URL prefix using WSGI middleware
        from werkzeug.middleware.proxy_fix import ProxyFix
        from werkzeug.middleware.shared_data import SharedDataMiddleware
        
        # Handle proxy headers
        app.wsgi_app = ProxyFix(app.wsgi_app, x_prefix=1)
        
        # Create a new WSGI app that handles the URL prefix
        def prefix_app(environ, start_response):
            # Set the script name to include the prefix
            environ['SCRIPT_NAME'] = url_prefix
            return app(environ, start_response)
        
        return prefix_app
    
    return app

app = create_wsgi_app()

# For WSGI servers like Gunicorn or uWSGI
if __name__ == "__main__":
    app.run() 