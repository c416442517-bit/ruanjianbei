from fastapi import APIRouter, HTTPException
from app.schemas import CrisisRequest, CrisisResult
from app.services.llm import chat_completion, parse_json
from app.services.prompts import CRISIS_SYSTEM, CRISIS_KEYWORDS
from app.config import settings

router = APIRouter()


@router.post("/crisis", response_model=CrisisResult)
def detect_crisis(req: CrisisRequest):
    if not settings.llm_api_key:
        raise HTTPException(500, "未配置 LLM_API_KEY，请在 backend/config/.env 中填入")

    text = req.text
    hit_kw = any(k in text for k in CRISIS_KEYWORDS)
    data = parse_json(chat_completion(CRISIS_SYSTEM, text, 0.1))
    risk_level = data.get("risk_level", "low")
    need_referral = bool(data.get("need_referral", False))
    if hit_kw:
        risk_level = "high"
        need_referral = True
    return CrisisResult(
        risk_level=risk_level,
        reason=data.get("reason", ""),
        need_referral=need_referral,
        hit_keyword=hit_kw,
    )
