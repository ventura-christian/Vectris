# LEARNING STATE

Last Updated: June 22, 2026

---

Understood:

- Project scoping and MVP thinking
- Systems analysis and workflow-first design
- Layered architecture fundamentals
- Relational schema design — tables, columns, types, constraints
- Primary keys and foreign keys
- Junction tables and why they exist
- Derived values vs stored values
- Column naming conventions
- Nullable vs required fields
- Status lifecycle modeling
- Why business logic belongs in the service layer
- Monolithic vs microservices architecture and why monolith fits Vectris
- Separation of concerns and the four system layers
- The dependency direction rule (layers only call downward)
- HTTP request-response cycle
- Server-side rendering vs client-side rendering
- What Jinja2 is and how it integrates with FastAPI
- What an ORM is and why SQLAlchemy exists
- What database migrations are and why Alembic is needed
- FastAPI vs Flask vs Django tradeoffs
- PostgreSQL vs MySQL vs SQLite vs MongoDB tradeoffs

Partially Understood:

- Database normalization
- REST API design
- Translating a schema into Python model classes

Not Learned Yet:

- SQLAlchemy
- Alembic migrations
- FastAPI dependency injection
- Database sessions
- Service layer implementation
- Pydantic validation models
- Testing

Current Learning Objective:

- Write the first SQLAlchemy model: app/models/transport_request.py
- Understand how SQLAlchemy models map to the schema defined in entities.md
