import os
from dotenv import load_dotenv

# 加載 .env 檔案
load_dotenv()

class Settings:
    LEETCODE_USERNAME: str = os.getenv("LEETCODE_USERNAME")
    LEETCODE_PASSWORD: str = os.getenv("LEETCODE_PASSWORD")
    DATA_FOLDER: str = "db/leetcode_solutions"  # 本地存放程式碼的資料夾
    CSV_FILE: str = "results.csv"  # 儲存結果的 CSV

settings = Settings()