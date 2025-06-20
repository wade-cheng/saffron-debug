import os
from collections.abc import Callable

__all__ = [
    "ENABLED",
    "dprint",
    "dprint_thunk",
]

ENABLED = os.environ.get("SAFFRON_DEBUG_ENABLED", "False") == "True"

def dprint(s) -> None:
    if ENABLED:
        print(s)

def dprint_thunk(t: Callable[[], str]) -> None:
    if ENABLED:
        print(t())