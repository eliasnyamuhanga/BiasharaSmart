# BiasharaSmart — improved starter

## Frontend setup (Windows)
1. Extract the ZIP.
2. Open the `BiasharaSmart` folder in VS Code.
3. Open Terminal → New Terminal.
4. Run `npm install`.
5. Run `npm run dev`.
6. Open the local URL printed by Vite.

## Improvements in this update
- Search now filters records on Sales, Inventory, Expenses, Debts, and Reports.
- English/Kiswahili switch is available in the top bar and its choice is saved locally.
- Reports explain sales, expenses, estimated profit, inventory units, and outstanding debts; CSV export remains available.
- Local display profile can save a name and email and displays the name in the top bar.
- Added a separate `backend/` FastAPI starter with registration, password-hashed login, JWT bearer tokens, and protected profile endpoint.

## Important current limitations
- The React app still stores business records in this browser and is **not connected to the FastAPI backend** yet.
- The profile editor is a local display profile, not a real authenticated account.
- Google OAuth is **not activated**. It requires Google Cloud OAuth credentials and server-side configuration; never put client secrets in the frontend.
- Backend account data is stored in a local SQLite database by default. Follow `backend/README.md` before testing.
- Before production, add user-owned business tables, connect the frontend API, migrations, email verification/password reset, rate limiting, backups, and security tests.
