from httpx import AsyncClient
from starlette import status

from app.core.config import settings
from app.db.tables import Post


async def test_post_create(async_client: AsyncClient):
    """Test that ingredient can be created"""
    url = f"{settings.api_version}/posts/"
    id_ = str(Post.generate_post_id("xkl123"))
    payload = {"id": id_, "title": "AITA?", "label": "NTA", "text": "test"}

    response = await async_client.post(url, json=payload)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {
        "id": response.json()["id"],
        "title": payload["title"],
        "label": payload["label"],
        "text": payload["text"],
    }
