# FlaskKit

A basic Flask framework to get you started quickly with web development. FlaskKit includes all the essential components you need to build a modern web application with minimal setup.

## Features

- 🚀 **Quick Setup** - Get started in minutes with pip install
- 🎨 **Modern UI** - Built with Bootstrap 5 for responsive design
- 📱 **Mobile Ready** - Responsive design that works on all devices
- 🔧 **Extensible** - Clean architecture with blueprints support
- 📝 **Form Handling** - Built-in form validation and flash messaging
- 🛡️ **Error Handling** - Custom 404 and 500 error pages
- 🔌 **API Ready** - Includes API endpoints and JSON responses
- ⚙️ **Configuration** - Environment-based configuration system

## Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone or download this repository**
   ```bash
   git clone <repository-url>
   cd flaskkit
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

## Project Structure

```
flaskkit/
├── app.py                 # Main Flask application
├── config.py             # Configuration settings
├── requirements.txt      # Python dependencies
├── templates/            # HTML templates
│   ├── base.html        # Base template
│   ├── index.html       # Home page
│   ├── about.html       # About page
│   ├── contact.html     # Contact page
│   ├── 404.html         # 404 error page
│   └── 500.html         # 500 error page
└── static/              # Static files
    ├── css/
    │   └── style.css    # Custom styles
    └── js/
        └── main.js      # JavaScript functionality
```

## Configuration

FlaskKit uses environment-based configuration. You can set the following environment variables:

- `FLASK_CONFIG` - Configuration to use (development, production, testing)
- `SECRET_KEY` - Secret key for sessions and CSRF protection
- `DATABASE_URL` - Database connection string
- `MAIL_SERVER` - Email server for sending emails
- `MAIL_USERNAME` - Email username
- `MAIL_PASSWORD` - Email password

### Example Environment Variables

```bash
export FLASK_CONFIG=production
export SECRET_KEY=your-secret-key-here
export DATABASE_URL=postgresql://user:password@localhost/flaskkit
```

## Available Routes

- `/` - Home page
- `/about` - About page
- `/contact` - Contact form
- `/api/health` - Health check API endpoint

## Customization

### Adding New Pages

1. Create a new template in the `templates/` directory
2. Add a route in `app.py`:

```python
@app.route('/new-page')
def new_page():
    return render_template('new_page.html', title='New Page')
```

### Adding New Static Files

Place CSS files in `static/css/` and JavaScript files in `static/js/`. Reference them in your templates:

```html
<link href="{{ url_for('static', filename='css/custom.css') }}" rel="stylesheet">
<script src="{{ url_for('static', filename='js/custom.js') }}"></script>
```

### Using Blueprints

For larger applications, organize your code using Flask blueprints:

1. Create a blueprint file (e.g., `blueprints/main.py`)
2. Register it in `app.py`:

```python
from blueprints.main import main_bp
app.register_blueprint(main_bp)
```

## Development

### Running in Development Mode

```bash
export FLASK_CONFIG=development
python app.py
```

### Running Tests

```bash
export FLASK_CONFIG=testing
python -m pytest
```

## Deployment

### Using Gunicorn

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

### Using Docker

Create a `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you have any questions or need help, please open an issue on GitHub.

---

**Happy coding! 🚀**
