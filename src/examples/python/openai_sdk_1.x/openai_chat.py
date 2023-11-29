""" Test script for OpenAI chat API """

# See documentation at https://gloveboxes.github.io/azure-openai-service-proxy/category/developer-endpoints/

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_ENDPOINT_URL = os.environ.get("OPENAI_ENDPOINT_URL")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
MODEL_NAME = "text-davinci-002"

MESSAGES = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {
        "role": "assistant",
        "content": "The Los Angeles Dodgers won the World Series in 2020.",
    },
    {"role": "user", "content": "Where was it played?"},
]

client = OpenAI(
    base_url=OPENAI_ENDPOINT_URL,
    api_key=OPENAI_API_KEY,
)


completion = client.chat.completions.create(
    model=MODEL_NAME, messages=MESSAGES  # e.g. gpt-35-instant
)

print(completion.model_dump_json(indent=2))
print()
print(completion.choices[0].message.content)
