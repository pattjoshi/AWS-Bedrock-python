"""Central configuration — the only place env vars are read."""

import os

AWS_REGION = os.environ.get("AWS_REGION", "us-east-1")

# Model IDs used across the course projects. Verify current availability with:
#   aws bedrock list-foundation-models --region us-east-1 \
#     --query "modelSummaries[?contains(modelId, 'claude')].modelId" --output table
CLAUDE_HAIKU_MODEL_ID = "anthropic.claude-haiku-5-5"
CLAUDE_SONNET_MODEL_ID = "anthropic.claude-sonnet-5-5"

DEFAULT_MODEL_ID = os.environ.get("BEDROCK_MODEL_ID", CLAUDE_HAIKU_MODEL_ID)
