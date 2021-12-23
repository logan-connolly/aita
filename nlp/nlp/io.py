import json
from pathlib import Path

from spacy.tokens import DocBin

from nlp import paths
from nlp.utils import get_date_stamp

RawPost = dict[str, str]


def read_from_json_file(file_name: str) -> list[RawPost]:
    """Read in local raw posts that were exported from API"""
    file_path = paths.get_raw_data_dir() / file_name
    assert file_path.exists(), "Can't find file"
    text = file_path.read_text()
    return json.loads(text)


def write_docs(doc_bin: DocBin, path: Path) -> None:
    """Write doc binary to disk"""
    assert path.parent.exists(), "Missing parent directory for docs"
    doc_bin.to_disk(path)


def write_train_docs(doc_bin: DocBin) -> None:
    """Write train data to proper path"""
    filename = f"{get_date_stamp()}_train.spacy"
    file_path = paths.get_processed_data_dir() / filename
    write_docs(doc_bin, file_path)


def write_valid_docs(doc_bin: DocBin) -> None:
    """Write validation data to proper path"""
    filename = f"{get_date_stamp()}_valid.spacy"
    file_path = paths.get_processed_data_dir() / filename
    write_docs(doc_bin, file_path)
