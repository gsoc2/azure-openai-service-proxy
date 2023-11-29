""" Test completions with azure openai """

# See documentation at https://gloveboxes.github.io/azure-openai-service-proxy/category/developer-endpoints/

import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

OPENAI_ENDPOINT_URL = os.environ.get("OPENAI_ENDPOINT_URL")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
API_VERSION = "2023-09-01-preview"
MODEL_NAME = "davinci-002"


client = AzureOpenAI(
    azure_endpoint=OPENAI_ENDPOINT_URL,
    api_key=OPENAI_API_KEY,
    api_version=API_VERSION,
)

response = client.completions.create(
    model=MODEL_NAME, prompt="write a 50 word poem about elephants", max_tokens=512
)

print(response)
