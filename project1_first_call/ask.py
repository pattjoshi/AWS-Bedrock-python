import sys
import boto3

MODEL_ID = "anthropic.claude-3-5-haiku-20241022-v1:0"


def ask(prompt: str) -> str:
    client = boto3.client("bedrock-runtime", region_name="us-east-1")
    response = client.converse(
        modelId=MODEL_ID,
        messages=[{"role": "user", "content": [{"text": prompt}]}],
    )
    return response["output"]["message"]["content"][0]["text"]


if __name__ == "__main__":
    prompt = " ".join(sys.argv[1:]) or "Say hello in one sentence."
    print(ask(prompt))
