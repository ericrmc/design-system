"""Subprocess coverage shim.

When `COVERAGE_PROCESS_START` is set in the environment, Python interpreters
that import this module (because the directory containing it is on PYTHONPATH)
will start a coverage tracer at startup and write a per-process .coverage.*
data file. conftest.py prepends this directory to PYTHONPATH for CLI subprocess
calls when tests are run under `pytest --cov`.
"""
import os

if os.environ.get("COVERAGE_PROCESS_START"):
    try:
        import coverage
        coverage.process_startup()
    except ImportError:
        pass
