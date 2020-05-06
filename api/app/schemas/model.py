from pydantic import BaseModel

from .post import LabelEnum


class ModelPayload(BaseModel):
    text: str


class ModelPrediction(BaseModel):
    prediction: LabelEnum
