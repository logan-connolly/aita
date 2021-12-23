from freezegun import freeze_time

from nlp import utils


@freeze_time("2021-12-25")
def test_get_date_stamp():
    """Test that date stamp is in correct format"""
    assert utils.get_date_stamp() == "20211225"
