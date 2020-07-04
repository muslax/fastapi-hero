import logging
from typing import Any, List
from bson.objectid import ObjectId
from fastapi import APIRouter, HTTPException
from starlette.responses import JSONResponse

from db.mongo import get_connection, get_collection
from core.config import MONGODB_NAME
from models.movie import Movie

router = APIRouter()

@router.get("", response_model=List[Movie])
async def read_many(limit: int=50, skip: int=0):
    collection = get_collection("movies")
    rs: List[Movie] = []
    cursor = collection.find({}, limit=limit, skip=skip)
    async for row in cursor:
        rs.append( Movie(**row) )
    return rs


@router.get("/{movie_id}", response_model=Movie)
async def read_one(movie_id: str):
    collection = get_collection("movies")
    if ObjectId.is_valid(movie_id):
        found = await collection.find_one({"_id": ObjectId(movie_id)})
        if found:
            return found
    # raise HTTPException(status_code=404, detail="Not found.")  # It's OK
    return JSONResponse( {"error": "NOT FOUND"}, status_code=404 )


@router.get("/search/{term}", response_model=List[Movie])
async def search(term: str, field: str="", limit: int=50, skip: int=0):
    collection = get_collection("movies")
    if field == "title":
        filter = {"title": {"$regex": term}}
    else:
        filter = { "$text": { "$search": term } }
    rs: List[Movie] = []
    cursor = collection.find(filter, limit=limit, skip=skip)
    async for row in cursor:
        rs.append( Movie(**row) )
    return rs

