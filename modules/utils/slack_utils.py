import os
import requests

def post_to_slack(message, channel):
#    SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN", "").strip()
#    if not SLACK_BOT_TOKEN:
#        print("Error: SLACK_BOT_TOKEN is not set")
#        return

    # デバッグ用: トークンの先頭と末尾数文字を表示（※本番では削除してください）
    print("DEBUG: channel =", channel[:10] + "..." + channel[-10:])

    url = "https://slack.com/api/chat.postMessage"
    headers = {
        "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "channel": channel,
        "text": message
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200 and response.json().get("ok"):
        print("✅ メッセージがSlackに投稿されました。")
    else:
        print("⚠️ 投稿エラー:", response.text)
