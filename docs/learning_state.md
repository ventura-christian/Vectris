# LEARNING STATE

Last Updated: June 24, 2026

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
- PostgreSQL installation and service management on macOS
- Creating a PostgreSQL database from the terminal
- What PATH is and why tools need to be on it
- What pip is and how it differs from pip3 outside a virtual environment
- What a virtual environment is and why it isolates project dependencies
- What .gitignore is and how Git uses it to exclude files
- ACID guarantees and why they matter in a hospital context
- SQLAlchemy Declarative Base pattern and how Python classes map to tables
- Alembic migration workflow — init, autogenerate, upgrade, version tracking
- FastAPI dependency injection using Depends()
- FastAPI type hint validation and 422 error responses
- Async versus sync in FastAPI at a conceptual level
- The difference between SQLAlchemy models and Pydantic schemas
- Which fields to exclude from a Pydantic input schema and why

Partially Understood:

- Database normalization
- REST API design
- Translating a schema into Python model classes
- Pydantic — needs deeper review at start of next session

Not Learned Yet:

- SQLAlchemy
- Alembic migrations
- FastAPI dependency injection
- Database sessions
- Service layer implementation
- Pydantic validation models
- Testing

Current Learning Objective:

- Write app/database/session.py — understand SQLAlchemy engine, session factory, and Base before writing any model
