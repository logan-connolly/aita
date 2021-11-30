from fastapi import APIRouter
from starlette.requests import Request
from starlette.status import HTTP_200_OK

from app.core.services.predict import AitaPredictor
from app.schemas.model import ModelPayload, ModelPrediction

router = APIRouter()


@router.post("/", response_model=ModelPrediction, status_code=HTTP_200_OK)
def predict_class(request: Request, payload: ModelPayload) -> ModelPrediction:
    """Predict AITA class based on input text from ModelPayload"""
    model: AitaPredictor = request.app.state.model
    return model.predict(payload)
