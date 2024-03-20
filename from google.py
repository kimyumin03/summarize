from google.cloud import translate

# Google Cloud Translation API 클라이언트 생성
client = translate.TranslationServiceClient()

def translate_text(text, target_language):
    # 번역 요청 생성
    parent = client.location_path("[YOUR_PROJECT_ID]", "global")
    response = client.translate_text(
        parent=parent,
        contents=[text],
        target_language_code=target_language,
        mime_type="text/plain"
    )

    # 번역된 텍스트 반환
    translated_text = response.translations[0].translated_text
    return translated_text

# 번역할 텍스트
paper_text = """
논문 내용을 여기에 입력하세요.
"""

# 각 언어로 번역
translated_texts = {
    "en": translate_text(paper_text, "en"),  # 영어로 번역
    "ja": translate_text(paper_text, "ja"),  # 일본어로 번역
    "zh-CN": translate_text(paper_text, "zh-CN"),  # 중국어 간체로 번역
    "ko": translate_text(paper_text, "ko"),  # 한국어로 번역
}

# 번역 결과 출력
for lang, text in translated_texts.items():
    print(f"{lang}: {text}\n")
