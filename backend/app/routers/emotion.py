from fastapi import APIRouter, HTTPException
from app.schemas import EmotionRequest, EmotionResult
from app.services.llm import chat_completion, parse_json
from app.services.prompts import EMOTION_SYSTEM
from app.config import settings

router = APIRouter()


@router.post("/emotion", response_model=EmotionResult)
def detect_emotion(req: EmotionRequest):
    if not settings.llm_api_key:
        raise HTTPException(500, "未配置 LLM_API_KEY，请在 backend/config/.env 中填入")

    data = parse_json(chat_completion(EMOTION_SYSTEM, req.text, 0.3))
    try:
        intensity = float(data.get("intensity", 0.5) or 0.5)
    except (TypeError, ValueError):
        intensity = 0.5
    return EmotionResult(
        emotion=data.get("emotion", "未知"),
        intensity=intensity,
        valence=data.get("valence", "neutral"),
    )
