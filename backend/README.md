# BiasharaSmart FastAPI backend starter

This is a **starter backend**, not yet connected to the React frontend. It provides a health endpoint, account registration, password hashing, email/password login, signed bearer tokens, and a protected current-user endpoint.

## Run on Windows

1. Open a new terminal in the `backend` folder.
2. Create a virtual environment: `python -m venv .venv`
3. Activate it: `.venv\\Scripts\\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env`, then replace `JWT_SECRET` with a long random value. Never commit `.env`.
6. In this terminal, load the environment variables. PowerShell example: `$env:JWT_SECRET="your-long-random-secret"` and `$env:CORS_ORIGINS="http://localhost:5173"`. (The backend loads the `.env` file automatically.)
7. Start the API: `uvicorn main:app --reload`
8. Open `http://127.0.0.1:8000/docs` for interactive API testing and `http://127.0.0.1:8000/health` for health status.

## Current endpoints

- `GET /health`
- `POST /auth/register` with `name`, `email`, `password` (minimum 10 characters)
- `POST /auth/login` with `email`, `password`
- `GET /auth/me` with bearer token
- `GET /api/summary` with bearer token

Local default database is SQLite. Set `DATABASE_URL` for PostgreSQL in deployment. Before production, add rate limiting, email verification/password reset, HTTPS, migrations, audit logging, backups, and tests. The local fallback JWT secret is only for development and must not be used publicly.

## Google sign-in

Google OAuth is **not configured**. Create OAuth credentials in Google Cloud Console, register exact development and production redirect URIs, keep the client secret only on the backend, validate Google's ID token server-side, and link accounts by verified email/provider subject. Never put a Google client secret in React environment variables.
