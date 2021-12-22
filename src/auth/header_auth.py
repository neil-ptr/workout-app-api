from typing import Optional

from jose.exceptions import JWTError
from fastapi import Header, HTTPException, status
from src.config.config import ACCESS_ALGORITHM, ACCESS_TOKEN_SECRET

from src.utils.jwt import decode_token

async def header_auth(x_access_token: Optional[str] = Header(None)):
    payload = decode_token(x_access_token, ACCESS_TOKEN_SECRET, ACCESS_ALGORITHM)
    return payload

