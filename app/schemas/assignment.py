from pydantic import BaseModel
from datetime import datetime


class AssignmentCreate(BaseModel):
    transport_request_id: int
    transporter_id: int


class AssignmentOut(BaseModel):
    id: int
    transport_request_id: int
    transporter_id: int
    assigned_at: datetime
    model_config = {'from_attributes': True}
