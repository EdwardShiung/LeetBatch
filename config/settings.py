import os 
from dotenv import load_dotenv

# Read .env file
load_dotenv()

class Settings:
    """設定管理，從.env 讀取環境變數"""
    LEETCODE_USERNAME: str = os.getenv("LEETCODE_USERNAME")
    LEETCODE_PASSWORD: str = os.getenv("LEETCODE_PASSWORD")
    
    # 確保這些變數有值，否則拋出錯誤
    if not LEETCODE_USERNAME or not LEETCODE_PASSWORD:
        raise ValueError("🔔 環境變數 LEETCODE_USERNAME 或 LEETCODE_PASSWORD 未設置！")
    
# 創建全域
settings = Settings()