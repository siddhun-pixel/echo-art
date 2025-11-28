# Echo Art 🎨🔊

Echo Art is a Flask-based web app that processes audio and abstract inputs. It uses Gunicorn for deployment and is configured for Render.

## Features
- REST API for audio and abstract processing
- HTML frontend with form submission
- SQLite database for storing submissions
- Ready-to-deploy with Render

## Setup

```bash
pip install -r requirements.txt
flask db init
flask db migrate
flask db upgrade
python app.py
