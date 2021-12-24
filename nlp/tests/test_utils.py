from nlp import utils


def test_generate_run_id():
    """Test that date stamp is in correct format"""
    assert len(utils.generate_run_id()) == 36
