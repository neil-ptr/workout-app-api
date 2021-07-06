from fastapi import APIRouter

from src.models.request import sets

router = APIRouter()


@router.get('/')
async def get_sets():
    return 'get sets'


@router.post('/')
async def post_sets():
    return 'post sets'


@router.put('/')
async def update_set():
    return 'get set'

@router.delete('/')
async def delete_set():
    return 'delete set'