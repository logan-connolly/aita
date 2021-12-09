import pytest

from nlp import io


def test_read_from_json_file(sample_posts, sample_posts_file):
    """Test that we read local JSON file"""
    posts = io.read_from_json_file(sample_posts_file.name)
    assert posts == sample_posts


def test_read_from_json_file_does_not_exist(sample_posts):
    """Test that we read local JSON file"""
    with pytest.raises(AssertionError):
        io.read_from_json_file("nonexistent_posts.json")


def test_writeout_train_data():
    """Test that we can writeout TrainSplits to disk in DocBin format"""
    assert None
