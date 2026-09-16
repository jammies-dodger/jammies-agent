import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if api_key is None: raise RuntimeError('OPENROUTER_API_KEY could not be loaded from .env file')

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)

response = client.chat.completions.create(
    model="openrouter/free",
    messages= [
        {
            "role": "user",
            "content": "Write a very short open ended story max 3 sentences."
        }
    ]
)

if response.usage is None: raise RuntimeError('response.usage is None, api request likely failed')

# Track token usage
prompt_tokens = response.usage.prompt_tokens
completion_tokens = response.usage.completion_tokens
print(f"Prompt tokens: {prompt_tokens}\nResponse tokens: {completion_tokens}")


print(response.choices[0].message.content)