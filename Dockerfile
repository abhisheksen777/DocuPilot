FROM python:3.13-slim

LABEL org.opencontainers.image.version="0.10.0" \
      org.opencontainers.image.title="DocuPilot" \
      org.opencontainers.image.description="AI-powered document management and intelligence platform" \
      org.opencontainers.image.source="https://github.com/abhisheksen777/DocuPilot" \
      org.opencontainers.image.licenses="MIT"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends tesseract-ocr poppler-utils \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml README.md LICENSE NOTICE /app/
COPY src /app/src

RUN pip install --upgrade pip \
    && pip install .

RUN useradd --create-home --uid 10001 appuser \
    && mkdir -p /data/object-store \
    && chown -R appuser:appuser /app /data

USER appuser

EXPOSE 8000

CMD ["uvicorn", "docupilot.server.main:app", "--host", "0.0.0.0", "--port", "8000"]
