# Learnoverse Internship Project

## Goal
Build a tiny React Native app that plays YouTube videos whose metadata lives in MongoDB.

---

# Project Overview

1. **Backend** (Django + MongoDB + YouTube API)


# Backend: Django API

## Tech Stack
- Python 3.11+
- Django 5.2
- PyMongo
- YouTube Data API v3
- django-cors-headers

## Folder Structure

backend/
├── backend/ # Django project
│ ├── settings.py
│ ├── urls.py
│ └── ...
├── api/ # Gateway app
├── video_service/ # Video fetching app
├── metadata_service/ # Metadata enrichment app
├── manage.py
├── requirements.txt
└── README.md

## Setup Instructions

1. Clone the backend repo:

git clone https://github.com/BhanuPrakash2407/learnoverse_backend.git
cd learnoverse_backend

# Create virtual environment:
  python -m venv venv
# Activate venv
Windows : venv\Scripts\activate

macOS/Linux: venv/bin/activate

# Install dependencies:

pip install -r requirements.txt

Create .env file in project root:

MONGO_URI=mongodb://localhost:27017/learnoverse
YT_API_KEY=YOUR_YOUTUBE_API_KEY

# Run the Backend

python manage.py runserver 0.0.0.0:8000

