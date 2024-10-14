from fastapi import APIRouter

router = APIRouter(
    prefix="/fast",
    tags=["fast"],
    responses={404: {"description": "Not found ;)"}},
)

@router.get("/")
async def root():
    return {"message": "Hello PIV-Estudo-Python - Applications!"}