from fastapi import APIRouter

from api.movie import router as movie_router
from api.thing import router as thing_router

router = APIRouter()

router.include_router(movie_router, prefix="/movie", tags=["Movies"])
router.include_router(thing_router, prefix="/thing", tags=["Things"])