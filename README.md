# 大学生心理健康智能关爱平台

基于情感计算与自然语言交互的心理疏导 Agent，结合匿名倾诉、情绪识别、危机预警和专业转介机制，打造全流程、有温度的心理关爱闭环。

## 功能模块

- **匿名倾诉入口** — 学生端无需注册，降低倾诉门槛
- **情绪识别** — NLP 文本情感分析，输出情绪标签与强度
- **心理疏导 Agent** — 大模型共情对话（倾听 → 共情 → 引导 → 不评判）
- **危机预警** — 关键词表 + 大模型风险判断，自伤/自杀倾向检测
- **专业转介** — 高风险自动生成转介工单，通知校心理中心
- **闭环反馈** — 情绪档案与趋势跟踪，长期关爱

## 技术栈

| 层 | 技术 |
|----|------|
| 前端 | 微信小程序 |
| 后端 | Python + FastAPI |
| 大模型 | 调用 API（疏导对话 / 情绪识别 / 风险判断） |
| 数据库 | MySQL / PostgreSQL（对话记录加密存储） |

## 目录结构

```
软件杯作品/
├── frontend/        # 小程序前端
├── backend/          # FastAPI 后端
│   ├── app/
│   ├── config/       # 配置（密钥放 .env，不进仓库）
│   └── data/mock/    # 示例假数据（真实数据绝不提交）
├── docs/             # 文档与答辩材料
├── .gitignore
└── README.md
```

## 本地开发

```bash
# 后端
cd backend
python -m venv venv
venv/Scripts/activate        # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload

# 前端
cd frontend
# 用微信开发者工具打开该目录
```

## 安全须知

- 真实学生心理健康数据属于敏感隐私，**绝不提交到仓库**，仅用 `data/mock/` 下的假数据
- API Key、数据库密码等放进 `.env`，已被 `.gitignore` 排除
