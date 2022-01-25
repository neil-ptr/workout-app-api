from typing import Optional

from jose.exceptions import JWTError, ExpiredSignatureError
from fastapi import Header, HTTPException, status
from src.config.config import ACCESS_ALGORITHM, ACCESS_TOKEN_SECRET

from src.utils.jwt import decode_token

async def header_auth(x_access_token: Optional[str] = Header(None)):
    try:
        payload = decode_token(x_access_token, ACCESS_TOKEN_SECRET, ACCESS_ALGORITHM)
        return payload
    except (JWTError, ExpiredSignatureError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )


