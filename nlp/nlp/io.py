import json
from pathlib import Path
from typing import Union

from spacy.tokens import DocBin

from nlp import paths, utils

RawPost = dict[str, Union[int, str]]


def write_raw_posts(posts: list[RawPost]) -> Path:
    """Write raw posts fetched from api to disk as JSON"""
    run_id = utils.generate_run_id()
    file_path = paths.get_raw_data_dir() / f"{run_id}_posts.json"
    file_path.write_text(json.dumps(posts))
    return file_path


def read_raw_posts(run_id: str) -> list[RawPost]:
    """Read in local raw posts that were exported from API"""
    file_path = paths.get_raw_data_dir() / f"{run_id}_posts.json"
    assert file_path.exists(), "Can't find file"
    text = file_path.read_text()
    return json.loads(text)


def write_docs(doc_bin: DocBin, path: Path) -> Path:
    """Write doc binary to disk"""
    assert path.parent.exists(), "Missing parent directory for docs"
    doc_bin.to_disk(path)
    return path


def write_train_docs(doc_bin: DocBin, run_id: str) -> Path:
    """Write train data to proper path"""
    filename = f"{run_id}_train.spacy"
    file_path = paths.get_processed_data_dir() / filename
    return write_docs(doc_bin, file_path)


def write_valid_docs(doc_bin: DocBin, run_id: str) -> Path:
    """Write validation data to proper path"""
    filename = f"{run_id}_valid.spacy"
    file_path = paths.get_processed_data_dir() / filename
    return write_docs(doc_bin, file_path)
