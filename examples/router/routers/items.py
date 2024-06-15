from fastapi import APIRouter

router = APIRouter()

@router.get("/items/", tags=["items"])
async def read_items():
    return [{"itemname": "Box"}, {"itemname": "Tree"}]


@router.get("/items/me", tags=["items"])
async def read_user_me():
    return {"itemname": "me...item"}


@router.get("/items/{itemname}", tags=["items"])
async def read_user(itemname: str):
    return {"itemname": itemname}
