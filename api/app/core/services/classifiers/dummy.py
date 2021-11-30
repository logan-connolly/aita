from spacy.tokens.doc import Doc

from app.core.constants import AitaLabel


class DummyClassifier:
    """Dummy model classifier that outputs random AITA class"""

    def predict(self, doc: Doc) -> AitaLabel:
        return AitaLabel.NTA if len(doc) < 10 else AitaLabel.YTA
