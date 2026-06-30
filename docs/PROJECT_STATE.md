# PROJECT_STATE

Last Updated: June 29, 2026

## Current Phase

API Layer

## Project Summary

Vectris is a hospital patient transport operations platform focused on:

1. Creating transport requests
2. Assigning transport requests
3. Tracking request completion

## MVP Scope

Included:

- Request creation
- Assignment workflow
- Status Tracking
- Dispatcher dashboard
- Database persistence
- REST API

## Current Status

Completed:

- Project scope
- User identification
- Workflow analysis
- MVP definition
- Technology direction
- Workflow stated defined (active, in_progress, complete)
- Entities identified (transport_requests, transporters, request_assignment)
- Data model fields defined
- Junction table pattern decided for multi-transporter support
- System design complete
- architecture.md documented (all 7 sections)
- Frontend technology direction decided (Jinja2 server-side templates)
- decisions.md updated with frontend technology decision
- PostgreSQL installed, running, and added to PATH
- Vectris database created
- completed_at column added to transport_requests schema
- Python virtual environment created and activated
- .gitignore created
- requirements.txt populated and all dependencies installed
- .env file created with database connection URL
- Database connection verified through virtual environment
- SQLAlchemy models written for all three entities
- Alembic initialized and first migration applied
- All three tables verified in PostgreSQL
- Pydantic schemas written for transport requests and transporters
- main.py created — FastAPI app boots and serves /docs
- get_db() dependency injection added to session.py
- transport_request_service.py written — create and status update

In Progress:

- API Layer

Not Started:

- Database implementation
- API implementation
- Frontend implementation
- Deployment

## Technology Direction

Backend:

- Python
- FastAPI

Database:

- PostgreSQL

Frontend:

- Jinja2 server-side templates (rendered by FastAPI)

Architecture:

- Monolithic application

## Current Risks

- Scope creep
- Learning curve
- Limited timeline
- Overthinking/over estimating my abilities

## Next Actions

1. Write transporter_service.py
2. Write assignment_service.py
3. Write API endpoints (transport_requests, transporters, assignments)
4. Build dispatcher dashboard
