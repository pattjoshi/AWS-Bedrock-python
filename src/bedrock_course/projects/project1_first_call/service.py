"""Business logic for Project 1: a single-turn call to Bedrock."""

from bedrock_course.clients import get_bedrock_runtime_client
from bedrock_course.config import DEFAULT_MODEL_ID


def ask_bedrock(prompt: str, model_id: str = DEFAULT_MODEL_ID) -> str:
    """Send one prompt to a Bedrock model and return its text reply."""
    client = get_bedrock_runtime_client()
    response = client.converse(
        modelId=model_id,
        messages=[{"role": "user", "content": [{"text": prompt}]}],
    )
    return response["output"]["message"]["content"][0]["text"]
