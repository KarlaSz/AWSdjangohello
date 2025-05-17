# Django Application on AWS Amazon🚀

## 📌 Project Overview
This project is a **Django-based web application** deployed on **Amazon Web Services (AWS)**. It utilizes essential AWS services such as **EC2** (compute), **RDS** (database), and **S3** (storage) to ensure scalability and reliability. The application serves a REST API and integrates with a **PostgreSQL database** for data management.

## 🌍 Live Deployment
The application is deployed on AWS EC2, with:
- **SQLite3 (db)** for data storage
- **AWS S3** for media and static files
- **Elastic Load Balancer** for efficient traffic distribution
- **Gunicorn + Nginx** for production-level WSGI server handling

## 🛠 Local Development Setup
### Prerequisites:
- Python 3.9+
- Django 4.0+
- SQLite3
- AWS CLI (configured with your AWS credentials)
- Virtual environment (recommended)

### Step 1: Clone the Repository
```bash
git clone https://github.com/KarlaSz/AWSdjangohello.git
cd django-hello
