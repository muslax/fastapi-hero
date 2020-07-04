from datetime import datetime
from typing import Any, List, Optional
from pydantic import BaseModel, Schema, validator

class IMDB(BaseModel):
    rating: Optional[Any]
    votes: Optional[Any]

class Movie(BaseModel):
    id: Optional[Any] = Schema(..., alias="_id")
    title: str
    plot: str = None
    fullplot: str = None
    pposter: str = None
    rated: str = None
    released: datetime = None
    genres: List[str] = []
    cast: List[str] = []
    writers: List[str] = []
    directors: List[str] = []
    imdb: IMDB
    # type: str

    @validator("id", check_fields=False)
    @classmethod
    def validate_id(cls, x):
        return str(x)
