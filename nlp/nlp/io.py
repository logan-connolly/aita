import json
from pathlib import Path
from typing import Union

from spacy.tokens import DocBin

from nlp import paths
from nlp.utils import generate_run_id

RawPost = dict[str, Union[int, str]]


def read_from_json_file(run_id: str) -> list[RawPost]:
    """Read in local raw posts that were exported from API"""
    file_path = paths.get_raw_data_dir() / f"{run_id}.json"
    assert file_path.exists(), "Can't find file"
    text = file_path.read_text()
    return json.loads(text)


def write_docs(doc_bin: DocBin, path: Path) -> Path:
    """Write doc binary to disk"""
    assert path.parent.exists(), "Missing parent directory for docs"
    doc_bin.to_disk(path)
    return path


def write_train_docs(doc_bin: DocBin) -> Path:
    """Write train data to proper path"""
    filename = f"{generate_run_id()}_train.spacy"
    file_path = paths.get_processed_data_dir() / filename
    return write_docs(doc_bin, file_path)


def write_valid_docs(doc_bin: DocBin) -> Path:
    """Write validation data to proper path"""
    filename = f"{generate_run_id()}_valid.spacy"
    file_path = paths.get_processed_data_dir() / filename
    return write_docs(doc_bin, file_path)
