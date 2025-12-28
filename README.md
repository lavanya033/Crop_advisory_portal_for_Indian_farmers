# Crop Advisory Portal for Indian Farmers 🌾

A Django-based web application that helps farmers make better crop decisions


## 🚀 Features
- Crop recommendation based on soil, season, and location
- Weather forecast using OpenWeather API
- AI-powered advisory using Groq API


## 🛠 Tech Stack
- Backend: Django (Python)
- Frontend: HTML, CSS, JavaScript
- Database: SQLite3
- APIs: Groq API, OpenWeather API

## ⚙️ Setup (Local)
```bash
git clone https://github.com/lavanya033/Crop_advisory_portal_for_Indian_farmers.git
cd Crop_advisory_portal_for_Indian_farmers
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
## .env file example
SECRET_KEY=your_secret_key
GROQ_API_KEY=your_groq_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
DEBUG=True
