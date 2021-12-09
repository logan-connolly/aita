from pathlib import Path


def get_project_dir() -> Path:
    """Returns path object to root of nlp project"""
    return Path(__file__).parents[1]


def get_data_dir() -> Path:
    """Returns path object to root of data directory"""
    return get_project_dir() / "data"


def get_raw_data_dir() -> Path:
    """Returns path object to raw data directory"""
    return get_data_dir() / "raw"
