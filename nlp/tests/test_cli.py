from nlp import cli, io


def test_preprocess(monkeypatch, tmp_path, sample_posts_id):
    """Test preprocess pipeline and that doc bin data was written out"""
    monkeypatch.setattr(io.paths, "get_processed_data_dir", lambda: tmp_path)
    processed_dir = cli.preprocess(sample_posts_id)
    assert (processed_dir / sample_posts_id / "train.spacy").exists()
    assert (processed_dir / sample_posts_id / "valid.spacy").exists()
