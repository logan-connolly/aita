import argparse
import enum
from pathlib import Path
from typing import Optional, Sequence

from nlp import http, io, model, paths, transform


class Command(enum.Enum):
    DOWNLOAD = "download"
    PREPROCESS = "preprocess"
    TRAIN = "train"


def parse_args(argv: Optional[Sequence[str]]) -> argparse.Namespace:
    """Parse command line arguments from user"""
    parser = argparse.ArgumentParser(description="Create NLP model.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    download = subparsers.add_parser(Command.DOWNLOAD.value)
    download.add_argument(
        "--url",
        default="http://localhost:8000/api/v1",
        help="URL to the running AITA API (default: http://localhost:8000/api/v1).",
    )

    preprocess = subparsers.add_parser(Command.PREPROCESS.value)
    preprocess.add_argument("id", help="Run ID to fetch stored data.")
    preprocess.add_argument("--labels", default="", help="Comma-separted labels.")

    train = subparsers.add_parser(Command.TRAIN.value)
    train.add_argument("id", help="Run ID to fetch stored data.")

    return parser.parse_args(argv)


def download(api_url: str) -> Path:
    """Download posts from running API instance"""
    raw_posts = http.fetch_posts(api_url)
    return io.write_raw_posts(raw_posts)


def preprocess(run_id: str, labels: str) -> Path:
    """Read in raw posts and process data to satisfy spacy train api"""
    raw_posts = io.read_raw_posts(run_id)

    parsed_posts = transform.parse_posts(raw_posts)
    filtered_posts = transform.filter_posts(parsed_posts, labels)

    docs = transform.make_docs(filtered_posts)
    split_data = transform.split_data(docs, train_ratio=0.6)

    train_docs = transform.convert_to_doc_binary(split_data.train)
    valid_docs = transform.convert_to_doc_binary(split_data.valid)

    io.write_docs(train_docs, transform.Split.TRAIN.value, run_id)
    io.write_docs(valid_docs, transform.Split.VALID.value, run_id)

    return paths.DATA_DIRS.processed


def train(run_id: str) -> Path:
    """Train spacy model with preprocessed doc bin data"""
    config_path = io.generate_config(run_id)
    return model.fit(run_id, config_path)
