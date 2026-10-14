# AWS Bedrock — Project-Based Learning

A hands-on course: each `projects/` folder under `src/bedrock_course/projects/`
is a standalone mini-project building toward a full GenAI application on
AWS Bedrock. See `PLAN.md` for the full roadmap and progress.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -e .            # installs bedrock_course as an importable package

aws configure                # one-time, if not already done
cp .env.example .env         # optional overrides (region, model id)
```

## Run Project 1

```bash
python -m bedrock_course.projects.project1_first_call.cli "What is Amazon Bedrock?"
```

## Run tests

```bash
pytest
```

## Structure

```
src/bedrock_course/
├── config.py              # env/config loading
├── clients.py              # boto3 client factory
└── projects/
    └── project1_first_call/
        ├── cli.py           # entrypoint
        └── service.py       # logic
```

## Rules

- Max 250 lines per file.
- One responsibility per module (CLI vs. logic separated).
- No hardcoded secrets — use `.env` / AWS CLI credentials.
- Tests mock AWS calls; no live calls in the test suite.
