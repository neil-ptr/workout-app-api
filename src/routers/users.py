from fastapi import APIRouter
from src.models.request.users import Login, SignUp

router = APIRouter()


@router.post('/users/login')
async def login_user(user: Login):
    return 'login'


@router.post('/users/signup')
async def signup_user(user: SignUp):
    print(user)
    return 'signup'
