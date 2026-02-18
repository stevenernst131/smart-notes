"""Entrypoint expected by Oryx/Gunicorn: exposes the FastAPI app as `app`."""

from backend.app import app  # noqa: F401
