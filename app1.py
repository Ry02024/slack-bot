# app.py
import os
import logging
import datetime
from zoneinfo import ZoneInfo  # Python 3.9以降

from modules.weather_events.weather_fetcher import test_module as test_weather
from modules.weather_events.events_fetcher import test_module as test_events
from modules.recruitment.job_fetcher import test_module as test_jobs
from modules.news.news_fetcher import test_module as test_news
from modules.auto_reply.reply_handler import test_module as test_auto_reply
from modules.status.slack_status import test_module as test_slack_status
from modules.status.metalife_status import test_module as test_metalife_status
from modules.utils.slack_utils import post_to_slack

SLACK_TEST_CHANNEL = ["C08BRQGQ2VB"]

def safe_get(label, content):
    """
    指定したモジュールの出力が空の場合は「情報なし」と返す。
    ラベルとともに出力する。
    """
    content = content.strip()
    if not content:
        return f"{label}: 情報なし"
    return f"{label}: {content}"
    
def post_morning():
    messages = []
    messages.append("【朝の投稿】")
    messages.append("天気情報: " + test_weather())
    messages.append("地元イベント: " + test_events())
    messages.append("データサイエンス求人情報: " + test_jobs())
    return "\n".join(messages)

def post_hourly():
    messages = []
    messages.append("【1時間ごとの投稿】")
    messages.append("利用規約とボット利用方法: " + test_auto_reply())
    messages.append("Slackログイン状況: " + test_slack_status())
    messages.append("Metalifeログイン状況: " + test_metalife_status())
    return "\n".join(messages)

def post_evening():
    messages = []
    messages.append("【夕方の投稿】")
    messages.append("日本のニュース: " + test_news())
    return "\n".join(messages)

def main():
    logging.basicConfig(level=logging.INFO)
    # 現在時刻を日本時間で取得
    now = datetime.datetime.now(ZoneInfo("Asia/Tokyo"))
    logging.info("Current Japan time: %s", now.strftime("%Y-%m-%d %H:%M:%S"))
    
    # 平日（月～金）の場合の処理
    if now.weekday() < 5:
        if now.hour == 9:
            full_message = post_morning()
        elif now.hour == 17:
            full_message = post_evening()
        else:
            full_message = post_hourly()
    else:
        full_message = "休日のため投稿は行いません。"

    # 万が一、全体が空の場合はフォールバックメッセージを設定
    if not full_message.strip():
        full_message = "投稿情報がありません。"

    # ログに出力して、どの情報が投稿されるか確認できるようにする
    logging.info("Slackに投稿するメッセージ:\n%s", full_message)
    post_to_slack(full_message, SLACK_TEST_CHANNEL)
    logging.info("投稿がSlackテストチャンネルに送信されました。")

if __name__ == "__main__":
    main()
