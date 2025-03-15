# app/routes.py
from flask import Flask, jsonify
import logging

# 朝の投稿用モジュール
from modules.weather_events.weather_fetcher import test_module as test_weather
from modules.weather_events.events_fetcher import test_module as test_events
from modules.recruitment.job_fetcher import test_module as test_jobs

# 定時（1時間ごと）の投稿用モジュール
from modules.auto_reply.reply_handler import test_module as test_auto_reply
from modules.status.slack_status import test_module as test_slack_status
from modules.status.metalife_status import test_module as test_metalife_status

# 夕方の投稿用モジュール
from modules.news.news_fetcher import test_module as test_news

# 共通の Slack 投稿関数
from modules.utils.slack_utils import post_to_slack

# configからチャンネル情報などの設定を読み込み
from app.config import Config

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/post_morning", methods=["POST"])
def post_morning():
    messages = []
    messages.append("【朝の投稿】")
    messages.append("天気情報: " + test_weather())
    messages.append("地元イベント: " + test_events())
    messages.append("データサイエンス求人情報: " + test_jobs())
    full_message = "\n".join(messages)
    logging.info("朝の投稿メッセージ:\n%s", full_message)
    
    # configから複数のチャンネルを取得
    channels = Config.SLACK_TEST_CHANNELS
    post_to_slack(full_message, channels)
    logging.info("朝の投稿がSlackに送信されました。")
    return jsonify({"status": "success", "message": "Morning post sent."})

@app.route("/post_hourly", methods=["POST"])
def post_hourly():
    messages = []
    messages.append("【1時間ごとの投稿】")
    messages.append("利用規約とボット利用方法: " + test_auto_reply())
    messages.append("Slackログイン状況: " + test_slack_status())
    messages.append("Metalifeログイン状況: " + test_metalife_status())
    full_message = "\n".join(messages)
    logging.info("1時間ごとの投稿メッセージ:\n%s", full_message)
    
    channels = Config.SLACK_TEST_CHANNELS
    post_to_slack(full_message, channels)
    logging.info("1時間ごとの投稿がSlackに送信されました。")
    return jsonify({"status": "success", "message": "Hourly post sent."})

@app.route("/post_evening", methods=["POST"])
def post_evening():
    messages = []
    messages.append("【夕方の投稿】")
    messages.append("日本のニュース: " + test_news())
    full_message = "\n".join(messages)
    logging.info("夕方の投稿メッセージ:\n%s", full_message)
    
    channels = Config.SLACK_TEST_CHANNELS
    post_to_slack(full_message, channels)
    logging.info("夕方の投稿がSlackに送信されました。")
    return jsonify({"status": "success", "message": "Evening post sent."})