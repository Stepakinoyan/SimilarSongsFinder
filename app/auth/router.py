from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from app.auth.client import oauth

router = APIRouter(prefix="/auth")


@router.get("/login")
async def login():
    return oauth.get_authorize_url()


@router.get("/authorize")
async def authorize(request: Request):
    code = request.query_params["code"]
    token = oauth.get_access_token(code=code)
    response = RedirectResponse(url="/docs")
    response.set_cookie('token', token.get("access_token"))
    return response
