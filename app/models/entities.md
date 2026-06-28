# ENTITIES

This file defines the database tables for Vectris. These three tables support the core MVP workflows: creating a transport request, assigning a transporter, and completing a request.

Last Updated: June 21, 2026

---

## Tables

- `transport_requests` — the job and all patient information
- `transporters` — the staff doing the work
- `request_assignment` — who is assigned to which job

---

### transport_requests

This table holds everything about a patient transport job from creation to completion.

| Column                   | Type      | Constraints                | Notes                                                                   |
| ------------------------ | --------- | -------------------------- | ----------------------------------------------------------------------- |
| `id`                     | SERIAL    | PRIMARY KEY                | Auto-generated. Each request gets a unique ID.                          |
| `patient_name`           | VARCHAR   | NOT NULL                   | Name of the patient being transported.                                  |
| `origin_department`      | VARCHAR   | NOT NULL                   | Department where the patient is being picked up.                        |
| `origin_room`            | VARCHAR   | NOT NULL                   | Room number at the pickup location.                                     |
| `destination_department` | VARCHAR   | NOT NULL                   | Department where the patient is being delivered.                        |
| `equipment_needed`       | VARCHAR   | NULLABLE                   | Wheelchair, stretcher, etc. Null means no equipment needed.             |
| `biohazard`              | BOOLEAN   | NOT NULL, DEFAULT FALSE    | Whether biohazard precautions are required.                             |
| `transporters_required`  | INTEGER   | NOT NULL, DEFAULT 1        | How many staff are needed for this job.                                 |
| `status`                 | VARCHAR   | NOT NULL, DEFAULT 'active' | Current state of the request.                                           |
| `created_at`             | TIMESTAMP | NOT NULL, DEFAULT NOW()    | When the request was created. Set automatically.                        |
| `completed_at`           | TIMESTAMP | NULLABLE                   | Set when status transitions to 'complete'. NULL means not yet complete. |

### Status values: transport tasks

### Active → In Progress → Complete

- `active` — request created, no one assigned yet
- `in_progress` — transporter assigned, job underway
- `complete` — transport finished, request closed

---

### transporters

This table holds information about transport staff and whether they are available.

| Column   | Type    | Constraints                   | Notes                          |
| -------- | ------- | ----------------------------- | ------------------------------ |
| `id`     | SERIAL  | PRIMARY KEY                   | Auto-generated unique ID.      |
| `name`   | VARCHAR | NOT NULL                      | Full name of the staff member. |
| `status` | VARCHAR | NOT NULL, DEFAULT 'available' | Current availability.          |

### Status values: transporters

- `available` — free to take a new assignment
- `on_job` — currently working a request
- `on_break` — temporarily unavailable

---

### request_assignment

This is a junction table that connects transport requests to the transporters assigned to them. It exists as its own table because a single request can require more than one transporter and I figured a single column on the request table couldn't handle that.

| Column                 | Type      | Constraints                          | Notes                           |
| ---------------------- | --------- | ------------------------------------ | ------------------------------- |
| `id`                   | SERIAL    | PRIMARY KEY                          | Auto-generated unique ID.       |
| `transport_request_id` | INTEGER   | NOT NULL, FK → transport_requests.id | The request being assigned.     |
| `transporter_id`       | INTEGER   | NOT NULL, FK → transporters.id       | The transporter being assigned. |
| `assigned_at`          | TIMESTAMP | NOT NULL, DEFAULT NOW()              | When the assignment was made.   |

### Relationships

**transport_requests** <-> **request_assignment** <-> **transporters**

One request can have many assignments. One transporter can have many assignments over time.

---

## Notes

- `total_time` is not stored as a column. It can always be calculated from `completed_at - created_at` when needed. Storing it separately would create two sources of truth.
- `destination_department` is a single field because transporters deliver to a department, not a specific room. The receiving staff handle room assignment on arrival.
- `origin_room` is required because the transporter needs an exact location to find the patient.
- `equipment_needed` is nullable because not every transport requires equipment.
