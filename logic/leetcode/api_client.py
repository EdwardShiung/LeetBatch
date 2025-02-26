import json
import os
from pathlib import Path
from playwright.async_api import async_playwright, Browser, BrowserContext, Page
from logic.leetcode.login_manager import load_cookies, login_leetcode

COOKIES_FILE: Path = Path("cookies.json")

class LeetCodeBrowser:
    """ LeetCode 自動化瀏覽器管理 """

    def __init__(self, headless: bool = True) -> None:
        """ 初始化 Playwright 瀏覽器 """
        self.headless: bool = headless
        self.browser: Browser | None = None
        self.context: BrowserContext | None = None
        self.page: Page | None = None

    async def launch(self) -> Page:
        """ 啟動瀏覽器，並嘗試載入 Cookies """
        playwright = await async_playwright().start()
        self.browser = await playwright.chromium.launch(headless=self.headless)
        self.context = await self.browser.new_context()
        self.page = await self.context.new_page()

        # 嘗試載入 Cookies（避免每次都重新登入）
        if COOKIES_FILE.exists():
            await load_cookies(self.page)
        else:
            print(" 找不到 Cookies，進行登入...")
            await login_leetcode(self.page)

        return self.page

    async def close(self) -> None:
        """ 關閉瀏覽器 """
        if self.browser:
            await self.browser.close()
            print("瀏覽器已關閉")

