import base64

from typing import Optional

from fastapi.exceptions import HTTPException
from fastapi import Request
from starlette.status import HTTP_401_UNAUTHORIZED


class CookieAuthScheme:
    async def __call__(self, request: Request) -> Optional[str]:
        token_cookie_val: str = request.cookies.get("token")
        if not token_cookie_val:
            raise HTTPException(
                status_code=HTTP_401_UNAUTHORIZED,
                detail="Not authenticated",
            )
        scheme, _, param = token_cookie_val.partition("%20")
        if scheme.lower() != "bearer":
            raise HTTPException(
                status_code=HTTP_401_UNAUTHORIZED,
                detail="Not authenticated",
            )
        return param
