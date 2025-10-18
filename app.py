from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import os
from datetime import datetime
from config import config

def create_app(config_name=None):
    """Application factory pattern for Flask app creation."""
    app = Flask(__name__)
    
    # Configuration
    config_name = config_name or os.environ.get('FLASK_CONFIG', 'default')
    app.config.from_object(config[config_name])
    
    # Register blueprints (if any)
    # from app.blueprints.main import main_bp
    # app.register_blueprint(main_bp)
    
    return app

# Create the Flask app instance
app = create_app()

@app.route('/')
def index():
    """Home page route."""
    return render_template('index.html', title='Home')

@app.route('/about')
def about():
    """About page route."""
    return render_template('about.html', title='About')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page route with form handling."""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Basic form validation
        if not name or not email or not message:
            flash('All fields are required!', 'error')
        else:
            # Here you would typically save to database or send email
            flash(f'Thank you {name}! Your message has been sent.', 'success')
            return redirect(url_for('contact'))
    
    return render_template('contact.html', title='Contact')

@app.route('/api/health')
def health_check():
    """API endpoint for health check."""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'version': '1.0.0'
    })

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return render_template('404.html', title='Page Not Found'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return render_template('500.html', title='Internal Server Error'), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
