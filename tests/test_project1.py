"""Unit test for Project 1 — mocks boto3, makes no real AWS calls."""

from unittest.mock import MagicMock, patch

from bedrock_course.projects.project1_first_call.service import ask_bedrock


@patch("bedrock_course.clients.boto3.client")
def test_ask_bedrock_returns_model_text(mock_boto_client):
    mock_client = MagicMock()
    mock_client.converse.return_value = {
        "output": {"message": {"content": [{"text": "hello there"}]}}
    }
    mock_boto_client.return_value = mock_client

    from bedrock_course.clients import get_bedrock_runtime_client

    get_bedrock_runtime_client.cache_clear()

    result = ask_bedrock("hi")

    assert result == "hello there"
    mock_client.converse.assert_called_once()
