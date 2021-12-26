import json
import shutil

import pytest

from nlp import io, paths, utils


def test_write_raw_posts(monkeypatch, tmp_path, sample_posts):
    """Test that we read local JSON file"""
    monkeypatch.setattr(paths, "get_raw_data_dir", lambda: tmp_path)
    file_path = io.write_raw_posts(sample_posts)
    assert file_path.exists()
    assert json.loads(file_path.read_text()) == sample_posts


def test_read_raw_posts(sample_posts, sample_posts_id):
    """Test that we read local JSON file"""
    posts = io.read_raw_posts(sample_posts_id)
    assert posts == sample_posts


def test_read_from_json_file_does_not_exist(sample_posts):
    """Test that we read local JSON file"""
    with pytest.raises(AssertionError):
        io.read_raw_posts("nonexistent_posts.json")


def test_write_train_docs(monkeypatch, tmp_path, sample_doc_bin):
    """Test that we can writeout train binary data to disk in DocBin format"""
    monkeypatch.setattr(paths, "get_processed_data_dir", lambda: tmp_path)
    doc_bin_path = io.write_train_docs(sample_doc_bin, utils.generate_run_id())
    assert doc_bin_path.exists()


def test_write_valid_docs(monkeypatch, tmp_path, sample_doc_bin):
    """Test that we can writeout validate binary data to disk in DocBin format"""
    monkeypatch.setattr(paths, "get_processed_data_dir", lambda: tmp_path)
    doc_bin_path = io.write_valid_docs(sample_doc_bin, utils.generate_run_id())
    assert doc_bin_path.exists()


def test_generate_config(monkeypatch, tmp_path, sample_posts_id):
    """Test that config was generated to config dir"""
    base_config = paths.get_config_dir() / "base.cfg"
    monkeypatch.setattr(paths, "get_config_dir", lambda: tmp_path)
    shutil.copy(base_config, paths.get_config_dir() / "base.cfg")
    config_path = io.generate_config(sample_posts_id)
    assert config_path.exists()
