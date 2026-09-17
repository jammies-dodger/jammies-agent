import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI

parser = argparse.ArgumentParser(description="jammies ai agent chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()

## load env vars
load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
prompt_mode = str.lower(os.environ.get("PROMPT_MODE"))

def runPrompt():
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

    response = client.chat.completions.create(
        model="openrouter/free",
        messages= [
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    )

    if response.usage is None: raise RuntimeError('response.usage is None, api request likely failed')

    # Track token usage
    prompt_tokens = response.usage.prompt_tokens
    completion_tokens = response.usage.completion_tokens
    print(f"Prompt tokens: {prompt_tokens}\nResponse tokens: {completion_tokens}")


    print(response.choices[0].message.content)


runPrompt()