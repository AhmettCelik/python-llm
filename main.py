import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

prompt = sys.argv[1] if len(sys.argv) > 1 else None
if prompt is None:
    raise ValueError("prompt parameter is missing!")

client = genai.Client(api_key=api_key)
response = client.models.generate_content(model="gemini-2.0-flash-001",
                                          contents=prompt)
print(response.text)
print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
