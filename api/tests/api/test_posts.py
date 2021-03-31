from json import dumps

from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from app.core.config import settings

POST = dict(id="xkl123", title="AITA?", label="NTA", text="Once upon a time")


class TestPost:
    def test_add_post(self, client):
        resp = client.post(f"{settings.api.version}/posts/", data=dumps(POST))
        assert resp.status_code == HTTP_201_CREATED
        assert resp.json() == POST

    def test_get_post(self, client):
        resp = client.get(f"{settings.api.version}/posts/{POST['id']}/")
        assert resp.status_code == HTTP_200_OK
        assert resp.json() == POST

    def test_get_posts(self, client):
        resp = client.get(f"{settings.api.version}/posts/")
        assert resp.status_code == HTTP_200_OK
        assert resp.json() == [POST]

    def test_update_post(self, client):
        POST["label"] = "YTA"
        payload = dumps(dict(label="YTA"))
        resp = client.put(f"{settings.api.version}/posts/{POST['id']}/", data=payload)
        assert resp.status_code == HTTP_200_OK
        assert resp.json() == POST

    def test_remove_post(self, client):
        resp = client.delete(f"{settings.api.version}/posts/{POST['id']}/")
        assert resp.status_code == HTTP_200_OK
        assert resp.json() == POST
