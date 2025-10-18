#!/usr/bin/env python3

from app import app

if __name__ == '__main__':
    print("Starting FlaskKit application...")
    print("Server will be available at: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    app.run(host='0.0.0.0', port=5000, debug=True)
