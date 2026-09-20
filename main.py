import json
import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI

from prompts import system_prompt
from call_function import available_functions, call_function

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
        tools=available_functions,
        temperature=0.2,
    )
    if response.usage is None: raise RuntimeError('response.usage is None, api request likely failed')

    if args.verbose:
        prompt_tokens = response.usage.prompt_tokens
        completion_tokens = response.usage.completion_tokens
        model = response.model
        print(f"Model: {model}")
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}\nResponse tokens: {completion_tokens}")


    message = response.choices[0].message
    if message.tool_calls:
        for tool_call in message.tool_calls:
            try:
                function_args = json.loads(tool_call.function.arguments or "{}")
                result_message = call_function(tool_call, args.verbose)
                if len(result_message["content"]) == 0:
                    raise RuntimeError(f"Error: no result content of called function: {tool_call.function.name}({function_args})")
            except Exception as e:
                print(e)
            else:
                if args.verbose: print(f"-> {result_message['content']}")
    else:
        print(message.content)

generate_content()