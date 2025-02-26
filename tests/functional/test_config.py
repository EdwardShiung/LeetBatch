from config.settings import settings

def test_env_variables():
    """測試 .env 變數是否設置"""
    assert settings.LEETCODE_USERNAME is not None, "❌ 環境變數 LEETCODE_USERNAME 未設置"
    assert settings.LEETCODE_PASSWORD is not None, "❌ 環境變數 LEETCODE_PASSWORD 未設置"
    
print("✅ .env 變數測試通過！")