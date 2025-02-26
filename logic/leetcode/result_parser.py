from playwright.async_api import Page

async def get_submission_result(page: Page):
    """ 讀取 LeetCode 提交結果（基於最新 HTML） """
    try:
        # **嘗試抓取錯誤類型（Compile Error, Runtime Error, etc.）**
        await page.wait_for_selector('span[data-e2e-locator="console-result"]', timeout=5000)
        error_type = await page.text_content('span[data-e2e-locator="console-result"]')
        error_type = error_type.strip() if error_type else "Unknown Error"
        print(f"✅ 錯誤類型：{error_type}")

        # **嘗試抓取詳細錯誤訊息**
        try:
            await page.wait_for_selector('div.font-menlo.whitespace-pre-wrap.break-all.text-xs.text-red-60.dark\:text-red-60', timeout=5000)
            error_details = await page.text_content('div.font-menlo.whitespace-pre-wrap.break-all.text-xs.text-red-60.dark\:text-red-60')
            error_details = error_details.strip() if error_details else "No details available"
        except:
            error_details = "No details available"

        print(f"✅ 詳細錯誤訊息：{error_details}")

        # **回傳完整錯誤資訊**
        return f"{error_type}\n{error_details}"

    except:
        print("❌ 無法讀取提交結果！")
        return "Failed to retrieve result."