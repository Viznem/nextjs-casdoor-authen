from typing import Annotated
from fastapi import APIRouter, Body, Depends, HTTPException, Response, status
from starlette.requests import Request
from starlette.responses import JSONResponse

from config.configcasdoor import get_casdoor_sdk
from utils import get_user_from_session

from models.casdoor_user import CasdoorUser

route = APIRouter(prefix="/casdoor")


@route.post("/signin")
async def casdoor_callback(
    code: Annotated[str, Body(embed=True)],
    request: Request,
    response: Response,
    sdk=Depends(get_casdoor_sdk),
):
    try:
        token = sdk.get_oauth_token(code=code)
        access_token = token.get("access_token")
        user = sdk.parse_jwt_token(access_token)

        # sdk.verify_jwt_token(access_token)

        request.session["casdoor_user"] = user

        return {
            "message": "Successfully logged in!",
            "access_token": access_token,
            "decoded_msg": user,
        }

    except Exception as e:
        response.status_code = status.HTTP_401_UNAUTHORIZED
        return {"error": str(e)}


@route.post("/signout", response_class=JSONResponse)
async def post_signout(request: Request):
    del request.session["casdoor_user"]
    return {"status": "ok"}


@route.get("/get-account", response_class=JSONResponse)
async def get_user(user_name: str, sdk=Depends(get_casdoor_sdk)):
    try:
        user_info = sdk.get_user(user_name)
        return user_info
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))


@route.post("/create-casdoor-user")
async def create_casdoor_user(casdoor_user: CasdoorUser, sdk=Depends(get_casdoor_sdk)):
    try:
        print(type(casdoor_user))
        res = sdk.add_user(casdoor_user)
        return res
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
