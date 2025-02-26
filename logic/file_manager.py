import os
import re
import csv
from config.settings import settings
from datetime import datetime

def get_code_files():
    """讀取本地端 leetcode_solutions 內的程式碼文件"""
    code_files = {}
    for file in os.listdir(settings.DATA_FOLDER):
        match = re.match(r"leetcode_(\d+)\.(\w+)", file)
        if match:
            question_id = int(match.group(1))
            lang = match.group(2)
            with open(f"{settings.DATA_FOLDER}/{file}", "r", encoding="utf-8") as f:
                code_files[question_id] = {"code": f.read(), "lang": lang}
    return code_files


def save_to_csv(results):
    """將提交結果存入 CSV"""
    csv_filename = f"leetcode_submissions_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    csv_filepath = f"./{csv_filename}"
    
    with open(csv_filepath, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["題號", "題目", "結果", "錯誤訊息"])  # 寫入標頭
        writer.writerows(results)  # 寫入資料
    
    print(f"✅ 提交結果已儲存至 {csv_filename}")
    return csv_filename
