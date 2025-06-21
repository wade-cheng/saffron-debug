"""A dead simple logging and debugging library.

This library is written in pure python. Feel free to use your IDE to jump to
and read the source code!
"""

import os
from collections.abc import Callable

__all__ = [
    "ENABLED",
    "dprint",
    "dprint_thunk",
]

ENABLED = os.environ.get("SAFFRON_DEBUG_ENABLED", "False") == "True"
"""Whether not saffron-debug is enabled.

This is whether the environment variable `SAFFRON_DEBUG_ENABLED` is `True`. 
This variable is set in saffron-debug's `__init__.py`, so it is read on program start
(or whenever saffron-debug is imported), not every debug print call.
"""

def dprint(s) -> None:
    """Print `s` if and only if saffron-debug is enabled."""
    if ENABLED:
        print(s)

def dprint_thunk(t: Callable[[], str]) -> None:
    """Print `t()` if and only if saffron-debug is enabled.
    
    A thunk is any function with type `Callable[[], Any]`. They can be used to 
    suspend execution such that code is only run when it is needed. For example, 
    `t = lambda: expensive_computation()` is a thunk, and the computation is only
    run when `t` is called (via `t()`).

    For the purposes of printing, we require this thunk to output something printable,
    not `Any`.

    # Examples

    A toy example:

    ```
    import time
    def expensive() -> str:
        time.sleep(2)
        return "result of computation was 42."
        
    sdbg.dprint_thunk(lambda: expensive())
    ```
    """
    if ENABLED:
        print(t())