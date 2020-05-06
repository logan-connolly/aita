from fastapi import APIRouter
from starlette.requests import Request

from app.schemas.model import ModelPayload, ModelPrediction
from app.services.model import AITAClassifier


router = APIRouter()


@router.post("/predict", response_model=ModelPrediction, status_code=200)
def predict_class(request: Request, payload: ModelPayload) -> ModelPrediction:
    model: AITAClassifier = request.app.state.model
    prediction: ModelPrediction = model.predict(payload)

    return prediction
