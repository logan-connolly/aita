import json
from pathlib import Path

from spacy.cli import fill_config
from spacy.cli.init_config import save_config
from spacy.tokens import DocBin

from nlp import paths

RawPost = dict[str, int | str]


def write_raw_posts(posts: list[RawPost]) -> Path:
    """Write raw posts fetched from api to disk as JSON"""
    run_id_path = paths.DATA_DIRS.create_run_id(paths.DataDir.RAW.value)
    posts_path = run_id_path / "posts.json"
    posts_path.write_text(json.dumps(posts))
    return posts_path


def read_raw_posts(run_id: str) -> list[RawPost]:
    """Read in local raw posts that were exported from API"""
    run_id_path = paths.DATA_DIRS.get_run_id(paths.DataDir.RAW.value, run_id)
    posts_path = run_id_path / "posts.json"
    return json.loads(posts_path.read_text())


def write_docs(doc_bin: DocBin, stage: str, run_id: str) -> Path:
    """Write doc binary to disk"""
    run_id_path = paths.DATA_DIRS.create_run_id(paths.DataDir.PROCESSED.value, run_id)
    doc_file_path = run_id_path / f"{stage}.spacy"
    doc_bin.to_disk(doc_file_path)
    return doc_file_path


def generate_config(run_id: str) -> Path:
    """Load spacy config from disk based on run id"""
    base_config_path = paths.DATA_DIRS.configs / "base.cfg"
    config_path = paths.DATA_DIRS.configs / f"{run_id}.cfg"

    _, cfg = fill_config(config_path, base_config_path)

    cfg["paths"]["train"] = str(paths.DATA_DIRS.processed / run_id / "train.spacy")
    cfg["paths"]["dev"] = str(paths.DATA_DIRS.processed / run_id / "valid.spacy")

    save_config(cfg, config_path)

    return config_path
