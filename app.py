# app.py
import os
import logging

# 各モジュールのテスト用関数をインポート
from modules.weather_events.weather_fetcher import test_module as test_weather
from modules.weather_events.events_fetcher import test_module as test_events
from modules.recruitment.job_fetcher import test_module as test_jobs
from modules.news.news_fetcher import test_module as test_news
from modules.auto_reply.reply_handler import test_module as test_auto_reply
from modules.status.slack_status import test_module as test_slack_status
from modules.status.metalife_status import test_module as test_metalife_status

# 共通ユーティリティからSlack投稿関数をインポート
from modules.utils.slack_utils import post_to_slack

# Slack テストチャンネルID（環境変数から取得）
SLACK_TEST_CHANNEL =["C08BRQGQ2VB"]

def main():
    logging.basicConfig(level=logging.INFO)
    messages = []

    # 朝の投稿内容（例）
    messages.append("【朝の投稿】")
    messages.append("天気情報: " + test_weather())
    messages.append("地元イベント: " + test_events())
    messages.append("データサイエンス求人情報: " + test_jobs())

    # 1時間ごとの投稿内容（例）
    messages.append("\n【1時間ごとの投稿】")
    messages.append("利用規約とボット利用方法: " + test_auto_reply())
    messages.append("Slackログイン状況: " + test_slack_status())
    messages.append("Metalifeログイン状況: " + test_metalife_status())

    # 夕方の投稿内容（例）
    messages.append("\n【夕方の投稿】")
    messages.append("日本のニュース: " + test_news())

    full_message = "\n".join(messages)
    logging.info("Slackに投稿するメッセージ:\n%s", full_message)

    # Slackへの投稿処理
    post_to_slack(full_message, SLACK_TEST_CHANNEL)
    logging.info("全ての投稿がSlackテストチャンネルに送信されました。")

if __name__ == "__main__":
    main()
