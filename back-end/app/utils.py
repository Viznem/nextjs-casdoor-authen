from starlette.requests import Request
from fastapi import HTTPException


async def get_user_from_session(request: Request):
    user = request.session.get("casdoor_user")
    if user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return user
