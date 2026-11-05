import hashlib
import secrets
from datetime import datetime, timedelta, timezone
from uuid import UUID
import jwt
from pwdlib import PasswordHash
from app.config import get_settings
password_hash = PasswordHash.recommended()
settings = get_settings()
def hash_password(password: str) -> str:
    return password_hash.hash(password)
def verify_password(password: str, hashed: str) -> bool:
    return password_hash.verify(password, hashed)
def issue_access_token(user_id: UUID) -> str:
    now = datetime.now(timezone.utc)
    payload = {"sub": str(user_id), "iss": settings.jwt_issuer, "iat": now, "exp": now + timedelta(minutes=settings.access_token_minutes)}
    return jwt.encode(payload, settings.jwt_secret.get_secret_value(), algorithm="HS256")
def new_refresh_token() -> str:
    return secrets.token_urlsafe(48)
def hash_refresh_token(token: str) -> str:
    return hashlib.sha256(token.encode()).hexdigest()
