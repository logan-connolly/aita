from json import dumps

from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from app.core.config import settings

POST = dict(reddit_id="xkl123", title="AITA?", label="NTA", text="Once upon a time")
POST_ID = None

# TODO: don't make fixtures mutability - should work asyncronously as well
# TODO: look again for wrappers/solutions for creating DB sandbox


def test_add_post(client):
    """Test that post is added to DB"""
    global POST_ID
    resp = client.post(f"{settings.api.version}/posts/", data=dumps(POST))
    POST_ID = resp.json()["id"]
    POST.update({"id": POST_ID})
    assert resp.status_code == HTTP_201_CREATED
    assert resp.json() == POST


def test_get_post(client):
    """Test that post can be retrieved from DB by id"""
    resp = client.get(f"{settings.api.version}/posts/{POST_ID}/")
    assert resp.status_code == HTTP_200_OK
    assert resp.json() == POST


def test_get_posts(client):
    """Test that a list of posts can be retrieved from DB"""
    resp = client.get(f"{settings.api.version}/posts/")
    assert resp.status_code == HTTP_200_OK
    assert any(POST == post for post in resp.json())


def test_update_post(client):
    """Test that dummy post is properly updated"""
    POST["label"] = "YTA"
    payload = dumps(dict(label="YTA"))
    resp = client.put(f"{settings.api.version}/posts/{POST_ID}/", data=payload)
    assert resp.status_code == HTTP_200_OK
    assert resp.json() == POST


def test_remove_post(client):
    """Test that dummy post is deleted from DB"""
    resp = client.delete(f"{settings.api.version}/posts/{POST_ID}/")
    assert resp.status_code == HTTP_200_OK
    assert resp.json() == POST
