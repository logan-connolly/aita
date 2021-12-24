from types import SimpleNamespace


from nlp import http


def test_get_number_of_pages(monkeypatch):
    """Test that the proper number of pages is returned"""
    expected_pages = 2
    monkeypatch.setattr(
        http.requests,
        "get",
        lambda _: SimpleNamespace(
            status_code=200, json=lambda: {"posts": http.PAGE_LIMIT * expected_pages}
        ),
    )
    n_pages = http.get_number_of_pages(api_url="http://madeupurl:8000/api/v1")
    assert n_pages == expected_pages


def test_fetch_posts(monkeypatch):
    """Test that two pages of posts items are fetched from api"""
    n_pages = 2
    items = [{"a": 1}, {"b": 2}, {"c": 1}]
    monkeypatch.setattr(http, "get_number_of_pages", lambda _: n_pages)
    monkeypatch.setattr(
        http.requests,
        "get",
        lambda _: SimpleNamespace(status_code=200, json=lambda: {"items": items}),
    )
    posts = http.fetch_posts(api_url="http://madeupurl:8000/api/v1")
    assert posts == [*items, *items]
