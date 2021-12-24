import json

import pytest
from spacy.tokens import DocBin

from nlp import paths, transform, utils


@pytest.fixture
def sample_posts() -> list[transform.RawPost]:
    """Return simple sample posts that will be used for testing"""
    return [
        {
            "reddit_id": "hc7wd7",
            "title": "AITA for having pot cookies out in the open in my own home?",
            "label": "NTA",
            "text": "sample text",
            "id": 202,
        },
        {
            "reddit_id": "hc6wd6",
            "title": "AITA for cheating on my homework",
            "label": "YTA",
            "text": "sample text",
            "id": 203,
        },
    ]


@pytest.fixture
def sample_posts_id(monkeypatch, tmp_path, sample_posts) -> str:
    """Take sample post fixture and write to tmp directory (mocked as data/raw)"""
    monkeypatch.setattr(paths, "get_raw_data_dir", lambda: tmp_path)
    run_id = utils.generate_run_id()
    mock_posts_dir = tmp_path / run_id
    mock_posts_dir.mkdir(parents=True, exist_ok=True)
    mock_posts_path = mock_posts_dir / "posts.json"
    mock_posts_path.write_text(json.dumps(sample_posts))
    return run_id


@pytest.fixture
def sample_doc_bin(sample_posts) -> DocBin:
    """Convert sample posts to doc bin"""
    tuple_list = transform.parse_posts(sample_posts)
    docs = transform.make_docs(tuple_list)
    return transform.convert_to_doc_binary(docs)
