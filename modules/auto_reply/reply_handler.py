from modules.generative.gemini_generator import generate_text

def test_module():
    # Gemini で生成するためのコンテキスト（用途に応じて変更してください）
    context = "生成AI時代の都市OSについて"
    return generate_text(context)

if __name__ == "__main__":
    print(test_module())
