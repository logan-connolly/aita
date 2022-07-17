import shutil
from types import SimpleNamespace

import pytest

from nlp import cli, http, io, model, paths


@pytest.mark.parametrize(
    "argv",
    [
        [cli.Command.DOWNLOAD.value],
        [cli.Command.PREPROCESS.value],
        [cli.Command.TRAIN.value],
    ],
)
def test_parse_command_args(argv):
    """Test that args are parsed properly"""
    args = cli.parse_args(argv)
    assert args.command == argv[0]


def test_download(monkeypatch, tmp_path, sample_posts):
    """Test that posts can be downloaded from api"""
    api_url = "http://fakeaddress:8000/api/v1"

    def mock_requests(url: str):
        if url == f"{api_url}/sync/":
            return SimpleNamespace(
                status_code=200, json=lambda: {"posts": len(sample_posts)}
            )
        else:
            return SimpleNamespace(
                status_code=200, json=lambda: {"items": sample_posts}
            )

    monkeypatch.setattr(http.requests, "get", mock_requests)
    monkeypatch.setattr(paths, "get_raw_data_dir", lambda: tmp_path)

    raw_posts_path = cli.download(api_url)
    assert raw_posts_path.exists()


def test_preprocess(monkeypatch, tmp_path, sample_posts_id):
    """Test preprocess pipeline and that doc bin data was written out"""
    monkeypatch.setattr(io.paths, "get_processed_data_dir", lambda: tmp_path)
    processed_dir = cli.preprocess(run_id=sample_posts_id, labels="YTA,NTA")
    assert (processed_dir / sample_posts_id / "train.spacy").exists()
    assert (processed_dir / sample_posts_id / "valid.spacy").exists()


def test_train(monkeypatch, tmp_path, sample_posts_id):
    """Test that training model works"""
    base_config = paths.get_config_dir() / "base.cfg"
    monkeypatch.setattr(io.paths, "get_config_dir", lambda: tmp_path)
    shutil.copy(base_config, paths.get_config_dir() / "base.cfg")
    monkeypatch.setattr(io.paths, "get_model_dir", lambda: tmp_path)
    monkeypatch.setattr(model, "train", lambda *_: None)

    train_dir = cli.train(sample_posts_id)
    assert train_dir.exists()
