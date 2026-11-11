from fastapi import HTTPException, status

from docupilot.application.interfaces import DocumentStore
from docupilot.application.services.documents import get_document
from docupilot.domain.models import Document, User


def get_owned_document_or_404(
    *,
    document_id: str,
    repository: DocumentStore,
    current_user: User,
) -> Document:
    document = get_document(document_id=document_id, repository=repository)
    if document is None or document.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found",
        )
    return document
