# Django Academic Portal

A REST API for academic records: organisations, courses, semesters, subjects, technical skills, students, assignments and assignment submissions. Built with Django and Django REST Framework. It is backend only, and you can explore it in the browser through DRF's built-in API pages.

## Data model

Every table uses a UUID primary key.

**Master data**

| Model | Fields |
| --- | --- |
| `Org` | `name` |
| `Course` | `course_name` (unique), `course_code` (unique), `org` → Org |
| `Semesters` | `semester_name` (unique), `sem_code` (unique) |
| `Subjects` | `subject_name` (unique), `subject_code` (unique) |
| `TechSkills` | `skill_name` (unique), `skill_code` (unique) |

**Records**

| Model | Fields |
| --- | --- |
| `StudentTable` | `student_usn_no` (unique), `email` (unique), `gender`, `course` → Course |
| `Assignments` | name, description, `start_date`, `submission_end_date`, `total_marks`, `assignment_code` (unique), and links to course, semester, subject and tech skill |
| `AssignmentTransactionTable` | `obtained_marks`, `remarks`, `candidate_submit_date` (set automatically), `student` → StudentTable, `assignment` → Assignments |

Deleting a course removes its students and assignments. Deleting a semester, subject or skill keeps the assignment and clears the link.

## API

Each resource is a DRF `ModelViewSet`, so all of them support list, create, retrieve, update and delete.

| Resource | Collection | Single item |
| --- | --- | --- |
| Organisations | `/api/orgs/` | `/api/orgs/{id}/` |
| Courses | `/api/courses/` | `/api/courses/{id}/` |
| Semesters | `/api/semesters/` | `/api/semesters/{id}/` |
| Subjects | `/api/subjects/` | `/api/subjects/{id}/` |
| Tech skills | `/api/techskills/` | `/api/techskills/{id}/` |
| Students | `/api/students/` | `/api/students/{id}/` |
| Assignments | `/api/assignments/` | `/api/assignments/{id}/` |
| Submissions | `/api/transactions/` | `/api/transactions/{id}/` |

Example: create a course under an organisation.

```http
POST /api/courses/
Content-Type: application/json

{
  "course_name": "Computer Science",
  "course_code": "CS",
  "org": "<org uuid>"
}
```

## Run it

Python 3.10 or newer.

```bash
git clone https://github.com/SanayKrishna/django-academic-portal.git
cd django-academic-portal
python -m venv env
source env/bin/activate         # Windows PowerShell: .\env\Scripts\Activate.ps1
pip install django djangorestframework
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/api/ to browse the endpoints. SQLite is the default database. To use PostgreSQL, change `DATABASES` in `AcademicPortal/settings.py` and install `psycopg`.

## Project layout

```text
AcademicPortal/   settings and root URLs
api/              models, serializers, viewsets and router
manage.py
```

## Next steps

- Authentication and roles (admin, faculty, student)
- File uploads for submissions
- Pagination and filtering on the list endpoints
