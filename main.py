import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if api_key is None: raise RuntimeError('OPENROUTER_API_KEY could not be loaded from .env file')

