from uuid import uuid4
from app.security import hash_password, verify_password, issue_access_token

def test_argon2_password_roundtrip() -> None:
    encoded = hash_password("correct horse battery staple")
    assert encoded != "correct horse battery staple"
    assert verify_password("correct horse battery staple", encoded)
    assert not verify_password("wrong password", encoded)

def test_access_token_is_issued() -> None:
    assert isinstance(issue_access_token(uuid4()), str)
