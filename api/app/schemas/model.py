from pydantic import BaseModel

from app.core.constants import AitaLabel


class ModelPayload(BaseModel):
    text: str


class ModelPrediction(BaseModel):
    prediction: AitaLabel
