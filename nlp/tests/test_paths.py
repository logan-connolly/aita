from nlp import paths


def test_get_project_dir():
    """Test that we can access module root `nlp`"""
    root_path = paths.get_project_dir()
    assert root_path.name == "nlp"
    assert root_path.parent.name == "aita"


def test_get_data_dir():
    """Test that we can access data directory"""
    data_dir = paths.get_data_dir()
    assert data_dir.name == "data"
    assert data_dir.parent.name == "nlp"


def test_get_raw_data_dir():
    """Test that we can access raw data directory"""
    data_dir = paths.get_raw_data_dir()
    assert data_dir.name == "raw"
    assert data_dir.parent.name == "data"