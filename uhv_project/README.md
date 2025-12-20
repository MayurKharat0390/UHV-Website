# Universal Human Values (UHV) Department Platform

The official academic platform for the UHV Department, designed to cultivate ethical, responsible, and harmonious individuals.

## Tech Stack
- **Backend:** Django 5.x / 4.x
- **Database:** SQLite
- **Frontend:** HTML5, Tailwind CSS (via CDN), Alpine.js, HTMX
- **Authentication:** Django Auth

## Features
- **Daily Reflection:** Interactive ethical scenarios with feedback.
- **Values Mapping:** Visual guide to living values in Family, College, Society, and Profession.
- **Digital Journal:** Private, secure weekly reflections for students.
- **Student Voices:** Moderated testimonials and reflections.
- **Activities Dashboard:** Tracking social initiatives.
- **Faculty Profiles:** Mentor philosophy and details.

## Installation & Setup

### Prerequisites
- Python 3.8+ installed.

### Quick Start (Windows PowerShell)
1. Run the setup script:
   ```powershell
   ./setup_project.ps1
   ```
2. Start the server:
   ```powershell
   python manage.py runserver
   ```
3. Open browser at `http://127.0.0.1:8000/`.

### Manual Setup
1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Apply Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
3. **Seed Data (Optional):**
   ```bash
   python seed_data.py
   ```
4. **Create Admin User:**
   ```bash
   python manage.py createsuperuser
   ```
5. **Run Server:**
   ```bash
   python manage.py runserver
   ```

## Admin Panel
Access the admin panel at `http://127.0.0.1:8000/admin/` to manage:
- Reflections (Scenarios)
- Student Voices (Approve/Reject)
- Activities
- Faculty

## Project Structure
- `uhv_project/`: Main settings.
- `core/`: Landing page and static content.
- `reflections/`: Daily scenario logic.
- `journals/`: Private student journals.
- `activities/`: Social work dashboard.
- `voices/`: Student citations.
- `faculty/`: Mentor profiles.
- `users/`: Authentication.
- `templates/`: HTML templates with Tailwind.

---
*Calm, ethical, and reflective.*
