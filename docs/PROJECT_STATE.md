# PROJECT_STATE

Last Updated: 18 June, 2026

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

In Progress:

- System design
- Data modeling
- Schema finalization (continue working on destination field structure)

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

- Minimal dashboard UI

Architecture:

- Monolithic application

## Current Risks

- Scope creep
- Learning curve
- Limited timeline
- Overthinking/over estimating my abilities

## Next Actions

1. Resolve destination field: single text field or location + room_number pair
2. Finalize and document full column schema in decisions.md
3. Create database schema (SQL or SQLAlchemy models)
4. Design API endpoints
5. Build backend

## Documentation

| architecture.md |
backlog.md |
diagrams.md |
