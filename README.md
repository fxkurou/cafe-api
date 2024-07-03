# Cafe API

## Overview

This is a RESTful API for managing restaurant menus, allowing employees to vote for their preferred menu items. The API supports multiple versions to ensure compatibility with older mobile app versions.

## Features

- **User Authentication**: JWT-based authentication.
- **Restaurant Management**: Create and manage restaurants.
- **Menu Management**: Upload daily menus for restaurants.
- **Menu Item Management**: Manage menu items for each menu.
- **Voting System**: Employees can vote for their preferred menu items.
- **API Versioning**: Supports multiple API versions via URL namespaces.

## Technology Stack

- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: JWT
- **Containerization**: Docker, Docker Compose
- **Testing**: PyTest

## Setup Instructions

### Prerequisites

- Docker
- Docker Compose
- Python 3.8+
- PostgreSQL

### Environment Variables

Create a `.env` file in the project root with the following environment variables:

```env
POSTGRES_DB=restaurant_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DJANGO_SECRET_KEY=your_secret_key_here
```

## Running with docker

### 1. Clone the repository:
```
git clone https://github.com/yourusername/restaurant_voting_api.git
cd restaurant_voting_api
```
### 2. Build and start the Docker containers
```
docker-compose up --build
```
### 3. Apply database migrations:
```
docker-compose exec web python manage.py migrate
```
4. Create a superuser (optional):
```
docker-compose exec web python manage.py createsuperuser
```

## Running without docker

### 1. Clone the repository:
```
git clone https://github.com/yourusername/restaurant_voting_api.git
cd restaurant_voting_api
```
### 2. Create and activate a virtual environment:
```
python -m venv env
env/bin/activate
```
### 3. Install the dependencies:
```
pip install -r requirements.txt
```
### 4. Set up the PostgreSQL database and user as specified in the .env file. Update DATABASES settings in restaurant_api/settings.py if necessary.

### 5. Apply database migrations:
```
python manage.py migrate
```
### 6. Create a superuser (optional):
```
python manage.py createsuperuser
```
### 7. Run the development server:
```
python manage.py runserver
```

## Running tests

### With docker
```
docker-compose run test pytest
```

### Without docker
```
pytest
```
