from nlp import paths
from pathlib import Path

from spacy.cli.train import train


def fit(run_id: str, config_path: Path) -> Path:
    """Train model based on generated configuration"""
    train_dir = paths.get_model_dir() / run_id
    train_dir.mkdir(parents=True, exist_ok=True)
    processed_dir = paths.get_processed_data_dir() / run_id
    overrides = {
        "paths.train": str(processed_dir / "train.spacy"),
        "paths.dev": str(processed_dir / "valid.spacy"),
    }
    train(config_path, train_dir, overrides=overrides)
    return train_dir
