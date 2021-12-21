from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from app.core.config import settings


def test_trigger_reddit_sync(client):
    """Test that post sync is instantiated"""
    resp = client.post(f"{settings.api.version}/sync/?filter=top&limit=50")
    assert resp.status_code == HTTP_201_CREATED


def test_get_reddit_sync_info(client):
    """Test that info regarding last sync is returned"""
    resp = client.get(f"{settings.api.version}/sync/")
    assert resp.status_code == HTTP_200_OK
