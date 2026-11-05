from datetime import datetime, timedelta, timezone
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, EmailStr, Field
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.config import get_settings
from app.database import get_db
from app.models import RefreshToken, User
from app.security import hash_password, verify_password, issue_access_token, new_refresh_token, hash_refresh_token
router = APIRouter(prefix="/auth", tags=["authentication"])
settings = get_settings()
class Credentials(BaseModel):
    email: EmailStr
    password: str = Field(min_length=12, max_length=128)
    display_name: str = Field(default="", max_length=80)
class LoginCredentials(BaseModel):
    email: EmailStr
    password: str
class Tokens(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
async def issue_tokens(user: User, db: AsyncSession) -> Tokens:
    raw = new_refresh_token()
    db.add(RefreshToken(user_id=user.id, token_hash=hash_refresh_token(raw), expires_at=datetime.now(timezone.utc) + timedelta(days=settings.refresh_token_days)))
    await db.commit()
    return Tokens(access_token=issue_access_token(user.id), refresh_token=raw)
@router.post("/register", response_model=Tokens, status_code=201)
async def register(payload: Credentials, db: AsyncSession = Depends(get_db)) -> Tokens:
    email = str(payload.email).lower()
    if await db.scalar(select(User).where(User.email == email)):
        raise HTTPException(status_code=409, detail="Account already exists")
    user = User(email=email, password_hash=hash_password(payload.password), display_name=payload.display_name)
    db.add(user)
    await db.flush()
    return await issue_tokens(user, db)
@router.post("/login", response_model=Tokens)
async def login(payload: LoginCredentials, db: AsyncSession = Depends(get_db)) -> Tokens:
    user = await db.scalar(select(User).where(User.email == str(payload.email).lower()))
    if not user or not user.is_active or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return await issue_tokens(user, db)
