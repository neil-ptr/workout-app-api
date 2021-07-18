from typing import Optional

from fastapi.exceptions import HTTPException
from fastapi import Request
from starlette.status import HTTP_401_UNAUTHORIZED

class CookieAuthScheme:
    def __init__(self):
        pass

    async def __call__(self, request: Request) -> Optional[str]:
        print('jdfkldsjflksdjklfdsfsd')
        token_cookie_val: str = request.cookies.get("token")
        scheme, _, param = token_cookie_val.partition(" ")
        print(token_cookie_val, 'sjfhids')
        print(scheme, param)
        if not token_cookie_val or scheme.lower() != "bearer":
            raise HTTPException(
                status_code=HTTP_401_UNAUTHORIZED,
                detail="Not authenticated",
            )
        return param
