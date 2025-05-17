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

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/django-app.git
   cd django-app



### Step 2: Install Dependencies
    ```bash
    pip install -r requirements.txt

### Step 2: Install Dependencies
    ```bash
    pip install -r requirements.txt

### Step 3: Configure Environment Variables
Create a .env file in the root directory with your AWS and database credentials:

AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
DATABASE_URL=postgres://user:password@aws-db-url/dbname
DEBUG=True

### Step 4: Apply Database Migrations
    ```bash
    python manage.py migrate

### Step 5: Run Local Server
    ```bash
    python manage.py runserver
    Your application will now be accessible at http://127.0.0.1:8000/.


🚀 Deployment on AWS
### Step 1: Configure AWS CLI
Ensure AWS CLI is installed and authenticated:

    ```bash
    aws configure
    Provide your AWS Access Key, Secret Key, and preferred region.

### Step 2: Launch EC2 Instance
Start an EC2 instance for hosting Django:

    ```bash
    aws ec2 run-instances --image-id ami-12345678 --count 1 --instance-type t3.micro --key-name your-key-name --security-group-ids sg-123456

Once launched, SSH into the instance:

    ```bash
    ssh -i your-key.pem ec2-user@your-ec2-public-ip

### Step 3: Deploy Code on EC2
Install dependencies on the server:


    ```bash
    sudo apt update && sudo apt install python3-pip python3-venv
    Clone and set up the project:

    ```bash
    git clone https://github.com/your-repo/django-hello.git
    cd django-heloo

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

### Step 4: Configure PostgreSQL (AWS RDS)
Create an RDS instance via AWS Console or CLI.

Update your DATABASE_URL in .env with RDS endpoint.

### Step 5: Set Up AWS S3 for Media Storage
    ```bash
    aws s3 mb s3://your-app-bucket-name

Update Django settings to use django-storages for managing media files.

### Step 6: Configure Gunicorn + Nginx
Set up Gunicorn as an application server:

    ```bash
    gunicorn --bind 0.0.0.0:8000 your_pr
