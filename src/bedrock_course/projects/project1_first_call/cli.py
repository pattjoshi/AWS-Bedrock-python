"""Entrypoint for Project 1 — parses args and prints the result."""

import sys

from bedrock_course.projects.project1_first_call.service import ask_bedrock


def main() -> None:
    prompt = " ".join(sys.argv[1:]) or "Say hello in one sentence."
    print(ask_bedrock(prompt))


if __name__ == "__main__":
    main()
