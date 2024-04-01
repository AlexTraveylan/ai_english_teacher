from typing import Literal, TypedDict

from groq import Groq

from app.settings import GROQ_API_KEY


class MessageAi(TypedDict):
    role: Literal["system", "user", "assistant"]
    content: str


def completion(
    messages: list[MessageAi],
    model: str = "mixtral-8x7b-32768",
    temperature: float = 0.7,
    top_p: float = 1,
) -> str:

    client = Groq(api_key=GROQ_API_KEY)

    chat_completion = client.chat.completions.create(
        messages=messages,
        model=model,
        temperature=temperature,
        top_p=top_p,
    )

    return chat_completion.choices[0].message.content


if __name__ == "__main__":
    mess = [
        MessageAi({"role": "system", "content": "You are a helpful assistant."}),
        MessageAi({"role": "user", "content": "What is the capital of France?"}),
    ]

    response = completion(mess)
    print(response)
