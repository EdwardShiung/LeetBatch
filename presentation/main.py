from fastapi import FastAPI
from presentation.api.routes import router

# 初始化 FastAPI 應用
app = FastAPI(
    title="LeetCode Submission API",
    description="提供自動提交 LeetCode 題目的 API",
    version="1.0.0",
    contact={
        "name": "EdwardShiung",
        "email": "edwardshiung@gmail.com",
    }
)

# 註冊 API 路由
app.include_router(router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Welcome to the LeetCode Submission API"}
