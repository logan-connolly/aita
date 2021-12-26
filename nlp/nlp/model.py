from nlp import paths
from pathlib import Path

from spacy.cli.train import train


def fit(run_id: str, config_path: Path) -> Path:
    """Train model based on generated configuration"""
    train_dir = paths.get_model_dir() / run_id
    train_dir.mkdir(parents=True, exist_ok=True)
    train(config_path, train_dir)
    return train_dir
