docker run --name postgres-db -e POSTGRES_USER=user -e POSTGRES_PASSWORD=password -p 5432:5432 -d postgres

# Project Python Files Overview (July 9, 2025)

## main.py
- FastAPI app entry point.
- Sets up app with lifespan event to initialize DB.
- Includes `/auth` router and a protected route using JWT authentication.

## app/util/protectRouter.py
- Provides `get_current_user` dependency for FastAPI.
- Extracts and validates JWT from Authorization header.
- Uses `UserService` to fetch user info from DB.

## app/util/init_db.py
- Defines `init_db()` to create all tables using SQLAlchemy Base metadata.

## app/service/userService.py
- `UserService` class for user signup, login, and fetching by ID.
- Handles password hashing, JWT creation, and user existence checks.

## app/routers/auth.py
- FastAPI router for `/login` and `/signup` endpoints.
- Uses `UserService` for authentication logic.

## app/db/schema/user.py
- Pydantic models for user input/output: `UserInCreate`, `UserOutput`, `UserInUpdate`, `UserInLogin`, `UserWithToken`.

## app/db/repository/userRepo.py
- `UserRepository` for DB operations: create user, check existence, get by email/ID.

## app/db/repository/base.py
- Base repository class holding SQLAlchemy session.

## app/db/models/user.py
- SQLAlchemy model for `User` table.
- Fields: id, username, password, full_name, address, email, is_active.

## app/core/security/hashHelper.py
- `HashHelper` class for password hashing and verification using bcrypt.

## app/core/security/authHandler.py
- `AuthHandler` class for JWT signing and decoding.
- Uses `decouple` for secret and algorithm config.

## app/core/database.py
- SQLAlchemy DB setup: engine, session, Base, and `get_db` dependency.
- Uses `decouple` for DB URL.

---

*This note was auto-generated to summarize all Python files in the workspace as of July 9, 2025.*