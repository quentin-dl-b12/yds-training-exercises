"""
helpers.py — Shared utilities for the hands-on exercise.

Provides:
  - DocumentStore: in-memory document database mock
  - send_reset_email: email sending mock
  - logger: pre-configured logger instance

Do not modify this file during the exercise.
"""

import logging

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger("practical")


# ---------------------------------------------------------------------------
# Document store — in-memory database mock
# ---------------------------------------------------------------------------

class DocumentStore:
    """
    Simple in-memory document store that mimics a NoSQL / document database.

    Documents are stored as plain dicts. Each document is identified by a
    string key (e.g. the user's email address or a UUID).

    Example document shape for a user:
        {
            "email": "alice@example.com",
            "password_hash": "<hashed value>",
            "reset_token": "<token or None>",
        }

    Usage:
        db = DocumentStore()
        db.set("alice@example.com", {"email": "alice@example.com", ...})
        user = db.get("alice@example.com")
        db.delete("alice@example.com")
        exists = db.exists("alice@example.com")
        all_docs = db.all()
    """

    def __init__(self):
        self._store: dict[str, dict] = {}

    def get(self, key: str) -> dict | None:
        """Return the document for *key*, or None if not found."""
        return self._store.get(key)

    def set(self, key: str, document: dict) -> None:
        """Insert or replace the document at *key*."""
        self._store[key] = document

    def delete(self, key: str) -> None:
        """Remove the document at *key*. No-op if not found."""
        self._store.pop(key, None)

    def exists(self, key: str) -> bool:
        """Return True if a document exists at *key*."""
        return key in self._store

    def all(self) -> dict[str, dict]:
        """Return a shallow copy of all documents."""
        return dict(self._store)


# Shared database instance — import this in app.py
db = DocumentStore()

# ---------------------------------------------------------------------------
# Email mock
# ---------------------------------------------------------------------------

def send_reset_email(address: str, token: str) -> None:
    """
    Mock sending a password reset email to *address*.

    In production this would dispatch an email containing a link of the form:
        https://app.example.com/reset-password?token=<token>

    For the purposes of this exercise the function is not implemented.

    Args:
        address: The recipient's email address.
        token:   The password reset token to include in the link.
    """
    # In a real app this would send an email containing a reset link.
    # For the exercise, the token is printed to stdout so you can copy it
    # into the POST /reset-password/confirm request body.
    print(f"[MOCK EMAIL] Password reset email sent to {address} — reset token: {token}.")
