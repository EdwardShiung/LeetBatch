import pytest
import asyncio
from logic.leetcode.api_client import LeetCodeBrowser
from logic.leetcode.submit_manager import submit_code
from logic.leetcode.result_parser import get_submission_result

@pytest.mark.asyncio
async def test_submission_result():
    """ 測試 LeetCode 提交結果解析 """

    browser = LeetCodeBrowser(headless=True)
    page = await browser.launch()

    question_slug = "two-sum"
    sample_code = "class Solution:\n    def twoSum(self, nums, target):\n        for i in range(len(nums)):\n            for j in range(i+1, len(nums)):\n                if nums[i] + nums[j] == target:\n                    return [i, j]"

    await submit_code(page, question_slug, sample_code, "py")
    result = await get_submission_result(page)

    assert result is not None, " 未能取得提交結果！"
    print(f"LeetCode 提交結果解析測試通過！結果: {result}")

    await browser.close()
