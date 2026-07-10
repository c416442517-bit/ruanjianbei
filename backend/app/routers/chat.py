from fastapi import APIRouter, HTTPException
from app.schemas import ChatRequest, ChatResponse
from app.services.llm import chat_completion, parse_json
from app.services.prompts import COUNSEL_SYSTEM, EMOTION_SYSTEM, CRISIS_SYSTEM, CRISIS_KEYWORDS
from app.config import settings

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    if not settings.llm_api_key:
        raise HTTPException(500, "未配置 LLM_API_KEY，请在 backend/config/.env 中填入")

    text = req.message

    # 1. 情绪识别
    emotion_data = parse_json(chat_completion(EMOTION_SYSTEM, text, 0.3))
    emotion = emotion_data.get("emotion", "未知")
    try:
        intensity = float(emotion_data.get("intensity", 0.5) or 0.5)
    except (TypeError, ValueError):
        intensity = 0.5

    # 2. 危机预警（关键词快速检测 + 模型判断）
    hit_kw = any(k in text for k in CRISIS_KEYWORDS)
    crisis_data = parse_json(chat_completion(CRISIS_SYSTEM, text, 0.1))
    risk_level = crisis_data.get("risk_level", "low")
    need_referral = bool(crisis_data.get("need_referral", False))
    if hit_kw:
        risk_level = "high"
        need_referral = True

    # 3. 疏导对话
    sys_prompt = COUNSEL_SYSTEM.format(emotion=emotion, intensity=round(intensity, 2))
    reply = chat_completion(sys_prompt, text, 0.7)

    return ChatResponse(
        reply=reply,
        emotion=emotion,
        intensity=round(intensity, 2),
        risk_level=risk_level,
        need_referral=need_referral,
        hit_keyword=hit_kw,
    )
