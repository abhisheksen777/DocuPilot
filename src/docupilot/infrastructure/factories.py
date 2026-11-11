from docupilot.application.interfaces import DocumentRepository, LLMProvider
from docupilot.infrastructure.config import Settings
from docupilot.infrastructure.repositories.in_memory_document_repository import (
    InMemoryDocumentRepository,
)
from docupilot.infrastructure.repositories.postgres_document_repository import (
    PostgresDocumentRepository,
)


def build_document_repository(settings: Settings) -> DocumentRepository:
    if settings.repository_backend.lower() == "postgres":
        return PostgresDocumentRepository(settings.postgres_url)
    return InMemoryDocumentRepository()


def build_llm_provider(settings: Settings) -> LLMProvider | None:
    del settings
    return None
