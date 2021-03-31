from fastapi import APIRouter, HTTPException
from praw import Reddit
from prawcore.exceptions import OAuthException
from starlette.requests import Request
from starlette.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED

from app.schemas.reddit import RedditInfo

router = APIRouter()


@router.get("/", response_model=RedditInfo, status_code=HTTP_200_OK)
async def get_connection_info(request: Request):
    """Check whether you are connected with Reddit API."""

    reddit: Reddit = request.app.state.reddit

    try:
        user = reddit.user.me()
    except OAuthException as err:
        raise HTTPException(
            HTTP_401_UNAUTHORIZED, "Reddit Authentication Failed"
        ) from err

    return {"user": str(user)}
