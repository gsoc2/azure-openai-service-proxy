""" Test OpenAI Embeddings API """

# See documentation at https://gloveboxes.github.io/azure-openai-service-proxy/category/developer-endpoints/

import os
from openai import OpenAI

OPENAI_ENDPOINT_URL = os.environ.get("OPENAI_ENDPOINT_URL")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_EMBEDDING_ENGINE = "text-embedding-ada-002"

client = OpenAI(
    base_url=OPENAI_ENDPOINT_URL,
    api_key=OPENAI_API_KEY,
)


content = (
    "This stunning leather wrap bracelet will add a touch of bohemian flair "
    "to your outfit."
    "The bracelet features a braided leather band in a rich brown color, "
    "adorned with turquoise beads and silver charms. "
    "The bracelet wraps around your wrist multiple times, creating a layered look that "
    "is eye-catching and stylish. "
    "The bracelet is adjustable and has a button closure for a secure fit. "
    "This leather wrap bracelet is the perfect accessory for any occasion, "
    "whether you want to dress up a casual outfit or add some color to a formal one."
)


query_embeddings = client.embeddings.create(
    model=OPENAI_EMBEDDING_ENGINE, input=str(content), encoding_format="float"
)

# print(query_embeddings.model_dump_json(indent=2))
print(query_embeddings.data[0].embedding)
