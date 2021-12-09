import json

from nlp import paths

RawPost = dict[str, str]


def read_from_json_file(file_name: str) -> list[RawPost]:
    """Read in local raw posts that were exported from API"""
    file_path = paths.get_raw_data_dir() / file_name
    assert file_path.exists(), "Can't find file"
    text = file_path.read_text()
    return json.loads(text)
