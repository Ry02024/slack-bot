import os
from google import genai

def generate_text(context):
    """
    Gemini API を利用して、指定されたコンテキストに基づく文章を生成する関数。
    GEMINI_API キーは環境変数 "GEMINI_API" から取得します。
    """
    gemini_api_key = os.getenv("GEMINI_API")
    if not gemini_api_key:
        return "GEMINI_API key が設定されていません。"
    
    # Gemini の API キーを設定
    genai.configure(api_key=gemini_api_key)
    
    # プロンプトの作成（用途に応じて調整してください）
    prompt = f"以下の内容に関する情報を元に、ユーザーに分かりやすい文章を生成してください:\n{context}"
    
    # 文章生成のリクエスト
    response = genai.models.generate_content(
        model="gemini-2.0-flash",  # ご利用のモデルに合わせて調整
        contents=prompt,
    )
    
    if response.text:
        return response.text.strip()
    else:
        return "適切な文章を生成できませんでした。"

if __name__ == "__main__":
    sample_context = "利用規約とボット利用方法に関する概要"
    generated = generate_text(sample_context)
    print("生成された文章:", generated)
