from openai import OpenAI
from api_pjt import config

CLIENT = OpenAI(
    api_key=config.OPENAI_API_KEY,
)


def ask_to_gpt(instructions, message):
    completion = CLIENT.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": instructions,
            },
            {
                "role": "user",
                "content": message,
            },
        ],
    )
    return completion.choices[0].message.content


system_instructions = """

"""

# 처음 인사를 위해
response = ask_to_gpt(system_instructions, "")
print(f"에이든 카페봇 : {response}\n\n")

while True:
    user_message = input("유저 : ")
    if user_message == "종료":
        break
    response = ask_to_gpt(system_instructions, user_message)
    print(f"에이든 카페봇 : {response}\n\n")

