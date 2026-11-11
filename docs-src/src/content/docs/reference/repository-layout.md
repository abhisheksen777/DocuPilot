---
title: Repository Layout
description: High-level map of the DocuPilot codebase.
---

## Main directories

- `src/docupilot/server` — FastAPI entrypoint, static UI, and HTTP routes
- `src/docupilot/workers` — Celery app and background tasks
- `src/docupilot/domain` — core domain models and invariants
- `src/docupilot/application` — use cases and provider interfaces
- `src/docupilot/adapters` — provider implementations for LLM, OCR, search, and storage
- `src/docupilot/infrastructure` — config and external integrations
- `src/docupilot/events` — internal event contracts
- `tests` — unit and integration tests
- `tools` — maintenance scripts for migrations, repairs, reindexing, and smoke checks
- `docs-src` — Starlight docs source
- `website/docs` — generated static docs output
- `website` — standalone marketing site

## Storage layout

Uploaded files and processed artifacts live under the local object-store layout when running locally. Blob references are stored as relative object-store keys so the repository does not depend on machine-specific absolute paths.

## User model

DocuPilot requires authenticated users. Guest access is disabled.

- `POST /users` creates a user
- `POST /users/login` sets the `docupilot_session` cookie
- document endpoints require a valid `docupilot_session` cookie
