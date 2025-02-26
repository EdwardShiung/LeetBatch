import json
import random
import asyncio
from playwright.async_api import Playwright
from logic.leetcode.login_manager import login_leetcode
from logic.leetcode.language_manager import set_language
from logic.leetcode.result_parser import get_submission_result
from config.settings import settings
from db.data_mappings import QUESTION_MAPPING, LANG_MAPPING


async def submit_code(playwright: Playwright, question_id: int, code: str, lang: str):
    """自動提交 LeetCode 題目"""
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    
    # 嘗試載入 Cookies
    try:
        with open("cookies.json", "r") as f:
            cookies = json.load(f)
        await context.add_cookies(cookies)
    except:
        print("⚠️ Cookies 不存在或無效，重新登入...")
        page = await context.new_page()
        await login_leetcode(page)
        await page.close()
    
    page = await context.new_page()
    url = f"https://leetcode.com/problems/{QUESTION_MAPPING[question_id]}/"
    await page.goto(url)
    await page.wait_for_timeout(5000)
    
    # 設定語言
    await set_language(page, LANG_MAPPING.get(lang, "python3"))
    
    # 確保 Monaco Editor 載入
    await page.wait_for_timeout(2000)
    await page.wait_for_selector(".monaco-editor", timeout=15000)
    
    # 填入程式碼
    await page.evaluate('(code) => monaco.editor.getModels()[0].setValue(code)', code)
    print("✅ 成功填入程式碼！")
    
    await page.wait_for_timeout(2000)  # 等待語言切換完成
    
    # 等待提交按鈕
    await page.wait_for_selector("button[data-e2e-locator='console-submit-button']", timeout=10000)
    await page.click("button[data-e2e-locator='console-submit-button']", force=True)
    print("✅ 提交成功！")
    
    # 隨機延遲，降低機器人偵測風險
    await page.wait_for_timeout(random.randint(5000, 15000))
    
    # 讀取提交結果
    result = await get_submission_result(page)
    
    await page.wait_for_timeout(2000)
    await browser.close()
    return result
