""" dalle-3 example """
import os
import json
from dotenv import load_dotenv

from openai import AzureOpenAI

load_dotenv()

OPENAI_ENDPOINT_URL = os.environ.get("OPENAI_ENDPOINT_URL")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

client = AzureOpenAI(
    azure_endpoint=OPENAI_ENDPOINT_URL,
    api_key=OPENAI_API_KEY,
    api_version="2023-12-01-preview",
)

print("Generating images...")

result = client.images.generate(
    model="dalle3",  # the name of your DALL-E 3 deployment
    prompt="a close-up of a bear walking through the forest",
    n=1,
)

json_response = json.loads(result.model_dump_json())
print(json.dumps(json_response, indent=2))
