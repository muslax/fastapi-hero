import logging
from motor.motor_asyncio import AsyncIOMotorClient

from core.config import (
    MONGODB_URI,
    MONGODB_NAME,
    MONGODB_MAX_POOL_SIZE,
    MONGODB_MIN_POOL_SIZE
)

class MongoDB:
    client: AsyncIOMotorClient = None

db = MongoDB()

def connect():
    logging.info("Connecting to MongoDB Atlas...")
    db.client = AsyncIOMotorClient(
        MONGODB_URI,
        maxPoolSize=MONGODB_MAX_POOL_SIZE,
        minPoolSize=MONGODB_MIN_POOL_SIZE
    )
    logging.info("Connected to MongoDB Atlas")

def close():
    logging.info("Closing MongoDB Atlas connection")
    db.client.close()
    logging.info("Connection closed")

def get_connection():
    return db.client

def get_collection(name: str):
    conn = get_connection()
    return conn[MONGODB_NAME][name]
