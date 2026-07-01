# TESTING CHECKLIST

> Last Updated: July 1, 2026

A manual reference for testing Vectris endpoints through Swagger UI while there's no automated test suite yet. Not a replacement for real tests, just a repeatable way to confirm my endpoints work.

## Before Testing Anything

1. Activate the virtual environment: `source venv/bin/activate`
2. Start the server: `uvicorn main:app --reload`
3. Open `http://127.0.0.1:8000/docs`

## One Thing to Note

Reference `entities.md` in my directory at `app/models/entities.md`. This document shows the information of all the tables and context to test my endpoints.

## Transporters

- `POST /transporters/`: create one with a name, confirm a 200 with an id and `"status": "available"`
- `GET /transporters/`: confirm the list includes what you just created
- `PATCH /transporters/{id}/status` with an invalid status: confirm 400
- `PATCH /transporters/{id}/status` with a made-up id: confirm 404
- `PATCH /transporters/{id}/status` with a valid status: confirm 200 and the status field actually changed

## Transport Requests

(add once built)

## Assignments

(add once built)
