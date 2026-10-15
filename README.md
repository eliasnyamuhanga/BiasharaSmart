# BiasharaSmart — Business Management App

BiasharaSmart is a business management application built with React and Vite, with a Python FastAPI backend starter.

## Frontend Setup (Windows)

1. Extract the project ZIP.
2. Open the `BiasharaSmart` folder in VS Code.
3. Open Terminal → New Terminal.
4. Run `npm install`.
5. Run `npm run dev`.
6. Open the local URL printed by Vite.

## Features

- Search and filter records on Sales, Inventory, Expenses, Debts, and Reports.
- English and Kiswahili language switch, with the selection saved locally.
- Reports explaining sales, expenses, estimated profit, inventory units, and outstanding debts.
- CSV export for reports.
- Local display profile that saves a name and email.
- Separate Python FastAPI backend starter with registration, password-hashed login, JWT bearer tokens, and a protected profile endpoint.

## Backend Setup

1. Open a terminal in the `backend` folder.
2. Create and activate a Python virtual environment.
3. Install dependencies from `requirements.txt`.
4. Follow `backend/README.md` to configure the environment and start the API.

## Current Limitations

- Business records are still stored in the browser and are not yet connected to the FastAPI backend.
- The profile editor is a local display profile, not a real authenticated account.
- Google sign-in is not configured and requires Google OAuth credentials and server-side setup.
- The backend uses a local SQLite database by default.

## Before Production

- Connect the React frontend to the backend API.
- Add user-owned business records and enforce access controls.
- Configure database migrations, email verification, password recovery, rate limiting, backups, and security tests.
- Keep secret credentials out of GitHub.

## Technologies

- React
- Vite
- Python
- FastAPI
- SQLite
