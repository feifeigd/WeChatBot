# AGENTS.md

## Project overview
- Single-file Python project: `main.py` is the only entrypoint.
- Managed by **uv**. Python 3.12 (`.python-version`).
- Dependencies: `openai` (DeepSeek API), `wxauto4` (WeChat automation, Windows-only).

## Commands
```bash
uv run main.py        # run the bot
uv add <package>      # add a dependency
uv sync               # install / sync dependencies
```

## Environment
- DeepSeek API key is read from env var `DeepSeek` (not `OPENAI_API_KEY`). Set it before running.

## Architecture notes
- `WeChatBot.__init__` creates an OpenAI client pointed at `https://api.deepseek.com` with model `deepseek-v4-flash`.
- `WeChatBot.__ask` enables DeepSeek reasoning mode (`reasoning_effort="high"` + `extra_body={"thinking": {"type": "enabled"}}`). Keep these params when editing the LLM call.
- `wxauto4` WeChat integration code is commented out in `main.py` — the bot currently only tests the LLM call and does not interact with WeChat.
- `wxauto4` is Windows-only; do not assume this runs on Linux/macOS.
- VS Code debug config (`.vscode/launch.json`) launches `main.py` via `debugpy`.

## Conventions
- No lint, typecheck, test, or CI is configured yet. Do not invent tooling without being asked.
