from types import SimpleNamespace

import pytest

from nlp import cli, http, model


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


@pytest.mark.usefixtures("data_dirs")
def test_download(monkeypatch, sample_posts):
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

    raw_posts_path = cli.download(api_url)
    assert raw_posts_path.exists()


@pytest.mark.usefixtures("data_dirs")
def test_preprocess(sample_posts_id):
    """Test preprocess pipeline and that doc bin data was written out"""
    processed_dir = cli.preprocess(run_id=sample_posts_id, labels="YTA,NTA")
    assert (processed_dir / sample_posts_id / "train.spacy").exists()
    assert (processed_dir / sample_posts_id / "valid.spacy").exists()


@pytest.mark.usefixtures("data_dirs")
def test_train(monkeypatch, sample_posts_id):
    """Test that training model works"""
    monkeypatch.setattr(model, "train", lambda *_: None)
    train_dir = cli.train(sample_posts_id)
    assert train_dir.exists()
