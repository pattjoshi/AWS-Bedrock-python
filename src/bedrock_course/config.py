"""Central configuration — the only place env vars are read."""

import os

AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")

# Model IDs used across the course projects.
CLAUDE_HAIKU_MODEL_ID = "anthropic.claude-3-5-haiku-20241022-v1:0"
CLAUDE_SONNET_MODEL_ID = "anthropic.claude-3-5-sonnet-20241022-v2:0"

DEFAULT_MODEL_ID = os.environ.get("BEDROCK_MODEL_ID", CLAUDE_HAIKU_MODEL_ID)
