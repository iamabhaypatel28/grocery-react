from fastapi import APIRouter, Depends
from fastapi.security import APIKeyHeader

from routes import (
    user,
)

router = APIRouter()

router.include_router(user.router)