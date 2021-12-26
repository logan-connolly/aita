from nlp import model, paths, utils


def test_fit(monkeypatch, tmp_path):
    """Test that directories exists after training"""
    monkeypatch.setattr(model, "train", lambda *_: None)
    monkeypatch.setattr(paths, "get_model_dir", lambda: tmp_path)

    run_id = utils.generate_run_id()
    config_path = tmp_path / "fake.cfg"
    train_dir = model.fit(run_id, config_path)
    assert train_dir.exists()
