from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/1")
def hello1():
    return {"message": "Hello Thing 1!"}


@router.get("/2")
def hello2():
    return {"message": "Hello Thing 2!"}


@router.get("/3")
def hello3():
    return {"message": "Hello Thing 3!"}
