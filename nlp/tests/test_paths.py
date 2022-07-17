from pathlib import Path

from nlp import paths


def test_create_data_dirs(tmp_path: Path):
    data_dirs = paths.DataDirs.create(tmp_path)

    for data_dir_name in data_dirs.__dataclass_fields__:
        assert getattr(data_dirs, data_dir_name).exists()
