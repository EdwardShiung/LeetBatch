from fastapi import APIRouter, HTTPException
import asyncio
import random
import csv
from datetime import datetime
from playwright.async_api import async_playwright
from logic.leetcode.submit_manager import submit_code
from logic.file_manager import get_code_files, save_to_csv
from config.settings import settings
from db.data_mappings import QUESTION_MAPPING



router = APIRouter()

"""API 端點：提交單一 LeetCode 題目"""
@router.get("/submit/{question_id}")
async def submit_question(question_id: int):

    code_files = get_code_files()
    if question_id not in code_files:
        raise HTTPException(status_code=404, detail="題目未找到")
    
    async with async_playwright() as playwright:
        result = await submit_code(playwright, question_id, code_files[question_id]["code"], code_files[question_id]["lang"])
    
    save_to_csv(result)
    return {"question_id": question_id, "result": result}


""" 依序提交所有題目，並儲存結果到 CSV 檔案 """
@router.get("/submit_multi_questions")
async def submit_multi_questions():
    
    code_files = get_code_files()
    results = []
    
    async with async_playwright() as playwright:
        for question_id, question_title in QUESTION_MAPPING.items():
            if question_id in code_files:
                print(f"🚀 正在提交題目 {question_id}: {question_title}")
                await asyncio.sleep(random.randint(5, 10))  # 避免提交過快
                result = await submit_code(playwright, question_id, code_files[question_id]["code"], code_files[question_id]["lang"])
            else:
                result = {"status": "No solution file found."}
                
            # 處理錯誤訊息
            if "\n" in result:
                status, error_message = result.split("\n", 1)
            else:
                status, error_message = result, ""

            # 存入結果
            results.append([question_id, question_title, status, error_message])
    
    csv_file = save_to_csv(results)
    
    return {"message": "Submission completed.", "csv_file": csv_file, "submission_results": results}
