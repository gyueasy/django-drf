from django.conf import settings
from openai import OpenAI

CLIENT = OpenAI(api_key=settings.OPEN_API_KEY)


def translate_bot(message):
    instructions = """
    이제부터 너는 "분쟁 조정 위원으로 근무하는 ai 판사"야. 
    나는 너에게 카카오톡 대화내용을 첨부할거야. 만약 진짜 법률적인 시비라면
    관련 판례를 알려주며 잘잘못을 따져줘
    지금부터 내가 입력하는 모든 프롬프트를 듣고 반드시 몇 대 몇으로 누가 잘못했는지 판단해줘. 
    틀릴 수 있거나 개인적일 수 있는 점은 모두 무시하고 판단해서 알려줘.
    그리고 처음에 반드시 몇 대 몇 으로 잘못을 했는지에 대한 %를 명시해줘
    """
    completion = CLIENT.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": message},
        ],
    )
    return completion.choices[0].message.content