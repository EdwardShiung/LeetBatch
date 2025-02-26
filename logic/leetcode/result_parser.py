import asyncio
from playwright.async_api import Page

async def get_submission_result(page: Page) -> str:
    """ 讀取 LeetCode 提交結果 """

    try:
        # **等待結果出現**
        await page.wait_for_selector('span[data-e2e-locator="console-result"]', timeout=10000)
        result_text: str = await page.text_content('span[data-e2e-locator="console-result"]')
        result_text = result_text.strip() if result_text else "Unknown Result"
        print(f" 提交結果：{result_text}")

        # **嘗試抓取詳細錯誤訊息**
        error_details: str = "No details available"
        try:
            await page.wait_for_selector('div.font-menlo.whitespace-pre-wrap.break-all.text-xs.text-red-60.dark\\:text-red-60', timeout=5000)
            error_details = await page.text_content('div.font-menlo.whitespace-pre-wrap.break-all.text-xs.text-red-60.dark\\:text-red-60')
            error_details = error_details.strip() if error_details else "No details available"
        except:
            pass

        # **如果是 Accepted，抓取執行時間 & 記憶體**
        if "Accepted" in result_text:
            try:
                await page.wait_for_selector('div[data-e2e-locator="submission-runtime"]', timeout=5000)
                runtime = await page.text_content('div[data-e2e-locator="submission-runtime"]')
                runtime = runtime.strip() if runtime else "N/A"

                await page.wait_for_selector('div[data-e2e-locator="submission-memory"]', timeout=5000)
                memory = await page.text_content('div[data-e2e-locator="submission-memory"]')
                memory = memory.strip() if memory else "N/A"

                print(f" 執行時間: {runtime}, 記憶體使用: {memory}")
                return f"{result_text} | Runtime: {runtime}, Memory: {memory}"
            except:
                return f"{result_text} | Execution details not found"

        return f"{result_text} | Error Details: {error_details}"

    except:
        print(" 無法讀取提交結果！")
        return "Failed to retrieve result."
