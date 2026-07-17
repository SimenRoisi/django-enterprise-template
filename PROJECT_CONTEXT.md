# Project Context

## Purpose

This project exists to learn professional Django + DRF architecture by building a production-style SaaS application.

The goal is not simply to produce working software. The goal is to understand:

- Why components exist
- Where responsibilities belong
- How scalable systems are structured


## Developer Context

The developer is learning Django while working professionally with a Django + DRF based AI SaaS platform.

AI tools are used heavily, but understanding architecture is the priority.


## Current Project Vision

Build an Attention Analytics Platform.

The future system will collect user attention data through integrations such as webcam-based gaze tracking.

The eye tracking system is a future integration, not the initial focus.


## Architecture Principles

Prefer:

- Explicit code before abstractions
- Clear separation of responsibilities
- Small incremental changes
- Understanding before implementation


Core flow:

Request

↓

URL

↓

View

↓

Serializer

↓

Service

↓

Model

↓

Database


## Current Phase

Phase 1:

Learning Django fundamentals.

Focus:

- Project structure
- Applications
- URLs
- Views
- Models
- Migrations
- Request lifecycle