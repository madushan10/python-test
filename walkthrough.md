# Project Setup Walkthrough

I have successfully scaffolded your enterprise FastAPI project in `d:\GIT\python-test`.

## What was built
The project uses the following robust, modern Python stack:
- **FastAPI** as the API web framework.
- **SQLAlchemy 2.x** and **Pydantic V2** for declarative models, ORM access, and data validation schemas.
- **PostgreSQL** configured as the primary relational database.
- **Alembic** set up for database migrations.
- **Redis & Celery** skeleton included for background job processing.
- **Pytest** configured for automated testing.
- **Docker Compose** added for quick local infrastructure spin-up.

## Key Modules
1. **User Management and Authentication Module:**
   - Designed around OAuth2 compatible flows (`OAuth2PasswordBearer`).
   - Uses `bcrypt` for secure password hashing.
   - Issues **JWT Access and Refresh Tokens**.
   - Contains a complete `User` domain model with corresponding CRUD operations for registration, querying, and updating user profiles.

2. **Core Settings & Security:**
   - Centralized `Settings` powered by `pydantic-settings` to securely manage `.env` configs.
   - Cleanly separated authentication endpoints (`/api/v1/auth`) and user management endpoints (`/api/v1/users`).

## Next Steps
> [!TIP]
> To get started locally, follow these steps:

1. **Install Dependencies:**
   ```bash
   cd d:\GIT\python-test
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Start Infrastructure (PostgreSQL & Redis):**
   ```bash
   docker-compose up -d
   ```

3. **Run Migrations (Alembic):**
   ```bash
   alembic revision --autogenerate -m "Initial migration"
   alembic upgrade head
   ```

4. **Start the FastAPI Server:**
   ```bash
   uvicorn app.main:app --reload
   ```
   You can then access the interactive Swagger UI at `http://localhost:8000/api/v1/openapi.json` or `http://localhost:8000/docs`.
