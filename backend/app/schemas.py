from __future__ import annotations
from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
    user_id: str | None = None


class ChatResponse(BaseModel):
    reply: str
    emotion: str
    intensity: float
    risk_level: str
    need_referral: bool
    hit_keyword: bool


class EmotionRequest(BaseModel):
    text: str


class EmotionResult(BaseModel):
    emotion: str
    intensity: float
    valence: str


class CrisisRequest(BaseModel):
    text: str


class CrisisResult(BaseModel):
    risk_level: str
    reason: str
    need_referral: bool
    hit_keyword: bool
