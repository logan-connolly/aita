from nlp.io import RawPost

TextLabel = tuple[str, str]


def parse_post(post: RawPost) -> TextLabel:
    """Given a raw post extract text and label values"""
    try:
        return post["text"], post["label"]
    except KeyError:
        raise ValueError("Expected a post with `text` and `label` as keys")


def parse_posts(posts: list[RawPost]) -> list[TextLabel]:
    """Parse raw posts into text/label pairs (input for spacy NLP train pipeline)"""
    return [parse_post(post) for post in posts]
