import pytest
from spacy.tokens import Doc, DocBin

from nlp import transform


def test_parse_posts(sample_posts):
    """Read in raw posts returning text/label tuple pairs"""
    parsed_posts = transform.parse_posts(sample_posts)
    assert parsed_posts == [("AITA sample text", "NTA"), ("AITA sample text", "YTA")]


def test_parse_posts_invalid():
    """Test invalid dictionary passed as post"""
    with pytest.raises(ValueError):
        transform.parse_posts([{"not_valid_text": "value", "label": "NTA"}])


def test_filter_posts(sample_posts):
    """Test that posts are correctly filtered out by label"""
    parsed_posts = transform.parse_posts(sample_posts)
    filtered_posts = transform.filter_posts(parsed_posts, labels="NTA")
    assert all(label == "NTA" for _, label in filtered_posts)


def test_split_data(sample_posts):
    """Test that we can take list of tuples and return splits"""
    parsed_posts = transform.parse_posts(sample_posts)
    docs = transform.make_docs(parsed_posts)
    split_data = transform.split_data(docs, train_ratio=0.5)
    assert len(split_data.train) == 1
    assert len(split_data.valid) == 1


def test_make_docs(sample_posts):
    """Test that docs are created from list of tuples"""
    parsed_posts = transform.parse_posts(sample_posts)
    docs = transform.make_docs(parsed_posts)
    assert all(isinstance(doc, Doc) for doc in docs)


def test_convert_to_doc_binary(sample_posts):
    """Test that docs are correctly written to binary format"""
    parsed_posts = transform.parse_posts(sample_posts)
    docs = transform.make_docs(parsed_posts)
    doc_bin = transform.convert_to_doc_binary(docs)
    assert isinstance(doc_bin, DocBin)
