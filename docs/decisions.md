# DECISIONS

This file tracks the decisions I made while designing Vectris and why I made them.

Last Updated: June 21, 2026

---

## Column Naming Convention

I originally named variables things like `current_location_of_patient` and `patient_destination_for_current_task`. These are too verbose for database column names and I realized that they read more like sentences and less like variables. I renamed everything to standard snake_case following Python and PostgreSQL conventions.

Examples:

- `current_location_of_patient` → `origin_department`
- `patient_destination_for_current_task` → `destination_department`
- `current_patient_biohazard_status` → `biohazard`
- `time_request_task_generated` → `created_at`

Short, readable names are easier to query and easier to understand in code. If a name needs more explanation, that belongs in documentation and not in the column name itself.

---

## Destination Field: Single Department Field

I considered three options for storing where the patient is going:

1. A single combined text string like `"ICU - Room 204"`
2. Two fields: `destination_department` + `destination_room`
3. One field: `destination_department` only

I went with option 3. The transporter's job is to deliver the patient to a department. The staff at that department handle the patient from there. The dispatcher doesn't need extra details but simply where to send them. Adding a room field would be extra complexity that the MVP (minimum viable product) workflow doesn't require.

---

## Origin Fields: Split Into Department and Room

For the pickup side I went the opposite direction. Origin uses two fields: `origin_department` and `origin_room`.

The transporter physically has to find the patient to pick them up. A department name alone (`"ICU"`) isn't enough — they need the room. Having two clean separate fields is better than one combined string because you don't have to parse or split anything if the system ever needs to use those values separately.

---

## total_time Is Not Stored

I originally planned to store `total_time` as a column that would be calculated when a request is completed. I decided against it.

`total_time` can always be derived from `completed_at - created_at`. Both of those values are already in the database. If I stored `total_time` separately and `completed_at` ever got corrected, the stored total time would be wrong. Storing a value that can be calculated from other values in the same row creates two sources of truth, which is a risk. The calculation happens at query time instead.

---

## Assignment Data Lives in request_assignment, Not transport_requests

Early on I had `transporter_id` as a column on the `transport_requests` table. I moved it to its own junction table.

The reason is that some jobs require more than one transporter. A single `transporter_id` column can only hold one value. If you need to assign two transporters to a request there's no clean way to do that with a single column. The junction table solves this — each row in `request_assignment` is one assignment, so a request needing two transporters just has two rows.

---

## equipment_needed Is Nullable

Not every transport requires equipment. A patient who can walk just needs staff guidance. If I made this field required I'd have to store a placeholder value like `"none"` for every unequipped transport, which isn't meaningful data. Null correctly represents "no equipment needed for this request."

---

## Status Values Are Enforced by the Application, Not the Database

Both `transport_requests` and `transporters` have status fields stored as VARCHAR strings. The valid values are defined and enforced in the application code (service layer), not as a database-level ENUM.

Using PostgreSQL ENUMs would require a database migration every time a status value needs to change. For an MVP where things might still shift, a VARCHAR with application-level validation is faster to work with. The tradeoff is that the database itself won't reject an invalid string — the application has to catch that.

---

## Three Tables Only — No Locations Table, No Audit Log

I considered adding a `locations` table so department names would be validated foreign keys instead of free text. I also considered a `dispatch_events` table for logging state changes.

I decided against both for MVP. A locations table would mean I have to build and populate a list of all hospital departments before any requests can be created. That's extra infrastructure before the core workflows even exist. Free-text is good enough for the scope and user base of this project. Same reasoning for the audit log, it's useful but not required for the three workflows to function.

Both are reasonable things to add in a future version.

## Dashboard Visualization Technology Determination

I had several options for displaying my dashboard. For simplicity and clarity's sake, I went with Jinja2 as it has a native library built into Python and allows me to keep my project in a monolithic structure.

### Frontend: Jinja2 Server-Side Templates

What it is?

- FastAPI renders HTML on the server using Python data and sends complete pages to the browser.

Benefits

- Native FastAPI support, no extra tooling
- Everything lives in one Python codebase which follows the monolithic architecture
- No JavaScript build pipeline
- Browser receives complete HTML ,nothing to "fetch" after load
- Easier to understand for a backend focused learner
- It's fast to prototype

Tradeoffs

- Page refreshes to update data (no live updates without JavaScript)
- Less interactive than a JS driven frontend
- Tightly coupled to the backend which allows the frontend and backend to live together

Why it fits my project

- The dispatcher dashboard is a read heavy operational view. It doesn't need real-time reactivity or complex client side state. A full page refresh when assigning a transporter is acceptable. Jinja2 keeps the entire system in one place, which aligns with the monolithic architecture decision for my project.

---

These were the options I considered:

### Plain HTML/JS as Static Files

What it is?

- FastAPI serves an index.html file. JavaScript in the browser calls your REST API endpoint and renders the results dynamically.

Benefits

- Clean separation between frontend and backend
- Frontend can be built and tested independently
- More "modern" architecture pattern

Tradeoffs

- Requires JavaScript knowledge to fetch and render data
- Two layers to debug (frontend JS + backend API)
- More moving parts for my minimum viable product
- Still requires understanding REST (representational state transfer) API (application program interface) design before building anything visible

Why this stack didn't fit my project

- The added complexity of managing client-side JavaScript data fetching is not justified for a dashboard that three users will interact with. It also delays having anything visible until the API if fully functional.

---

### JavaScript Framework (React, Vue, Angular)

What it is?

- A dedicated frontend application, written in JavaScript, that communicates with your backend via API and gets deployed separately.

Benefits

- Industry standard for production web applications
- Highly interactive, no page refreshes
- Strong ecosystem and job market relevance

Tradeoffs

- Requires Node.js, npm, a build pipeline
- Separate deployment from the backend (breaks the monolithic architecture design choice I made)
- Steep learning curve on top of an already full backend build
- Complete overkill for a 3 workflow dispatcher dashboard

Why this stack didn't fit my project

- The scope of this stack would require learning an entirely separate ecosystem and I wanted to make an application with Python. The monolithic architecture decision ruled it out completely and a JavaScript framework implies a separate frontend application, which is the opposite of a monolith.
