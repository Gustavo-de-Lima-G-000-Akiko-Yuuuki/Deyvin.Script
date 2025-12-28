#!/usr/bin/env python3
"""Entry point script for the DeyvinScript interpreter.

This module simply proxies to :func:`deyvin.interpreter.cli` in order to
provide a convenient executable when the package is installed or run
directly from the repository.  After installation from PyPI the
console script ``deyvin`` will be available and you can run your
DeyvinScript files like this::

    deyvin path/to/script.deyvin

If you are running from a source checkout you can execute the module
directly for development purposes::

    python deyvin_script.py path/to/script.deyvin

Both forms accept the ``-v`` flag for verbose logging.
"""

from __future__ import annotations

from deyvin.interpreter import cli


def main() -> int:
    """Run the command‑line interface and return the exit code."""
    return cli()


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
