import json
import os
from pathlib import Path
from playwright.async_api import Page
from config.settings import settings

COOKIES_FILE: Path = Path("cookies.json")

async def login_leetcode(page: Page) -> None:
    """ 自動登入 LeetCode 並儲存 Cookies """
    
    # **1️⃣ 打開 LeetCode 登入頁面**
    await page.goto("https://leetcode.com/accounts/login/")
    await page.wait_for_timeout(3000)  # 等待 3 秒確保頁面加載完成

    # **2️⃣ 填寫帳號密碼**
    await page.fill("#id_login", settings.LEETCODE_USERNAME)
    await page.fill("#id_password", settings.LEETCODE_PASSWORD)
    
    # **3️⃣ 點擊登入按鈕**
    await page.click("button[type='submit']")
    await page.wait_for_timeout(5000)  # 等待 5 秒讓 LeetCode 登入成功

    # **4️⃣ 儲存 Cookies**
    cookies: list[dict] = await page.context.cookies()
    COOKIES_FILE.write_text(json.dumps(cookies), encoding="utf-8")

    print("登入成功，Cookies 已儲存！")
    
    
async def load_cookies(page: Page) -> None:
    """ 載入已存儲的 Cookies（如果存在）"""
    if COOKIES_FILE.exists():
        cookies: list[dict] = json.loads(COOKIES_FILE.read_text(encoding="utf-8"))
        await page.context.add_cookies(cookies)
        print(" Cookies 已載入！")
    else:
        print("⚠️ 找不到 Cookies，請先登入！")