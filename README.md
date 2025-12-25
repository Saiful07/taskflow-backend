# TaskFlow Backend – Advanced Task Management API

TaskFlow is a backend-first task management system built using Django REST Framework.  
It demonstrates real-world backend engineering concepts such as multi-tenant architecture, JWT authentication, nested resources, and permission-based access control.

This project focuses on clean backend design, security, and real debugging rather than tutorial-level CRUD.

---

## Project Purpose

Most beginner projects stop at basic CRUD operations.  
TaskFlow goes further by implementing:

- Multi-tenant workspaces
- Projects scoped to workspaces
- Tasks scoped to projects
- JWT-based authentication
- Secure permission checks at every level
- Full task lifecycle management

This makes it a strong backend portfolio project suitable for internships and junior backend roles.

---

## Architecture Overview

User  
└── Workspace  
  └── Project  
    └── Task  

- A user can belong to multiple workspaces  
- A workspace contains multiple projects  
- A project contains multiple tasks  
- All data access is strictly scoped to prevent data leaks  

---

## Authentication

- JWT authentication using djangorestframework-simplejwt  
- Email-based login  
- Access token required for all protected endpoints  
- Token expiration handled correctly  

---

## Core Features

### Workspaces
- Create and list workspaces
- Workspace owner and members
- Automatic membership assignment on creation

### Projects
- Projects belong to a workspace
- Only workspace members can access projects
- Nested API design

### Tasks
- Tasks belong to projects
- Full lifecycle support:
  - Create
  - List
  - Retrieve
  - Update
  - Delete
- Task statuses:
  - TODO
  - IN_PROGRESS
  - DONE
- Priority levels:
  - LOW
  - MEDIUM
  - HIGH

---

## Permissions and Security

- JWT enforced on all APIs
- Workspace-scoped permissions
- Project and task isolation
- Object-level filtering to prevent unauthorized access

Security is intentional and explicitly implemented.

---

## API Endpoints Summary

### Authentication
POST   /api/auth/login/  
POST   /api/auth/refresh/  

### Workspaces
POST   /api/workspaces/create/  
GET    /api/workspaces/  
GET    /api/workspaces/<id>/  

### Projects
POST   /api/workspaces/<workspace_id>/projects/create/  
GET    /api/workspaces/<workspace_id>/projects/  

### Tasks
POST   /api/projects/<project_id>/tasks/create/  
GET    /api/projects/<project_id>/tasks/  
GET    /api/projects/<project_id>/tasks/<task_id>/  
PATCH  /api/projects/<project_id>/tasks/<task_id>/  
DELETE /api/projects/<project_id>/tasks/<task_id>/  

---

## Tech Stack

- Python
- Django
- Django REST Framework
- JWT (SimpleJWT)
- SQLite (development)
- Git and GitHub

---

## Running the Project Locally

1. Clone the repository:
   git clone https://github.com/<your-username>/taskflow-backend.git

2. Navigate to the project:
   cd taskflow-backend/config

3. Create and activate virtual environment:
   python -m venv .venv  
   .venv\Scripts\activate

4. Install dependencies:
   pip install -r requirements.txt

5. Run migrations:
   python manage.py migrate

6. Create superuser:
   python manage.py createsuperuser

7. Start server:
   python manage.py runserver

---

## What This Project Demonstrates

- Backend system design
- RESTful API best practices
- Authentication and authorization
- Debugging real backend issues
- Clean Django project structure
- Professional Git workflow

---

## Future Enhancements

- Task comments and activity logs
- Pagination and filtering
- Role-based task permissions
- Frontend integration
- Deployment using Docker and cloud services

---

## Author

Saiful Islam  
Backend Developer (Python / Django)

This project was built to demonstrate practical backend engineering skills, not just to complete a tutorial.

---

## Final Notes

This backend system was designed, implemented, debugged, and completed end-to-end with a strong focus on correctness, security, and scalability.
