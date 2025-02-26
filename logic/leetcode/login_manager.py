import json
from playwright.async_api import Page
from config.settings import settings


async def login_leetcode(page: Page):
    """自動登入 LeetCode 並儲存 cookies"""
    await page.goto("https://leetcode.com/accounts/login/")
    await page.fill("#id_login", settings.LEETCODE_USERNAME)
    await page.fill("#id_password", settings.LEETCODE_PASSWORD)
    await page.click("button[type='submit']")
    
    # 等待登入完成
    await page.wait_for_timeout(5000)
    cookies = await page.context.cookies()
    
    with open("cookies.json", "w") as f:
        json.dump(cookies, f)
    print("✅ 登入成功，Cookies 已儲存！")