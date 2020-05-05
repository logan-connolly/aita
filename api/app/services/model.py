from loguru import logger

from app.schemas.model import ModelPayload, ModelPrediction


class AITAClassifier:
    """Model for predicting AITA class"""

    def __init__(self, path):
        self.path = path
        self.model = self._load_model()

    def _load_model(self):
        logger.debug(f"Loading model from: {self.path}")

        def model(tokens):
            return "YTA" if len(tokens) > 5 else "NTA"
        return model

    def _pre_process(self, payload: ModelPayload):
        logger.debug("Pre-processing payload.")
        return payload.text.lower().split()

    def _predict(self, tokens) -> str:
        logger.debug("Predicting AITA class.")
        return self.model(tokens)

    def _post_process(self, prediction: str) -> ModelPrediction:
        logger.debug("Post-processing prediction.")
        return ModelPrediction(prediction=prediction)

    def predict(self, payload: ModelPayload) -> ModelPrediction:
        if payload is None:
            raise ValueError(f"{payload} is not a valid payload.")

        tokens = self._pre_process(payload)
        prediction = self._predict(tokens)
        return self._post_process(prediction)
