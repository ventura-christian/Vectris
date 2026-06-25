# PROJECT_STATE

Last Updated: June 24, 2026

## Current Phase

Database Design

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

In Progress:

- Database Layer

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

1. Write app/database/session.py
2. Write three SQLAlchemy model files
3. Initialize Alembic and run first migration
4. Verify all three tables exist in PostgreSQL
