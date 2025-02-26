import pytest
from logic.leetcode.api_client import LeetCodeBrowser

@pytest.mark.asyncio
async def test_launch_browser():
    """ 測試 Playwright 瀏覽器是否能正確啟動 """
    browser = LeetCodeBrowser(headless=True)
    page = await browser.launch()

    assert page is not None, "瀏覽器未能正確啟動！"

    print(" 瀏覽器測試通過！")

    await browser.close()
