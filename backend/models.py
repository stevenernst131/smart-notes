"""Data models for the Smart Notes app.

Uses simple in-memory storage by default. When DB integration is enabled,
swap this out for SQLAlchemy / SQLite models.
"""

from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, Field


# ── Request / Response schemas ───────────────────────────────────────────────

class NoteCreate(BaseModel):
    title: str
    content: str


class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


class NoteOut(BaseModel):
    id: str
    title: str
    content: str
    created_at: str
    updated_at: str


class AIResult(BaseModel):
    note_id: str
    action: str
    result: str


# ── In-memory store (replace with DB later) ──────────────────────────────────

class NoteRecord:
    def __init__(self, title: str, content: str):
        self.id = uuid.uuid4().hex[:12]
        self.title = title
        self.content = content
        now = datetime.now(timezone.utc).isoformat()
        self.created_at = now
        self.updated_at = now

    def to_out(self) -> NoteOut:
        return NoteOut(
            id=self.id,
            title=self.title,
            content=self.content,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
