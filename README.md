# UHV Website - Universal Human Values Department

Official website for the Universal Human Values (UHV) Department, built with Django.

## 🚀 Quick Deploy to Railway

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new)

This project is configured for one-click deployment to Railway.

### Environment Variables Required

Set these in Railway:

```
SECRET_KEY=<generate-a-secure-key>
DEBUG=False
ALLOWED_HOSTS=.railway.app
```

Generate a SECRET_KEY:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Post-Deployment Steps

1. Add PostgreSQL database in Railway
2. Create superuser via Railway terminal:
   ```bash
   cd uhv_project && python manage.py createsuperuser
   ```

## 📁 Project Structure

```
UHV-Website/
├── Procfile                  # Railway startup
├── runtime.txt               # Python version
├── railway.json              # Build config
├── requirements.txt          # Dependencies
└── uhv_project/              # Django project
    ├── manage.py
    ├── uhv_project/          # Settings
    ├── core/                 # Core app
    ├── users/                # User management
    ├── reflections/          # Daily reflections
    ├── journals/             # Student journals
    ├── activities/           # Activities
    ├── voices/               # Student testimonials
    ├── faculty/              # Faculty profiles
    ├── quotes/               # Daily quotes
    ├── resources/            # Resources
    ├── progress/             # Progress tracking
    ├── templates/            # HTML templates
    └── static/               # Static files
```

## 🛠️ Local Development

See `uhv_project/LOCAL_SETUP.md` for detailed instructions.

Quick start:
```bash
cd uhv_project
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## 📚 Documentation

- **Deployment Guide**: `uhv_project/RAILWAY_DEPLOYMENT.md`
- **Local Setup**: `uhv_project/LOCAL_SETUP.md`
- **Admin Guide**: `uhv_project/ADMIN_GUIDE.md`

## 🔐 Features

- Daily Reflections Engine
- Student Journals with streak tracking
- Activities Dashboard
- Student Voices/Testimonials
- Faculty Profiles
- Resource Library
- Progress Tracking
- Admin Dashboard (Jazzmin UI)

## 🌐 Tech Stack

- **Backend**: Django 5.0
- **Database**: PostgreSQL (production), SQLite (development)
- **Server**: Gunicorn
- **Static Files**: WhiteNoise
- **Admin UI**: Jazzmin
- **Frontend**: HTMX, Vanilla CSS

## 📄 License

Academic project for Universal Human Values Department.
