from spacy.tokens import Doc, DocBin

from nlp import transform


def test_parse_posts(sample_posts):
    """Read in raw posts returning text/label tuple pairs"""
    tuple_list = transform.parse_posts(sample_posts)
    assert tuple_list == [("sample text", "NTA")]


def test_split_train_data():
    """Test that we can take list of tuples and return splits"""
    assert None


def test_make_docs(sample_posts):
    """Test that docs are created from list of tuples"""
    tuple_list = transform.parse_posts(sample_posts)
    docs = transform.make_docs(tuple_list)
    assert all(isinstance(doc, Doc) for doc in docs)


def test_convert_to_doc_binary(sample_posts):
    """Test that docs are correctly written to binary format"""
    tuple_list = transform.parse_posts(sample_posts)
    docs = transform.make_docs(tuple_list)
    doc_bin = transform.convert_to_doc_binary(docs)
    assert isinstance(doc_bin, DocBin)
