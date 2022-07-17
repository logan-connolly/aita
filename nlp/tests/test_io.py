import json

import pytest

from nlp import io, transform


@pytest.mark.usefixtures("data_dirs")
def test_write_raw_posts(sample_posts):
    """Test that we read local JSON file"""
    file_path = io.write_raw_posts(sample_posts)
    assert file_path.exists()
    assert json.loads(file_path.read_text()) == sample_posts


def test_read_raw_posts(sample_posts, sample_posts_id):
    """Test that we read local JSON file"""
    posts = io.read_raw_posts(sample_posts_id)
    assert posts == sample_posts


def test_read_from_json_file_does_not_exist():
    """Test that we read local JSON file"""
    with pytest.raises(AssertionError):
        io.read_raw_posts("nonexistent_posts.json")


@pytest.mark.usefixtures("data_dirs")
def test_write_train_docs(sample_posts_id, sample_doc_bin):
    """Test that we can writeout train binary data to disk in DocBin format"""
    docs = io.write_docs(sample_doc_bin, transform.Split.TRAIN.value, sample_posts_id)
    assert docs.exists()


def test_write_valid_docs(sample_posts_id, sample_doc_bin):
    """Test that we can writeout validate binary data to disk in DocBin format"""
    docs = io.write_docs(sample_doc_bin, transform.Split.VALID.value, sample_posts_id)
    assert docs.exists()


@pytest.mark.usefixtures("data_dirs")
def test_generate_config(sample_posts_id):
    """Test that config was generated to config dir"""
    config_path = io.generate_config(sample_posts_id)
    assert config_path.exists()
