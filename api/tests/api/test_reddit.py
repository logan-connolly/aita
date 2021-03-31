from starlette.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED

from app.core.config import settings


class TestReddit:
    def test_get_reddit_info(self, client):
        resp = client.get(f"{settings.api.version}/reddit/info/")
        assert resp.status_code == HTTP_200_OK

    def test_get_reddit_info_invalid(self, client, monkeypatch):
        pass
