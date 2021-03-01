from fastapi import APIRouter
from starlette.requests import Request
from starlette.status import HTTP_200_OK

from app.schemas.model import ModelPayload, ModelPrediction
from app.services.model import AITAClassifier

router = APIRouter()


@router.post("/", response_model=ModelPrediction, status_code=HTTP_200_OK)
def predict_class(request: Request, payload: ModelPayload) -> ModelPrediction:
    """Predict AITA class based on input text from ModelPayload"""
    model: AITAClassifier = request.app.state.model
    prediction: ModelPrediction = model.predict(payload)
    return prediction
