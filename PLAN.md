# AWS Bedrock Learning Course — Plan

Project-based path to learn AWS Bedrock with Python, following production-style
folder structure and coding conventions (max 250 lines/file, single
responsibility per module, no hardcoded secrets).

## Phase 0 — Account & environment setup
- [x] Create AWS account
- [x] Create IAM user (`bedrock-dev`) with Bedrock access
- [x] Create access keys, configure AWS CLI (`aws configure`)
- [x] Verify Bedrock model access (auto-enabled; no manual step needed)

## Phase 1 — Repo scaffolding (done)
- [x] Create `src/bedrock_course/` package layout
- [x] Add `config.py` — central env/config loading (region, model IDs)
- [x] Add `clients.py` — single boto3 client factory
- [x] Add `.env.example` and `.gitignore` (exclude `.env`, `__pycache__`, etc.)
- [x] Add shared `requirements.txt`
- [x] Add `README.md` with setup + run instructions
- [x] Restructure Project 1 into `src/bedrock_course/projects/project1_first_call/`
  - `cli.py` — argument parsing / entrypoint only
  - `service.py` — `ask_bedrock()` logic
- [x] Add `tests/test_project1.py` with mocked boto3 call (passing)
- [x] Remove old flat `project1_first_call/ask.py`
- [x] Commit + push

## Phase 2 — Project 1: First Bedrock call
- [ ] Run `python -m bedrock_course.projects.project1_first_call.cli "..."` locally, confirm real response from Claude
- [ ] Understand `converse()` request/response shape

## Phase 3 — Project 2: Terminal chatbot with memory
- [ ] Multi-turn conversation loop, history list
- [ ] Streaming responses (`converse_stream`)

## Phase 4 — Project 3: RAG over your own documents
- [ ] Upload docs to S3
- [ ] Decide: Bedrock Knowledge Bases + OpenSearch Serverless (small cost)
      vs. local FAISS (free) — pending your choice
- [ ] Build retrieval + answer pipeline with citations

## Phase 5 — Project 4: Agent with tool use
- [ ] Define a custom action (Lambda function)
- [ ] Bedrock Agent wired to call it via function calling

## Phase 6 — Project 5 (optional): Wrap as an API
- [ ] FastAPI service exposing `/ask`

## Phase 7 — Observability & guardrails (cross-cutting, add once core projects work)
- [ ] CloudWatch logging
- [ ] Bedrock Guardrails basic policy

---
**Coding rules in force for this repo:**
1. Max 250 lines per file — split by responsibility if exceeded.
2. One responsibility per module (CLI vs service/logic separated).
3. No hardcoded secrets — env vars via `.env` (gitignored) + `config.py`.
4. Type hints on all functions; docstrings only where non-obvious.
5. Thin entrypoints, testable business logic.
6. Tests use mocked AWS calls — no real API calls in test suite.
7. `snake_case` for files/functions, `PascalCase` for classes.
8. Single shared `requirements.txt`, pinned versions.
9. follow proper branching and git commit message. create development, main branch, each phase create pulll request to development. 
