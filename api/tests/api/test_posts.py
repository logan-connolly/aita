import pytest

from json import dumps


payload = dict(post_id="1234", label="NTA", text="Once upon a time...")


@pytest.mark.usefixtures("create_tables")
class TestSource:
    @pytest.mark.asyncio
    async def test_add_post(self, host, event_loop, server, session):
        global payload
        async with session.post(f"{host}/posts/", data=dumps(payload)) as resp:
            response = await resp.json()
            payload.update({"id": response.get("id")})
            assert response == payload
            assert resp.status == 201

    @pytest.mark.asyncio
    async def test_get_post(self, host, event_loop, server, session):
        global payload
        async with session.get(f"{host}/posts/{payload['id']}") as resp:
            assert resp.status == 200
            assert await resp.json() == payload

    @pytest.mark.asyncio
    async def test_get_posts(self, host, event_loop, server, session):
        global payload
        async with session.get(f"{host}/posts/") as resp:
            assert resp.status == 200
            assert await resp.json() == [payload]

    @pytest.mark.asyncio
    async def test_update_post(self, host, event_loop, server, session):
        global payload
        payload["label"] = "YTA"

        async with session.put(
            f"{host}/posts/{payload['id']}", data=dumps(payload)
        ) as resp:
            assert resp.status == 200
            assert await resp.json() == payload

    @pytest.mark.asyncio
    async def test_remove_post(self, host, event_loop, server, session):
        global payload
        async with session.delete(f"{host}/posts/{payload['id']}") as resp:
            assert resp.status == 200
            assert await resp.json() == payload
