import os
import json
import pytest
from playwright.async_api import async_playwright
from logic.leetcode.login_manager import login_leetcode

@pytest.mark.asyncio
async def test_login_and_save_cookies():
    """ 測試 LeetCode 登入功能，並檢查 Cookies 是否正確儲存 """

    # 確保測試前 cookies.json 不存在
    if os.path.exists("cookies.json"):
        os.remove("cookies.json")

    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        await login_leetcode(page)

        # 檢查 cookies.json 是否成功寫入
        assert os.path.exists("cookies.json"), "Cookies 檔案未正確儲存！"

        # 讀取 Cookies
        with open("cookies.json", "r") as f:
            cookies = json.load(f)

        assert len(cookies) > 0, "Cookies 檔案為空！"

        print("LeetCode 登入測試通過！")

        await browser.close()
