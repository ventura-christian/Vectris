# This file contains any logical decisions I made for the project

## Decision: Transport request data model

***[ ] = variables***

***Context:*** Defining each part of the job

---

Required for the request itself

- Job status
  - Active: Has been created but not assigned
    - [active]
  - In-progress: This job has been assigned and started
    - [in_progress]
  - Completed: The job has been finalized
    - [complete]

- Request assignment
  - The Transporter ID will be used to denote who is assigned each job
    - [transporter_ID]

- Number of transporters needed for job
  - [transporters_required]

Required for the patient involved with the request

- Patient name
  - [patient_name]
- Patient room number
  - [room_number]
- Patient location
  - [location]
- Request destination
  - [destination]
- Equipment required
  - [equipment_needed]
- Biohazard status
  - [biohazard_status]

Request information: these will be logged separately and tracked

- Time request came into queue
  - [created_at]
- Time request was finalized
  - [completed_at]

After job completed

- Transporter ID is logged
  - [transporter_ID]
- Request information: job start and end times
  - [created_at]
  - [completed_at]
- Total time on job (transporter received the job and until finalized)
  - [total_time]
  - This will be calculated with [created_at] & [completed_at]

***Reasoning***

---

Entities

- Transport request (the job)
- Transporter (the person doing the job)
