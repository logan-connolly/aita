import math
import random
from dataclasses import dataclass

from spacy.tokens import Doc, DocBin

from nlp.io import RawPost
from nlp.tokenizer import nlp

TextLabel = tuple[str, str]


@dataclass
class SplitData:
    train: list[Doc]
    valid: list[Doc]


def parse_post(post: RawPost) -> TextLabel:
    """Given a raw post extract text and label values"""
    try:
        return post["text"], post["label"]
    except KeyError:
        raise ValueError("Expected a post with `text` and `label` as keys")


def parse_posts(posts: list[RawPost]) -> list[TextLabel]:
    """Parse raw posts into text/label pairs (input for spacy NLP train pipeline)"""
    return [parse_post(post) for post in posts]


def make_docs(posts: list[TextLabel]) -> list[Doc]:
    """Make documents that spacy can use for training"""
    docs = []
    for doc, label in nlp.pipe(texts=posts, as_tuples=True):
        if label == "YTA":
            doc.cats["positive"] = 1
            doc.cats["negative"] = 0
        else:
            doc.cats["positive"] = 0
            doc.cats["negative"] = 1
        docs.append(doc)
    return docs


def split_data(docs: list[Doc], train_ratio: float = 0.6) -> SplitData:
    """Shuffle data and split into train/valid sets"""
    assert 0 < train_ratio < 1, "Ratio must be greater than 0 and less than 1"
    docs_copy = docs.copy()
    random.shuffle(docs_copy)
    cutoff = math.floor(len(docs_copy) * train_ratio)
    return SplitData(train=docs_copy[:cutoff], valid=docs_copy[cutoff:])


def convert_to_doc_binary(docs: list[Doc]) -> DocBin:
    """Take list of docs and convert to binary for storage"""
    return DocBin(docs=docs)
