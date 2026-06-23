# Vectris Software Architecture Decisions & Explanations

## Architecture Type

Why monolithic architecture for Vectris?

- I only have one codebase and one deployable unit.
- All of my data  relationships(transport_requests, transporters, and request_assignments) heavily rely on each other and keeping all my code in one codebase simplifies my deployment.
- I have myself (one dev), three workflows, a timeline, and a transport team with a handful of users.
- I decided not to separated my codebase using microservices to avoid issues when debugging, simplify deployment, and because I am not taking this product to scale.
- I didn't want to hassle with tons of services, technologies, and attempting to get 5 services running in tandem. I felt this was not only overkill but could create problems that I didn't have otherwise.

## System Layers

I want to enforce the separation of concerns (each part of my application should have one job and know as little as possible about everything else). This will make my codebase easier to debug when something goes ary.

***Database Layer***

- This is where my data lives permanently.
- PostgreSQL is a running process that stores rows in tables on disk.
- Its only job is to store data reliably and retrieve data accurately.

***Business Logic Layer (Service Layer)***

There is one rule for this layer: ***if it's a business rule, it lives in the service layer, not the API***

- This is where decisions happen.
- I don't want to have to write multiple versions of the same code. If I need my API endpoint or my HTTP request to change and update, then I'd essentially be making more of a mess for myself if a bug occurs and I have the same code written twice or in different locations.

***API Layer***

The API layer (app/api/)has a narrow job: to receive input, validate that it's shaped correctly, call the right service, and return the result.

It should not be making business decisions. It should not be writing SQL (structured query language).

It is a thin translation layer between the outside world and the Vectris internals.

***Frontend Layer***

This layer lives in (frontend/) and is the part the dispatcher sees and interacts with.

- These are the Jinja2 templates that contain HTML files with Python variables injected into them.
- The frontend depends on the the API to provide it with data.
- It doesn't apply business rules.
- It asks the API for data and displays it.

***The Direction Rule***

I will apply this rule so that the information and dependencies only flow downward, never upwards.

Each layer will never understand the layer above it and that is what will make Vectris powerful, easy to debug if issues arise, and allow me to adjust tech if I need to without having to rewrite entire sections of the codebase that relies on whatever I may change.

## Technology Stack

***Python***

This is the language I will write Vectris in.

The reasons behind this decision:

- Large ecosystem of libraries
- A robust feature set
- Has nice performance characteristics
- Excellent data manipulation
- Readable syntax that prioritizes clarity
- Strong web framework ecosystem

***FastAPI vs Flask vs Django

Why not Flask?

- It's a microframework that provides routing and request handling but none of the other robust features that Django and FastAPI offer.
- I would have to incorporate all of the other tech I will need (database integration, templating, validation) from third party libraries.
- I would have to make all structural decisions myself and there are better options that provide me those features baked in.

Why no Django?

- I felt this framework makes too many decisions and comes packed with an ORM (object relational mapping), an admin panel, a templating engine, authentication, a migration system and much more.
- unfortunately, for my application and needs, this was overkill and was largely unnecessary for my design choice.

Why FastAPI?

- It's modern, high performance and designed around Python's type annotation system.
- I get automatic data validation with Pydantic, automatic API documentation with Swagger UI, async support by default, and a clean dependency injection system.
- It's specifically designed for building APIs which is exactly the tech I need for my project.
- I also want to use Jinja2 and vectris can be served both JSON endpoints and HTML pages with FastAPI in a clean and structured fashion.
- It is also the fastest between Flask and Django and the type annotation system will help me catch errors earlier.
- I also liked the automatic documentation feature to help with my presentation.

## Data Flow - How a Transport Request Moves Through the System

## Frontend Architecture

## Database Architecture

## What This System Does Not Do (By Design)
