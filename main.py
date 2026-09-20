import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI

from prompts import system_prompt

parser = argparse.ArgumentParser(description="jammies ai agent chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

## load env vars
load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
prompt_mode = str.lower(os.environ.get("PROMPT_MODE"))

def generate_content():
    if prompt_mode == "disable" or prompt_mode == "disabled":
        print(f"---prompt skipped---")
        return

    if api_key is None: raise RuntimeError('OPENROUTER_API_KEY could not be loaded from .env file')

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )

    user_prompt = args.user_prompt

    if user_prompt is None or len(user_prompt) == 0: raise TypeError('Missing prompt')

    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ]


    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        temperature=0
    )



    if response.usage is None: raise RuntimeError('response.usage is None, api request likely failed')

    # Track token usage

    if args.verbose:
        prompt_tokens = response.usage.prompt_tokens
        completion_tokens = response.usage.completion_tokens
        model = response.model
        print(f"Model: {model}")
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}\nResponse tokens: {completion_tokens}")

    print(response.choices[0].message.content)

generate_content()