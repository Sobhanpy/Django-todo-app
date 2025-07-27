# ToDo App with Django and Django REST Framework

This is a full-featured ToDo list application built using Django and Django REST Framework (DRF). It includes user authentication (login, registration, token-based access), a RESTful API, and core CRUD functionality for managing tasks.

## Features

- User Registration and Login
- Token-based Authentication (via DRF)
- Create, Read, Update, and Delete for ToDo items
- RESTful API endpoints
- Docker support for easy containerized deployment

## Technologies Used

- Python 3
- Django
- Django REST Framework
- Docker & Docker Compose
- Postman or any REST client (for testing)

## Getting Started

You can run this project either locally with Python or using Docker containers.

---

### Option 1: Local Setup

#### Prerequisites

- Python 3.9+
- pip
- virtualenv (recommended)

#### Installation

1. **Clone the repository**

git clone https://github.com/Sobhanpy/django-todo-app.git
cd todo-app


2. **Create and activate a virtual environment**

python -m venv env
On Linux :source env/bin/activate 
On Windows: env\Scripts\activate


3. **Install dependencies**

pip install -r requirements.txt


4. **Run migrations**

python manage.py migrate


5. **Create a superuser (admin access)**

python manage.py createsuperuser


6. **Run the development server**

python manage.py runserver


App will be available at: `http://localhost:8000/`

---

### Option 2: Using Docker

#### Prerequisites

- Docker
- Docker Compose

#### Run the app with Docker

1. **Clone the repository**

git clone https://github.com/Sobhanpy/django-todo-app.git
cd django-todo-app


2. **Build and start the containers**

docker-compose up --build


This will:

- Build the Docker image
- Run migrations inside the container
- Start the Django development server

3. **Access the app**

The API will be accessible at: `http://localhost:8000/`

---

## API Usage

### Authentication

Use the `/api/token/` endpoint to obtain a JWT access and refresh token.

#### POST `/api/token/`

**Request body:**
```json
{
  "username": "your_username",
  "password": "your_password"
}

Response:

{
  "access": "your-access-token",
  "refresh": "your-refresh-token"
}

Include the access token in the Authorization header for all subsequent requests:

Authorization: Bearer your-access-token
```
