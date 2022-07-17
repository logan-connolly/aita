from pathlib import Path

from spacy.cli.train import train

from nlp import paths


def fit(run_id: str, config_path: Path) -> Path:
    """Train model based on generated configuration"""
    train_dir = paths.DATA_DIRS.create_run_id(paths.DataDir.MODELS.value, run_id)
    train(config_path, train_dir)
    return train_dir
