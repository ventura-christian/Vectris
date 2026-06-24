# PROJECT_STATE

Last Updated: June 23, 2026

## Current Phase

System Design

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

In Progress:

- None

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

1. Create SQLAlchemy models (app/models/)
2. Set up Alembic migrations
3. Design and build API endpoints
4. Build backend service layer
5. Build frontend templates
