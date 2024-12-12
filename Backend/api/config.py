from fastapi import APIRouter, Depends
from routes import user, product

router = APIRouter()

router.include_router(user.router)
router.include_router(product.router)