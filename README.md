# Project Foundation: Learn Django + DRF Through Building an Enterprise-Grade Application

## Purpose

This repository is not only a software project. It is a structured learning environment to build a deep understanding of how professional Django + Django REST Framework applications are designed, structured, and maintained.

The primary goal is not to maximize development speed. AI coding tools can already generate working code. The goal is to understand **why the code exists, where responsibilities belong, and how a scalable backend system is designed**.

The project should simulate how an experienced engineering team would build a production system.

---

# Why this project exists

The developer currently works as a Fullstack AI Engineer in a professional environment using:

* Django
* Django REST Framework
* React
* PostgreSQL
* Celery
* Redis
* Kubernetes
* Azure
* AI integrations
* Multiple external integrations (CRM systems, Shopify, etc.)

AI coding assistants make it possible to implement features quickly, but understanding the architecture behind the generated code is the limiting factor.

This project exists to close that gap.

The objective is to develop the mental model required to look at an enterprise Django codebase and immediately understand:

* How requests flow through the system
* Why files are structured the way they are
* Where business logic belongs
* How APIs are designed
* How integrations are handled
* How authentication and multi-tenancy work
* How production systems stay maintainable

---

# Core learning philosophy

Do not build a tutorial project.

Do not blindly copy patterns.

Every component should answer:

1. What problem does this solve?
2. Why does Django provide this feature?
3. Why would an enterprise team structure it this way?
4. What are the alternatives?
5. What are the tradeoffs?

The goal is architectural understanding.

---

# Future application vision

The long-term application idea is an **Attention Analytics Platform**.

The concept:

A system that can collect user attention data and provide analytics.

Potential capabilities:

* Webcam-based eye tracking
* Gaze estimation
* Screen coordinate mapping
* Calibration
* Attention heatmaps
* User interaction analytics
* Experiment creation and management

However, the eye tracking system is NOT the starting point.

The eye tracking engine will eventually be treated as an external integration/service.

The first priority is building the professional backend foundation.

---

# Architectural approach

The system should be designed like a real SaaS product.

High-level architecture:

```
React Frontend

↓

Django REST Framework API

↓

Views / API Layer

↓

Service Layer

↓

Models / ORM

↓

PostgreSQL Database

↓

External Integrations
    - Eye Tracking Engine
    - AI Models
    - External APIs
```

---

# Development philosophy

Build from first principles.

Do not immediately hide complexity behind abstractions.

The learning order should be:

## Phase 1: Django fundamentals

Understand:

* Django project structure
* manage.py
* settings
* URLs
* applications
* request lifecycle

The goal:

Understand how Django starts and how a request moves through the framework.

---

## Phase 2: Database layer

Learn:

* Models
* ORM
* Migrations
* Relationships
* Querying

Understand:

```
Python object

↓

Django Model

↓

Migration

↓

SQL

↓

Database
```

---

## Phase 3: API development

Learn:

* Serializers
* APIViews
* URL routing
* Request validation
* Responses

Understand:

```
HTTP Request

↓

URL

↓

View

↓

Serializer

↓

Business Logic

↓

Database

↓

Response
```

Start with explicit APIViews before introducing ViewSets and routers.

The goal is understanding before convenience.

---

## Phase 4: Business logic architecture

Introduce:

* Service layer
* Separation of concerns
* Testing strategy

Preferred flow:

```
View

↓

Service

↓

ORM
```

Views should handle HTTP concerns.

Services should contain business logic.

---

## Phase 5: Production concepts

Add:

* Authentication
* Authorization
* Organizations
* Multi-tenancy
* Background workers
* Logging
* Monitoring
* Testing
* CI/CD

The final system should resemble a professional SaaS backend.

---

# AI Agent Instructions

This repository will use AI coding assistants extensively.

Agents must behave like senior engineers mentoring a developer.

The priority order is:

1. Understanding
2. Correct architecture
3. Maintainability
4. Implementation speed

Before implementing significant changes, agents should explain:

* The design
* The affected components
* The data flow
* Why this approach is chosen

Avoid:

* Generating large amounts of code without explanation
* Introducing unnecessary abstractions
* Copying patterns without understanding
* Optimizing prematurely

Prefer:

* Simple explicit solutions
* Clear architecture
* Small incremental commits
* Explaining tradeoffs

---

# Cursor and Claude Code configuration

Create and maintain:

```
.cursor/
    rules/
        django-guidelines.mdc
        engineering-principles.mdc
        code-review.mdc
        testing-guidelines.mdc

PROJECT_CONTEXT.md

ARCHITECTURE.md

DECISIONS.md

LESSONS.md
```

Purpose:

## engineering-principles.mdc

Defines AI behavior and engineering principles.

## PROJECT_CONTEXT.md

Explains:

* What is being built
* Why it exists
* Current goals

## ARCHITECTURE.md

Documents:

* System design
* Components
* Data flows

## DECISIONS.md

Records important architectural decisions:

Example:

```
Decision:
Use service layer for business logic.

Reason:
Keeps views simple and improves testing.

Alternative:
Business logic inside views.

Rejected because:
Creates large unmaintainable views.
```

## LESSONS.md

Documents learning outcomes:

Examples:

* Django concepts
* Architectural patterns
* Important discoveries

---

# Definition of success

This project is successful when the developer can:

* Open an unfamiliar Django repository and understand its structure
* Explain the request lifecycle
* Understand the purpose of models, serializers, views, services, and tasks
* Design new features before coding
* Build integrations cleanly
* Understand multi-tenant SaaS architecture
* Use AI coding tools without blindly trusting generated code

The final product matters.

The deeper goal is becoming a stronger engineer.
