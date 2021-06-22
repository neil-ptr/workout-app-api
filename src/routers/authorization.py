from fastapi import APIRouter

router = APIRouter()


@router.post('/auth')
async def auth():
    pass
