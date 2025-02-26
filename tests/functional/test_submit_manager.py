import pytest
import asyncio
from logic.leetcode.api_client import LeetCodeBrowser
from logic.leetcode.submit_manager import submit_code

@pytest.mark.asyncio
async def test_submit_code():
    """ 測試 LeetCode 程式碼提交功能 """
    
    browser = LeetCodeBrowser(headless=True)
    page = await browser.launch()

    question_slug = "two-sum"
    sample_code = "class Solution:\n    def twoSum(self, nums, target):\n        for i in range(len(nums)):\n            for j in range(i+1, len(nums)):\n                if nums[i] + nums[j] == target:\n                    return [i, j]"

    result = await submit_code(page, question_slug, sample_code, "py")

    assert result is not None, "未能取得提交結果！"

    print("LeetCode 提交測試通過！")

    await browser.close()
