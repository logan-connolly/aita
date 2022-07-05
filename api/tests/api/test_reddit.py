from httpx import AsyncClient
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND

from app.core.config import settings


async def test_trigger_reddit_sync(async_client: AsyncClient):
    """Test that post sync is instantiated"""
    resp = await async_client.post(f"{settings.api_version}/sync/?filter=top&limit=10")
    assert resp.status_code == HTTP_201_CREATED


async def test_get_reddit_sync_info(async_client: AsyncClient):
    """Test that info regarding last sync is returned"""
    resp = await async_client.get(f"{settings.api_version}/sync/")
    assert resp.status_code == HTTP_404_NOT_FOUND
