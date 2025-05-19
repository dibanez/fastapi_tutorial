from fastapi import APIRouter
from app.api.routes import router as item_router
from app.api.auth import router as auth_router

router = APIRouter()
router.include_router(auth_router)
router.include_router(item_router)