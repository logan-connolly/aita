from fastapi import APIRouter
from starlette.requests import Request
from starlette.status import HTTP_200_OK

from app.schemas.reddit import RedditInfo

router = APIRouter()


@router.get("/", response_model=RedditInfo, status_code=HTTP_200_OK)
async def get_connection_info(request: Request):
    """Check whether you are connected with Reddit API."""
    return {"user": request.app.state.user}
