# Smart Notes — AI-Powered Notes App

A template app ready to deploy on [Embr](https://portal.embrdev.io). FastAPI backend serves a plain HTML/JS frontend on a single port — no frontend build step needed.

## Deploy to Embr

This repo includes a [`build.yaml`](build.yaml) that tells Embr how to build and run the app:

```yaml
version: 1
platform: python
platformVersion: "3.14"
run:
  port: 8080
```

Connect this repo in the [Embr Portal](https://portal.embrdev.io), and Embr will install dependencies from `requirements.txt`, then start the server automatically.

## Run Locally

```bash
pip install -r requirements.txt
PORT=8008 uvicorn backend.app:app --reload --port ${PORT}
```

Open http://localhost:8008

## Features

- **CRUD notes** — create, edit, delete
- **AI actions** — summarize, extract action items, sentiment analysis (mock by default)
- **Optional AI** — set `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_API_KEY`, and `AZURE_OPENAI_DEPLOYMENT` env vars, then uncomment the real implementation in `backend/ai_service.py`
- **Optional DB** — in-memory storage by default; swap `backend/store.py` for SQLite/Postgres
