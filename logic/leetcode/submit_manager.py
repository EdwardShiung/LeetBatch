import asyncio
from playwright.async_api import Page
from logic.leetcode.api_client import LeetCodeBrowser
from logic.leetcode.result_parser import get_submission_result
from config.settings import settings

LANG_MAPPING: dict[str, str] = {
    "py": "python3",
    "java": "java",
    "cpp": "cpp",
    "js": "javascript"
}

async def submit_code(page: Page, question_slug: str, code: str, lang: str) -> str:
    """ 自動提交 LeetCode 程式碼，並回傳結果 """
    
    # 1️. 前往 LeetCode 題目頁面
    url: str = f"https://leetcode.com/problems/{question_slug}/"
    await page.goto(url)
    await page.wait_for_timeout(5000)  # 確保頁面載入完成

    # 2️. 選擇語言
    leetcode_lang: str = LANG_MAPPING.get(lang, "python3")
    await set_language(page, leetcode_lang)

    # 3️. 填入程式碼
    await page.wait_for_selector(".monaco-editor", timeout=10000)
    await page.evaluate('(code) => monaco.editor.getModels()[0].setValue(code)', code)
    print("成功填入程式碼！")

    await asyncio.sleep(2)  # 等待 2 秒，確保編輯器載入完成

    # 4️. 提交程式碼
    await page.wait_for_selector("button[data-e2e-locator='console-submit-button']", timeout=10000)
    await page.click("button[data-e2e-locator='console-submit-button']", force=True)
    print(" 提交成功！")

    # 5️. 讀取提交結果
    result: str = await get_submission_result(page)

    return result

async def set_language(page: Page, lang: str) -> None:
    """ 選擇 LeetCode 的程式語言 """
    try:
        elements = await page.query_selector_all('//button[@aria-haspopup="dialog"]')

        if len(elements) > 2:
            await elements[2].click()
            await asyncio.sleep(2)

            language_option_selector: str = f'//div[contains(@class, "cursor-pointer")][.//div[contains(translate(text(), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "{lang.lower()}")]]'
            await page.wait_for_selector(language_option_selector, timeout=8000)
            await page.click(language_option_selector, force=True)
            print(f" 成功選擇語言: {lang}")

    except Exception as e:
        print(f"⚠️ 語言選擇失敗，可能已預設為 {lang}，錯誤: {e}")
