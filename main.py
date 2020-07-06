from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.router import router
from core import config
from db.mongo import connect, close, get_connection

app = FastAPI(title=config.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_event_handler("startup", connect)
app.add_event_handler("shutdown", close)

# Default route
@app.get("/")
def home():
    return {"message": config.PROJECT_NAME}

app.include_router(router, prefix="/v1")
