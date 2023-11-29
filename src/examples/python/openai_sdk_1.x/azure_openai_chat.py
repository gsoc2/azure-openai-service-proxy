""" Test Azure OpenAI Chat Completions API """

# See documentation at https://gloveboxes.github.io/azure-openai-service-proxy/category/developer-endpoints/

import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

OPENAI_ENDPOINT_URL = os.environ.get("OPENAI_ENDPOINT_URL")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
API_VERSION = "2023-09-01-preview"
MODEL_NAME = "text-davinci-002"


client = AzureOpenAI(
    azure_endpoint=OPENAI_ENDPOINT_URL,
    api_key=OPENAI_API_KEY,
    api_version=API_VERSION,
)

MESSAGES = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {
        "role": "assistant",
        "content": "The Los Angeles Dodgers won the World Series in 2020.",
    },
    {"role": "user", "content": "Where was it played?"},
]


completion = client.chat.completions.create(
    model=MODEL_NAME,  # e.g. gpt-35-instant
    messages=MESSAGES,
)

print(completion.model_dump_json(indent=2))
print()
print(completion.choices[0].message.content)
