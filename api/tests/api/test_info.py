from httpx import AsyncClient
from starlette import status

from app.core.config import settings


async def test_get_reddit_info(async_client: AsyncClient):
    """Test that reddit user info is retrieved"""
    resp = await async_client.get(f"{settings.api_version}/info/account/")
    assert resp.status_code == status.HTTP_200_OK


async def test_get_reddit_labels(async_client: AsyncClient):
    """Test that label counts are returned for the reddit posts"""
    resp = await async_client.get(f"{settings.api_version}/info/label/")
    assert resp.status_code == status.HTTP_200_OK
