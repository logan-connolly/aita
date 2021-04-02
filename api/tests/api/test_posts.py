from json import dumps

from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from app.core.config import settings

POST = dict(id="xkl123", title="AITA?", label="NTA", text="Once upon a time")


def test_add_post(client):
    """Test that post is added to DB"""
    resp = client.post(f"{settings.api.version}/posts/", data=dumps(POST))
    assert resp.status_code == HTTP_201_CREATED
    assert resp.json() == POST


def test_get_post(client):
    """Test that post can be retrieved from DB by id"""
    resp = client.get(f"{settings.api.version}/posts/{POST['id']}/")
    assert resp.status_code == HTTP_200_OK
    assert resp.json() == POST


def test_get_posts(client):
    """Test that a list of posts can be retrieved from DB"""
    resp = client.get(f"{settings.api.version}/posts/")
    assert resp.status_code == HTTP_200_OK
    assert resp.json() == [POST]


def test_update_post(client):
    """Test that dummy post is properly updated"""
    POST["label"] = "YTA"
    payload = dumps(dict(label="YTA"))
    resp = client.put(f"{settings.api.version}/posts/{POST['id']}/", data=payload)
    assert resp.status_code == HTTP_200_OK
    assert resp.json() == POST


def test_remove_post(client):
    """Test that dummy post is deleted from DB"""
    resp = client.delete(f"{settings.api.version}/posts/{POST['id']}/")
    assert resp.status_code == HTTP_200_OK
    assert resp.json() == POST
