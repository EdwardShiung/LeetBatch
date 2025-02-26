async def set_language(page, lang):
    try:
        # 1️. 找到所有 `aria-haspopup="dialog"` 按鈕
        elements = await page.query_selector_all('//button[@aria-haspopup="dialog"]')

        for i, element in enumerate(elements):
            text = await element.inner_text()
            print(f"Button {i}: {text}")

        # 2️. 點擊語言選擇按鈕
        if len(elements) > 2:
            print("🔹 正在點擊語言選擇按鈕...")
            await elements[2].click()
            await page.wait_for_timeout(5000)  # 增加等待時間
        else:
            print("⚠️ 找不到語言選擇按鈕！")
            return

        # 3️. 選擇目標語言（忽略大小寫）
        language_option_selector = f'//div[contains(@class, "cursor-pointer")][.//div[contains(translate(text(), "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz"), "{lang.lower()}")]]'
        await page.wait_for_selector(language_option_selector, timeout=8000)
        await page.click(language_option_selector, force=True)

        print(f"✅ 成功選擇語言: {lang}")
    except Exception as e:
        print(f"⚠️ 語言選擇失敗，可能已預設為 {lang}，錯誤: {e}")
