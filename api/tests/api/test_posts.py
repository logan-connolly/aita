import pytest

from json import dumps


post = dict(post_id="1234", label="NTA", text="Once upon a time...")


class TestPost:
    @pytest.mark.asyncio
    async def test_add_post(self, host, event_loop, server, session):
        global post
        async with session.post(f"{host}/posts/", data=dumps(post)) as resp:
            assert resp.status == 201
            response = await resp.json()
            post.update({"id": response.get("id")})
            assert response == post

    @pytest.mark.asyncio
    async def test_get_post(self, host, event_loop, server, session):
        global post
        async with session.get(f"{host}/posts/{post['id']}") as resp:
            assert resp.status == 200
            assert await resp.json() == post

    @pytest.mark.asyncio
    async def test_get_posts(self, host, event_loop, server, session):
        global post
        async with session.get(f"{host}/posts/") as resp:
            assert resp.status == 200
            assert await resp.json() == [post]

    @pytest.mark.asyncio
    async def test_update_post(self, host, event_loop, server, session):
        global post
        post["label"] = "YTA"
        async with session.put(
            f"{host}/posts/{post['id']}", data=dumps(dict(label="YTA"))
        ) as resp:
            assert resp.status == 200
            assert await resp.json() == post

    @pytest.mark.asyncio
    async def test_remove_post(self, host, event_loop, server, session):
        global post
        async with session.delete(f"{host}/posts/{post['id']}") as resp:
            assert resp.status == 200
            assert await resp.json() == post
