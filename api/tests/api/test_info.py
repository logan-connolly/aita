from starlette.status import HTTP_200_OK

from app.core.config import settings


def test_get_reddit_info(client):
    """Test that reddit user info is retrieved"""
    resp = client.get(f"{settings.api_version}/info/account/")
    assert resp.status_code == HTTP_200_OK


def test_get_reddit_labels(client):
    """Test that label counts are returned for the reddit posts"""
    resp = client.get(f"{settings.api_version}/info/label/")
    assert resp.status_code == HTTP_200_OK
