from nlp import transform


def test_parse_posts(sample_posts):
    """Read in raw posts returning text/label tuple pairs"""
    tuple_list = transform.parse_posts(sample_posts)
    assert tuple_list == [("sample text", "NTA")]


def test_split_train_data():
    """Test that we can take list of tuples and return splits
    input: list[tuple[str,str]]
    output: TrainSplits"""
    assert None
