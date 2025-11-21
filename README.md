# django-academic-portal
A structured Django REST Framework backend for managing academic data such as organizations, courses, semesters, subjects, technical skills, students, assignments, and assignment submissions.

---

## Table of Contents
- Overview  
- Features  
- Technology Stack  
- Database Schema  
- Installation  
- Configuration  
- API Documentation  
- Usage Examples  
- Project Structure  
- Development  
- Troubleshooting  
- Future Enhancements  
- Contributors  

---

# Overview
This project is a backend API built using Django and Django REST Framework for an Academic Portal.  
It provides endpoints to manage:

- Organizations  
- Courses  
- Semesters  
- Subjects  
- Technical Skills  
- Students  
- Assignments  
- Assignment submissions  

The system is modular, clean, and designed for easy extension such as authentication, role-based access, or frontend integration.

---

# Features

### Core Features
- Organization management  
- Course and semester structure  
- Subject and technical skill definitions  
- Student registration with course linking  
- Assignment creation and distribution  
- Submission tracking with marks + remarks  
- UUID-based primary keys for data integrity  
- RESTful API endpoints  

### Technical Features
- Django REST Framework serializers  
- Unique fields for consistency  
- Nested read-only serializer for submission display  
- SQLite support out of the box  
- Clean, extensible codebase  

---

# Technology Stack

### Backend Framework
- Django 5.2.7  
- Django REST Framework  

### Database
- SQLite (default for development)  
- Easily swappable to PostgreSQL  

### Other
- Python 3.x  

---

# Database Schema

## Master Tables

### Org
- id (UUID)  
- name  

### Course
- id (UUID)  
- course_name  
- course_code  
- org (FK → Org)  

### Semesters
- id (UUID)  
- semester_name  
- sem_code  

### Subjects
- id (UUID)  
- subject_name  
- subject_code  

### TechSkills
- id (UUID)  
- skill_name  
- skill_code  

---

## Transactional Tables

### StudentTable
- id  
- student_usn_no  
- email  
- gender  
- course (FK → Course)  

### Assignments
- id  
- assignment_name  
- assignment_description  
- start_date  
- submission_end_date  
- total_marks  
- assignment_code (unique)  
- tech_skill (FK)  
- subject (FK)  
- semester (FK)  
- course (FK)  

### AssignmentTransactionTable
- id  
- obtained_marks  
- candidate_submit_date  
- remarks  
- student (FK → StudentTable)  
- assignment (FK → Assignments)  

---

# Installation

## 1. Clone Repository
```
git clone https://github.com/SanayKrishna/django-academic-portal.git
cd django-academic-portal
```

## 2. Create Virtual Environment
```
python -m venv env
```

## 3. Activate Virtual Environment
**PowerShell:**
```
.\env\Scripts\Activate.ps1
```

## 4. Install Dependencies
```
pip install -r requirements.txt
```

## 5. Apply Migrations
```
python manage.py makemigrations
python manage.py migrate
```

## 6. Run Development Server
```
python manage.py runserver
```

---

# Configuration

### SQLite (default)
Already configured in settings.

### PostgreSQL (optional)
Update `DATABASES` in `settings.py`:

```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "dbname",
        "USER": "username",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
```

---

# API Documentation

### Base URL
```
http://127.0.0.1:8000/api/
```

---

# Master Data Endpoints

### Organizations
- `GET /api/orgs/`  
- `POST /api/orgs/`

### Courses
- `GET /api/courses/`  
- `POST /api/courses/`

### Semesters
- `GET /api/semesters/`  
- `POST /api/semesters/`

### Subjects
- `GET /api/subjects/`  
- `POST /api/subjects/`

### Tech Skills
- `GET /api/tech-skills/`  
- `POST /api/tech-skills/`

---

# Students
- `GET /api/students/`  
- `POST /api/students/`

---

# Assignments
- `GET /api/assignments/`  
- `POST /api/assignments/`

---

# Assignment Transactions
- `GET /api/assignment-transactions/`  
- `POST /api/assignment-transactions/`

---

# Usage Examples

### Create Organization
```
POST /api/orgs/
{
    "name": "ABC University"
}
```

### Create Course
```
POST /api/courses/
{
    "course_name": "Computer Science",
    "course_code": "CS",
    "org": "<org_uuid>"
}
```

### Register Student
```
POST /api/students/
{
    "student_usn_no": "1MS21CS001",
    "email": "student@example.com",
    "gender": "Male",
    "course": "<course_uuid>"
}
```

### Create Assignment
```
POST /api/assignments/
{
    "assignment_name": "REST API Task",
    "assignment_description": "Build a Django REST API",
    "start_date": "2025-01-10T10:00:00Z",
    "submission_end_date": "2025-01-20T23:59:59Z",
    "total_marks": 100,
    "assignment_code": "API01",
    "course": "<course_uuid>",
    "semester": "<semester_uuid>",
    "subject": "<subject_uuid>",
    "tech_skill": "<tech_uuid>"
}
```

---

# Project Structure

```
django-academic-portal/
├── AcademicPortal/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── api/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── migrations/
├── db.sqlite3
├── manage.py
└── README.md
```

---

# Development

### Run Server
```
python manage.py runserver
```

### Create Migrations
```
python manage.py makemigrations
python manage.py migrate
```

---

# Troubleshooting

### ModuleNotFoundError: rest_framework
```
pip install djangorestframework
```

### Migration Issues
```
python manage.py makemigrations
python manage.py migrate
```

### Virtual Environment Activation Error
```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

# Future Enhancements
- JWT authentication  
- User roles (Admin, Faculty, Student)  
- File uploads for submission  
- Pagination + filtering  
- PostgreSQL migration  
- Frontend (React/Next.js)  
- CI/CD pipeline  
- Analytics dashboard  

---

# Contributors
**Sanay Krishna**  
Developer – Academic Portal Backend
