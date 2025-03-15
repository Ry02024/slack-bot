import os

class Config:
    # Bot Token は環境変数から取得（必須）
    SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN", "").split()
    # チャンネルはカンマ区切りの文字列として環境変数に設定し、リストに変換する
    SLACK_TEST_CHANNELS = ["C08BRQGQ2VB"]