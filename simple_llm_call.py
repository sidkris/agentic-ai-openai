from langsmith import traceable
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()


client = OpenAI()

@traceable
def test_call(prompt : str):
    response = client.chat.completions.create(
        model = "gpt-4.1-mini",
        messages = [
            {"role" : "user", "content" : prompt}
        ]
    )

    return response.choices[0].message.content

print(test_call("What makes Rust and excellent choice for systems programming?"))