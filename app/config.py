import os
from dotenv import load_dotenv

# .env ファイルがある場合、環境変数を読み込む
load_dotenv()

class Config:
    # Slack 関連の設定
    SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN", "").split()
    SLACK_TEST_CHANNEL = ["C08BRQGQ2VB"]
    
    # Gemini API の設定
    GEMINI_API = os.getenv("GEMINI_API", "").split()
