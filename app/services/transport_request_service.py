from sqlalchemy.orm import Session
from app.models.transport_request import TransportRequest
from app.schemas.transport_request import TransportRequestCreate
from typing import Optional


VALID_TRANSITIONS = {
    "active": "in_progress",
    "in_progress": "complete",
}


def create_request(db: Session, data: TransportRequestCreate) -> TransportRequest:
    # Creates a new SQLAlchemy model instance from the validated Pydantic input.
    request = TransportRequest(
        patient_name=data.patient_name,
        origin_department=data.origin_department,
        origin_room=data.origin_room,
        destination_department=data.destination_department,
        equipment_needed=data.equipment_needed,
        biohazard=data.biohazard,
        transporters_required=data.transporters_required,
    )
    db.add(request)
    db.commit()
    db.refresh(request)
    return request


def update_status(
    db: Session, request_id: int, new_status: str
) -> Optional[TransportRequest]:
    # Find the request or return None if it doesn't exist.
    request = (
        db.query(TransportRequest).filter(TransportRequest.id == request_id).first()
    )

    if request is None:
        return None

    # Enforce that the status can only move to its valid next state.
    if VALID_TRANSITIONS.get(request.status) != new_status:
        raise ValueError(f"Cannot transition from '{request.status}' to '{new_status}'")

    request.status = new_status

    # If completing the request, record when it finished
    if new_status == "complete":
        from datetime import datetime, timezone

        request.completed_at = datetime.now(timezone.utc)

    db.commit()
    db.refresh(request)
    return request
