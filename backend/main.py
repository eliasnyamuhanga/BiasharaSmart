"""BiasharaSmart API starter. Configure secrets before any public deployment."""
import os
from datetime import datetime, timedelta, timezone
from typing import Generator

import jwt
from pwdlib import PasswordHash
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import DateTime, Integer, String, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker


load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./biasharasmart.db")

JWT_SECRET = os.getenv("JWT_SECRET")
if not JWT_SECRET:
    # Local development only; set a long random JWT_SECRET in .env for real use.
    JWT_SECRET = "LOCAL-ONLY-CHANGE-ME-BIASHARASMART-SECRET"
JWT_ALGORITHM = "HS256"
TOKEN_MINUTES = 60 * 12
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
password_hash = PasswordHash.recommended()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(80))
    email: Mapped[str] = mapped_column(String(254), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(500))
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

Base.metadata.create_all(bind=engine)
app = FastAPI(title="BiasharaSmart API", version="0.1.0")
origins = [x.strip() for x in os.getenv("CORS_ORIGINS", "http://localhost:5173").split(",") if x.strip()]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

class RegisterInput(BaseModel):
    name: str = Field(min_length=2, max_length=80)
    email: EmailStr
    password: str = Field(min_length=10, max_length=128)

class LoginInput(BaseModel):
    email: EmailStr
    password: str

class UserOutput(BaseModel):
    id: int
    name: str
    email: EmailStr

class TokenOutput(BaseModel):
    access_token: str
    token_type: str = "bearer"

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def make_token(user: User) -> str:
    now = datetime.now(timezone.utc)
    return jwt.encode({"sub": str(user.id), "iat": now, "exp": now + timedelta(minutes=TOKEN_MINUTES)}, JWT_SECRET, algorithm=JWT_ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        user_id = int(payload["sub"])
    except (jwt.PyJWTError, KeyError, TypeError, ValueError):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired token", headers={"WWW-Authenticate": "Bearer"})
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user

@app.get("/health")
def health():
    return {"status": "ok", "service": "BiasharaSmart API"}

@app.post("/auth/register", response_model=UserOutput, status_code=201)
def register(payload: RegisterInput, db: Session = Depends(get_db)):
    email = payload.email.lower()
    if db.scalar(select(User).where(User.email == email)):
        raise HTTPException(status_code=409, detail="An account with this email already exists")
    user = User(name=payload.name.strip(), email=email, password_hash=password_hash.hash(payload.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@app.post("/auth/login", response_model=TokenOutput)
def login(payload: LoginInput, db: Session = Depends(get_db)):
    user = db.scalar(select(User).where(User.email == payload.email.lower()))
    if not user or not password_hash.verify(payload.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Incorrect email or password", headers={"WWW-Authenticate": "Bearer"})
    return {"access_token": make_token(user), "token_type": "bearer"}

@app.get("/auth/me", response_model=UserOutput)
def me(user: User = Depends(get_current_user)):
    return user

@app.get("/api/summary")
def summary(user: User = Depends(get_current_user)):
    # Deliberately not returning business records yet. Next step is to add
    # user_id-owned products/sales/expenses/debts tables and migrate local data.
    return {"user_id": user.id, "message": "Authenticated. Business-data endpoints are the next build step."}
