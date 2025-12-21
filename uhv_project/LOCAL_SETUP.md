# 🔧 Local Development Setup

## Setting Up Environment Variables

For local development, create a `.env` file in the project root with these settings:

```env
# Django Settings
SECRET_KEY=django-insecure-uhv-academic-platform-dev-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (leave empty to use SQLite in development)
# DATABASE_URL=
```

**Note**: The `.env` file is gitignored for security. Never commit it to version control.

## Installation Steps

1. **Create and activate virtual environment**:
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Create .env file** (copy from .env.example):
```bash
Copy-Item .env.example .env
```

4. **Run migrations**:
```bash
python manage.py migrate
```

5. **Create superuser**:
```bash
python manage.py createsuperuser
```

6. **Run development server**:
```bash
python manage.py runserver
```

7. **Access the site**:
- Main site: http://localhost:8000
- Admin panel: http://localhost:8000/admin

## Development vs Production

- **Development**: Uses SQLite database, DEBUG=True, no HTTPS required
- **Production (Railway)**: Uses PostgreSQL, DEBUG=False, HTTPS enabled, security headers active

The settings.py automatically detects the environment based on the `DATABASE_URL` variable.
