import os
from google import genai
from app.config import Config  # Configから設定を取得
import logging
from datetime import datetime

# Gemini API キーを設定
GEMINI_API_KEY = Config.GEMINI_API[0] if Config.GEMINI_API else os.getenv("GEMINI_API", "")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API key が設定されていません。")

# Gemini クライアントの初期化
client = genai.Client(api_key=GEMINI_API_KEY)

def get_local_events(location="秋葉原", days=1):
    """
    Gemini 2.0のGoogle検索機能を使って、指定された場所の今後のイベント情報を取得する
    
    Parameters:
    location (str): イベントを検索する場所（デフォルト: 東京）
    days (int): 今日から何日分のイベントを検索するか（デフォルト: 7）
    
    Returns:
    str: 整形されたイベント情報
    """
    try:
        # 現在の日付を取得
        current_date = datetime.now().strftime("%Y年%m月%d日")
        
        # Gemini 2.0にイベント情報を問い合わせるプロンプト
        prompt = f"""現在（{current_date}）から今後{days}日間の{location}で開催される主要なイベントについて検索し、以下の形式で回答してください:

        【探すイベントの種類】
        - 技術カンファレンス
        - 文化イベント
        - フェスティバル
        - 展示会
        - コンサート
        - その他の注目イベント

        各イベントについて、以下の情報を含めてください:
        1. イベント名
        2. 開催日時
        3. 開催場所
        4. 簡単な説明（1-2文）
        
        最大5つの興味深いイベントを選び、箇条書きで回答してください。検索結果に基づいて最新の情報を提供してください。
        """
        
        # Gemini 2.0で回答を生成（検索機能を使用）
        response = client.models.generate_content(
            model="gemini-2.0-flash",  # gemini-2.0シリーズを使用
            contents=prompt,
        )
        
        if response.text:
            # 応答の先頭に場所情報を追加
            return f"【{location}の今後{days}日間のイベント情報】\n{response.text.strip()}"
        else:
            return f"{location}のイベント情報を取得できませんでした。"
            
    except Exception as e:
        logging.error(f"イベント情報の取得中にエラーが発生しました: {e}")
        return f"{location}のイベント情報の取得中にエラーが発生しました。しばらくしてからもう一度お試しください。"

def test_module():
    """
    モジュールのテスト関数
    東京のイベント情報を取得して返します
    """
    return get_local_events()

if __name__ == "__main__":
    # コマンドラインからの実行時のテスト用
    print(test_module())
