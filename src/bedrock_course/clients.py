"""Single factory for boto3 clients used across the course."""

from functools import lru_cache

import boto3

from bedrock_course.config import AWS_REGION


@lru_cache(maxsize=1)
def get_bedrock_runtime_client():
    """Return a cached boto3 client for invoking Bedrock models."""
    return boto3.client("bedrock-runtime", region_name=AWS_REGION)
