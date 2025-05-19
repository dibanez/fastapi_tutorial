from fastapi import FastAPI
from app.api import router as api_router
from app.config import settings
from app.db import Base, engine
from app.models.item import Item
from app.models.user import User

app = FastAPI(title=settings.PROJECT_NAME)

# Crear las tablas
Base.metadata.create_all(bind=engine)

app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}
