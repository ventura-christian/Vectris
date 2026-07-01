# LEARNING STATE

> Last Updated: July 1, 2026

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
- SQLAlchemy models — writing Python classes that map to database tables
- Alembic migrations — init, autogenerate, upgrade workflow
- Database sessions — engine, SessionLocal, Base pattern
- Pydantic — schemas vs SQLAlchemy models, input/output separation, which fields to exclude
- FastAPI dependency injection using Depends() and the get_db() generator pattern
- Pydantic input vs output schema separation and why both are needed
- Service layer implementation — separating business logic from API handlers
- Resource management with Python generators (yield + finally)
- SQLAlchemy session lifecycle — add, commit, refresh
- State machine enforcement in the service layer
- State diagrams and why they catch invalid status transitions before code does
- Entity relationship diagrams using Mermaid syntax
- Checking a UI mockup against an already-decided schema instead of building straight from the mockup
- Deriving a second UI signal (delayed) from the same time-based pattern used for priority
- A service function that reaches into more than one table in a single operation

Partially Understood:

- Database normalization
- REST API design
- Translating a schema into Python model classes

Not Learned Yet:

- Testing

Current Learning Objective:

- Write the transporter API endpoints, then update the dashboard templates to match the corrected wireframe