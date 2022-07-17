import json
import shutil
import uuid
from pathlib import Path

import pytest
from spacy.tokens import DocBin

from nlp import paths, transform


@pytest.fixture
def data_dirs(tmp_path: Path, monkeypatch) -> paths.DataDirs:
    tmp_data_dirs = paths.DataDirs.create(tmp_path)
    original_base_cfg = paths.DATA_DIRS.configs / "base.cfg"
    shutil.copy(original_base_cfg, tmp_data_dirs.configs / "base.cfg")
    monkeypatch.setattr(paths, "DATA_DIRS", tmp_data_dirs)
    return tmp_data_dirs


@pytest.fixture
def sample_posts() -> list[transform.RawPost]:
    """Return simple sample posts that will be used for testing"""
    return [
        {
            "reddit_id": "hc7wd7",
            "title": "AITA",
            "label": "NTA",
            "text": "sample text",
            "id": 202,
        },
        {
            "reddit_id": "hc6wd6",
            "title": "AITA",
            "label": "YTA",
            "text": "sample text",
            "id": 203,
        },
    ]


@pytest.fixture
def sample_posts_id(
    data_dirs: paths.DataDirs, sample_posts: list[transform.RawPost]
) -> str:
    """Take sample post fixture and write to tmp directory (mocked as data/raw)"""
    run_id = str(uuid.uuid4())
    run_id_path = data_dirs.create_run_id(paths.DataDir.RAW.value, run_id)
    (run_id_path / "posts.json").write_text(json.dumps(sample_posts))
    return run_id


@pytest.fixture
def sample_doc_bin(sample_posts: list[transform.RawPost]) -> DocBin:
    """Convert sample posts to doc bin"""
    tuple_list = transform.parse_posts(sample_posts)
    docs = transform.make_docs(tuple_list)
    return transform.convert_to_doc_binary(docs)
