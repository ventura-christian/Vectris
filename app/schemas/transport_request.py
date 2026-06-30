from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# What the caller send when creating a new transport request.
class TransportRequestCreate(BaseModel):
    patient_name: str
    origin_department: str
    origin_room: str
    destination_department: str
    equipment_needed: Optional[str] = None
    biohazard: bool = False
    transporters_required: int = 1


# What the API send back after reading from the database.
class TransportRequestOut(BaseModel):
    id: int
    patient_name: str
    origin_department: str
    origin_room: str
    destination_department: str
    equipment_needed: Optional[str]
    biohazard: bool
    transporters_required: int
    status: str
    created_at: datetime
    completed_at: Optional[datetime]
    # This allows Pydantic to read from a SQLAlchemy model instance.
    model_config = {"from_attributes": True}
