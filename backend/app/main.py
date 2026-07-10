from fastapi import FastAPI
from app.routers import chat, emotion, crisis
from app.config import settings

app = FastAPI(
    title="大学生心理健康智能关爱平台",
    description="基于情感计算与自然语言交互的心理疏导 Agent",
    version="0.1.0",
)

app.include_router(chat.router, tags=["疏导对话"])
app.include_router(emotion.router, tags=["情绪识别"])
app.include_router(crisis.router, tags=["危机预警"])


@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "大学生心理健康智能关爱平台",
        "docs": "/docs",
        "model": settings.llm_model,
    }


@app.get("/health")
def health():
    return {"status": "healthy", "llm_configured": bool(settings.llm_api_key)}
