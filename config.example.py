"""
Example configuration file for FlaskKit.
Copy this file to config_local.py and modify as needed.
"""

import os

# Example environment variables for development
# Copy these to your .env file or set them in your environment

# Flask Configuration
FLASK_CONFIG = 'development'
SECRET_KEY = 'your-secret-key-here'

# Database Configuration
DATABASE_URL = 'sqlite:///flaskkit.db'
DEV_DATABASE_URL = 'sqlite:///flaskkit_dev.db'

# Email Configuration (optional)
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'your-email@gmail.com'
MAIL_PASSWORD = 'your-app-password'

# Debug Mode
FLASK_DEBUG = True
