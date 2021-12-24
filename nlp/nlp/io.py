import json
from pathlib import Path
from typing import Union

from spacy.tokens import DocBin

from nlp import paths, utils

RawPost = dict[str, Union[int, str]]


def write_raw_posts(posts: list[RawPost]) -> Path:
    """Write raw posts fetched from api to disk as JSON"""
    run_id = utils.generate_run_id()
    run_id_dir = paths.get_raw_data_dir() / run_id
    run_id_dir.mkdir(parents=True, exist_ok=True)
    file_path = run_id_dir / "posts.json"
    file_path.write_text(json.dumps(posts))
    return file_path


def read_raw_posts(run_id: str) -> list[RawPost]:
    """Read in local raw posts that were exported from API"""
    file_path = paths.get_raw_data_dir() / run_id / "posts.json"
    assert file_path.exists(), f"Can't find file: {file_path}"
    text = file_path.read_text()
    return json.loads(text)


def write_docs(doc_bin: DocBin, path: Path) -> Path:
    """Write doc binary to disk"""
    path.parent.mkdir(parents=True, exist_ok=True)
    assert path.parents[1].exists(), f"Missing directory: {path.parents[1]}"
    doc_bin.to_disk(path)
    return path


def write_train_docs(doc_bin: DocBin, run_id: str) -> Path:
    """Write train data to proper path"""
    file_path = paths.get_processed_data_dir() / run_id / "train.spacy"
    return write_docs(doc_bin, file_path)


def write_valid_docs(doc_bin: DocBin, run_id: str) -> Path:
    """Write validation data to proper path"""
    file_path = paths.get_processed_data_dir() / run_id / "valid.spacy"
    return write_docs(doc_bin, file_path)
