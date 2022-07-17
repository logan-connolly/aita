from nlp import model, paths


def test_fit(data_dirs: paths.DataDirs, sample_posts_id: str, monkeypatch):
    """Test that directories exists after training"""
    monkeypatch.setattr(model, "train", lambda *_: None)
    config_path = data_dirs.models / "fake.cfg"

    train_dir = model.fit(sample_posts_id, config_path)

    assert train_dir.exists()
