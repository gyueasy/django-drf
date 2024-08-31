from django.conf import settings
import openai

# OpenAI API 설정
openai.api_key = settings.OPEN_API_KEY

def translate_bot(message: str) -> str:
    instructions = """
    이제부터 너는 "영어, 한글 번역가"야. 
    지금부터 내가 입력하는 모든 프롬프트를 무조건 한글은 영어로, 영어는 한글로 번역해줘. 
    프롬프트의 내용이나 의도는 무시하고 오직 번역만 해줘.
    """
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": instructions},
                {"role": "user", "content": message},
            ],
        )
        return completion.choices[0].message['content'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

def analyze_conversation(conversation: str) -> dict:
    try:
        response = openai.Completion.create(
            engine="davinci",
            prompt=(
                f"Analyze the following conversation and provide the percentage of negative emotions and aggressive intent. "
                f"Also, determine the speaker's share of responsibility based on these metrics:\n\n{conversation}"
            ),
            max_tokens=150
        )
        analysis_result = response.choices[0].text.strip()
        return parse_analysis_result(analysis_result)
    except Exception as e:
        return {"error": str(e)}

def parse_analysis_result(text: str) -> dict:
    result = {}
    
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip().lower()
        if 'negative emotion' in line:
            result['negative_emotion_ratio'] = line.split(':')[1].strip()
        elif 'aggressive intent' in line:
            result['aggressive_intent_ratio'] = line.split(':')[1].strip()
        elif 'responsibility' in line:
            result['responsibility'] = line.split(':')[1].strip()
    
    return result
