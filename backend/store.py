"""In-memory note storage.

Drop-in replacement target: swap this module for a DB-backed version
(e.g. SQLAlchemy + SQLite/Postgres) without changing the API layer.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional

from backend.models import NoteCreate, NoteRecord, NoteUpdate


class NoteStore:
    def __init__(self) -> None:
        self._notes: dict[str, NoteRecord] = {}

    def create(self, data: NoteCreate) -> NoteRecord:
        rec = NoteRecord(title=data.title, content=data.content)
        self._notes[rec.id] = rec
        return rec

    def list_all(self) -> list[NoteRecord]:
        return sorted(self._notes.values(), key=lambda n: n.created_at, reverse=True)

    def get(self, note_id: str) -> Optional[NoteRecord]:
        return self._notes.get(note_id)

    def update(self, note_id: str, data: NoteUpdate) -> Optional[NoteRecord]:
        rec = self._notes.get(note_id)
        if rec is None:
            return None
        if data.title is not None:
            rec.title = data.title
        if data.content is not None:
            rec.content = data.content
        rec.updated_at = datetime.now(timezone.utc).isoformat()
        return rec

    def delete(self, note_id: str) -> bool:
        return self._notes.pop(note_id, None) is not None


# Singleton used by the API
note_store = NoteStore()
