import json

import pytest

from nlp import paths


@pytest.fixture
def sample_posts():
    """Return simple sample posts that will be used for testing"""
    return [
        {
            "reddit_id": "hc7wd7",
            "title": "AITA for having pot cookies out in the open in my own home?",
            "label": "NTA",
            "text": "sample text",
            "id": 202,
        }
    ]


@pytest.fixture
def sample_posts_file(monkeypatch, tmp_path, sample_posts):
    """Take sample post fixture and write to tmp directory (mocked as data/raw)"""
    monkeypatch.setattr(paths, "get_raw_data_dir", lambda: tmp_path)
    mock_posts_path = tmp_path / "posts.json"
    mock_posts_path.write_text(json.dumps(sample_posts))
    return mock_posts_path
