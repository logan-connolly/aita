from types import SimpleNamespace

import pytest

from nlp import cli, http, model

FAKE_ID = "68bc414d-918a-43e7-8d2b-9bd2f7783360"
EXAMPLE_LABELS = "NTA,YTA"
FAKE_URL = "http://fakeaddress:8000/api/v1"


def test_parse_download_command():
    argv = [cli.Command.DOWNLOAD.value]
    args = cli.parse_args(argv)

    assert args.command == cli.Command.DOWNLOAD.value


def test_parse_preprocess_command():
    argv = [cli.Command.PREPROCESS.value, FAKE_ID, "--labels", EXAMPLE_LABELS]
    args = cli.parse_args(argv)

    assert args.command == cli.Command.PREPROCESS.value
    assert args.id == FAKE_ID
    assert args.labels == EXAMPLE_LABELS


def test_parse_train_command():
    argv = [cli.Command.TRAIN.value, FAKE_ID]
    args = cli.parse_args(argv)

    assert args.command == cli.Command.TRAIN.value
    assert args.id == FAKE_ID


@pytest.mark.usefixtures("data_dirs")
def test_download(monkeypatch, sample_posts):
    """Test that posts can be downloaded from api"""

    def mock_get_posts_response(url: str):
        assert "/posts" in url
        return SimpleNamespace(
            status_code=200,
            json=lambda: {"items": sample_posts, "total": len(sample_posts)},
        )

    monkeypatch.setattr(http.requests, "get", mock_get_posts_response)
    raw_posts_path = cli.download(FAKE_URL)

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
