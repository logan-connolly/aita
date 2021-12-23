import pytest
from freezegun import freeze_time

from nlp import io, paths


def test_read_from_json_file(sample_posts, sample_posts_file):
    """Test that we read local JSON file"""
    posts = io.read_from_json_file(sample_posts_file.name)
    assert posts == sample_posts


def test_read_from_json_file_does_not_exist(sample_posts):
    """Test that we read local JSON file"""
    with pytest.raises(AssertionError):
        io.read_from_json_file("nonexistent_posts.json")


@freeze_time("2021-12-25")
def test_write_train_docs(monkeypatch, tmp_path, sample_doc_bin):
    """Test that we can writeout train binary data to disk in DocBin format"""
    monkeypatch.setattr(paths, "get_processed_data_dir", lambda: tmp_path)
    io.write_train_docs(sample_doc_bin)
    assert (tmp_path / "20211225_train.spacy").exists()


@freeze_time("2021-12-25")
def test_write_valid_docs(monkeypatch, tmp_path, sample_doc_bin):
    """Test that we can writeout validate binary data to disk in DocBin format"""
    monkeypatch.setattr(paths, "get_processed_data_dir", lambda: tmp_path)
    io.write_valid_docs(sample_doc_bin)
    assert (tmp_path / "20211225_valid.spacy").exists()
