from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from app.core.config import settings


def test_get_reddit_info(client):
    """Test that reddit user info is retrieved"""
    resp = client.get(f"{settings.api.version}/reddit/info/")
    assert resp.status_code == HTTP_200_OK


def test_trigger_reddit_sync(client):
    """Test that post sync is instantiated"""
    resp = client.post(f"{settings.api.version}/reddit/sync/?limit=10")
    assert resp.status_code == HTTP_201_CREATED


def test_get_reddit_sync_info(client):
    """Test that info regarding last sync is returned"""
    resp = client.get(f"{settings.api.version}/reddit/sync/")
    assert resp.status_code == HTTP_200_OK


def test_get_reddit_labels(client):
    """Test that label counts are returned for the reddit posts"""
    resp = client.get(f"{settings.api.version}/reddit/label/")
    assert resp.status_code == HTTP_200_OK
