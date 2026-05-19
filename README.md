# harjoitustyo_eljuja – Django Ticketing App

A Django-based ticketing / ticket sales web application created as part of my Software Developer studies at Taitotalo.

This was a group project, but I was the only team member with prior coding skills, so I implemented the core application logic end-to-end (from project setup to the main features) and maintained the codebase in GitHub.

## What this project demonstrates
- Practical Python & Django development in a real, working application
- Building data models and application workflows
- Structuring a Django project in a maintainable way
- Using Git/GitHub for version control

## Tech stack
- Python
- Django
- HTML (templates)
- Database: SQLite (default) / (update if you used something else)

## Features (high level)
- Ticketing workflow (create/manage tickets, basic ticket handling)
- Admin interface for managing data (Django admin)

> Note: This is a learning project, so the focus is on demonstrating backend fundamentals and end-to-end implementation rather than production hardening.

## Getting started (local development)
1. Clone the repository
   ```bash
   git clone https://github.com/Elinaoj/harjoitustyo_eljuja.git
   cd harjoitustyo_eljuja
   
1. Create and activate a virtual environment
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate

2. Install dependencies
    pip install -r requirements.txt

3. Run migrations and start the server
    python manage.py migrate
    python manage.py runserver

4. Open the app in your browser:
    http://127.0.0.1:8000/
