import os
from google import genai
from app.config import Config  # Configから設定を取得
import logging

# Gemini API キーを設定
GEMINI_API_KEY = Config.GEMINI_API[0] if Config.GEMINI_API else os.getenv("GEMINI_API", "")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API key が設定されていません。")

# Gemini クライアントの初期化
client = genai.Client(api_key=GEMINI_API_KEY)

def get_weather_info(location="東京"):
    """
    Gemini 2.0のGoogle検索機能を使って、指定された場所の天気情報を取得する
    
    Parameters:
    location (str): 天気を取得したい地域名（デフォルト: 東京）
    
    Returns:
    str: 整形された天気情報
    """
    try:
        # Gemini 2.0に天気情報を問い合わせるプロンプト
        prompt = f"""現在の{location}の天気について検索し、以下の情報を含めて回答してください:
        1. 現在の天気状況（晴れ、雨など）
        2. 現在の気温
        3. 今日の最高気温と最低気温
        4. 降水確率
        5. 明日の天気予報の簡単な概要
        
        情報は簡潔に、箇条書きで回答してください。検索結果に基づいて最新の情報を提供してください。"""
        
        # Gemini 2.0で回答を生成（検索機能を使用）
        response = client.models.generate_content(
            model="gemini-2.0-flash",  # gemini-2.0シリーズを使用
            contents=prompt,
        )
        
        if response.text:
            # 応答の先頭に場所情報を追加
            return f"【{location}の天気情報】\n{response.text.strip()}"
        else:
            return f"{location}の天気情報を取得できませんでした。"
            
    except Exception as e:
        logging.error(f"天気情報の取得中にエラーが発生しました: {e}")
        return f"{location}の天気情報の取得中にエラーが発生しました。しばらくしてからもう一度お試しください。"

def test_module():
    """
    モジュールのテスト関数
    東京の天気情報を取得して返します
    """
    return get_weather_info()

if __name__ == "__main__":
    # コマンドラインからの実行時のテスト用
    print(test_module())
