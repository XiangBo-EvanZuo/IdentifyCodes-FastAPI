from fastapi import APIRouter

router = APIRouter()


@router.post('/confirm')
async def confirm_code(
        id,
        answer
):
    pass
