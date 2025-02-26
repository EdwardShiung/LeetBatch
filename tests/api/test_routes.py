import pytest
from httpx import AsyncClient
from presentation.main import app

@pytest.mark.asyncio
async def test_submit_single_question():
    """ 測試提交單一 LeetCode 題目 API """

    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/submit/1")

    assert response.status_code == 200, f" API 回應錯誤: {response.status_code}"
    json_data = response.json()

    assert "question_id" in json_data, " 回應 JSON 缺少 'question_id'"
    assert "question" in json_data, " 回應 JSON 缺少 'question'"
    assert "result" in json_data, " 回應 JSON 缺少 'result'"

    print(f" 單題提交 API 測試通過！結果: {json_data}")


@pytest.mark.asyncio
async def test_submit_multi_questions():
    """ 測試批量提交 LeetCode 題目 API """

    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/submit_multi")

    assert response.status_code == 200, f" API 回應錯誤: {response.status_code}"
    json_data = response.json()

    assert "message" in json_data and json_data["message"] == "Submission completed.", "❌ 批量提交 API 回應異常"
    assert "csv_file" in json_data, " 回應 JSON 缺少 'csv_file'"
    assert "submission_results" in json_data, " 回應 JSON 缺少 'submission_results'"
    assert isinstance(json_data["submission_results"], list), " submission_results 應為列表"

    print(f"批量提交 API 測試通過！結果: {json_data}")
