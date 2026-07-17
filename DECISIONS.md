# Architecture Decisions


## ADR-001: Project purpose

Date:
18-07-2026


Decision:

Build a reusable Django enterprise template before building application features.


Reason:

Understanding architecture is the primary goal.

Using AI without understanding generated code creates knowledge gaps.


Alternative considered:

Immediately building the eye tracking application.


Rejected because:

Too many unknown layers would be introduced simultaneously.

## ADR-002: Dependency management with uv

Decision:

Use uv for Python dependency management.

Reason:

Modern, fast, reproducible dependency management with lock files.

Alternative considered:

pip + requirements.txt.

Rejected because:

uv provides a cleaner workflow for modern Python projects.