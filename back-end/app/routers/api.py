from fastapi import APIRouter, Depends, HTTPException

from routers import casdoor

route = APIRouter(prefix="/api/v1")

route.include_router(casdoor.route)
