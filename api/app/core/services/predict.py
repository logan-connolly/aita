from typing import Protocol

from loguru import logger
from spacy.tokens.doc import Doc

from app.core.constants import AitaLabel
from app.core.services.tokenizer import nlp
from app.schemas.model import ModelPayload, ModelPrediction


class Predictable(Protocol):
    """Interface for classifier model"""

    def predict(self, doc: Doc) -> AitaLabel:
        """Predicts AITA class based on text doc"""
        ...


class AitaPredictor:
    """Predictor class that processes and predicts label based on payload text"""

    def __init__(self, classifier: Predictable) -> None:
        self.classifier = classifier

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(model='{self.classifier}')"

    def _pre_process(self, payload: ModelPayload) -> Doc:
        logger.debug("Pre-processing payload.")
        return nlp(payload.text)

    def _predict(self, doc: Doc) -> AitaLabel:
        logger.debug("Predicting AITA class.")
        return self.classifier.predict(doc)

    def _post_process(self, prediction: str) -> ModelPrediction:
        logger.debug("Post-processing prediction.")
        return ModelPrediction(prediction=prediction)

    def predict(self, payload: ModelPayload) -> ModelPrediction:
        """Given a ModelPayload text predict a AITA class"""
        doc = self._pre_process(payload)
        prediction = self._predict(doc)
        return self._post_process(prediction)
