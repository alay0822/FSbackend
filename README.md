<<<<<<< HEAD
# TDFullStack
=======
# FSbackend
>>>>>>> fd3ce9ac7dafa2eb039cc7fddd24da8a06b39151

Full-Stack To-Do App Instructions Summary
1. Set Up Your Environment
Install Python, Node.js, and set up a virtual environment.

Organize the project into separate folders for the React frontend and FastAPI backend.

2. FastAPI Backend
Initialize a FastAPI project.

Use SQLAlchemy and Pydantic to model a To-Do item (id, title, completed).

Implement full CRUD API endpoints:

Create, Read (all & one), Update, Delete

Add filtering by completion status.

3. React Frontend
Build a UI to:

Add, edit, delete, and view tasks

Include filters: All, Completed, Pending

Use fetch to connect to the FastAPI backend.

Add dark/light mode toggle.

4. Integration & Testing
Ensure all features work via the UI.

Test APIs with HTTPie or Swagger UI.

Debug any integration issues.


API Endpoints


GET https://fsbackend-t547.onrender.com/api/tasks/ to READ TASKS
GET https://fsbackend-t547.onrender.com/api/tasks/{task_id}/ to GET TASK
POST https://fsbackend-t547.onrender.com/api/tasks/ to CREATE TASKS
DELETE https://fsbackend-t547.onrender.com/api/tasks/ to DELETE ALL TASKS
DELETE https://fsbackend-t547.onrender.com/api/tasks/{task_id}/ to DELETE TASKS
PUT https://fsbackend-t547.onrender.com/api/tasks/{task_id}/ to UPDATE TASKS


