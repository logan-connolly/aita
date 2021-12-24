import argparse
from pathlib import Path
from typing import Optional, Sequence

from nlp import http, io, paths, transform


def validate_args(args: argparse.Namespace) -> argparse.Namespace:
    """Make sure that passed args are correct"""
    acceptable_commands = ("download", "preprocess")
    assert args.command in acceptable_commands, f"Unsupported command: {args.command!r}"
    return args


def parse_args(argv: Optional[Sequence[str]]) -> argparse.Namespace:
    """Parse command line arguments from user"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "command", help="Available commands to perform (download, preprocess)"
    )
    parser.add_argument(
        "--id", dest="id", help="ID for run id that is used to fetch stored data"
    )
    parser.add_argument(
        "--labels", dest="labels", help="Comma-separted string of labels to download"
    )
    parser.add_argument(
        "--url", dest="url", help="Url for fetching posts from running API instance"
    )
    return parser.parse_args(argv)


def download(api_url: str) -> Path:
    """Download posts from running API instance"""
    raw_posts = http.fetch_posts(api_url)
    return io.write_raw_posts(raw_posts)


def preprocess(run_id: str, labels: Optional[str]) -> Path:
    """Read in raw posts and process data to satisfy spacy train api"""
    raw_posts = io.read_raw_posts(run_id)
    parsed_posts = transform.parse_posts(raw_posts)
    filtered_posts = transform.filter_posts(parsed_posts, labels)
    docs = transform.make_docs(filtered_posts)
    split_data = transform.split_data(docs, train_ratio=0.6)
    io.write_train_docs(transform.convert_to_doc_binary(split_data.train), run_id)
    io.write_valid_docs(transform.convert_to_doc_binary(split_data.valid), run_id)
    return paths.get_processed_data_dir()
