from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from sqlalchemy.sql import func

# Models inherit from 'Base'; denotes location of the class
from app.database.session import Base


class TransportRequest(Base):
    """
    SQLAlchemy model for the transport_requests table.
    """

    __tablename__ = "transport_requests"

    id = Column(Integer, primary_key=True)
    patient_name = Column(String, nullable=False)
    origin_department = Column(String, nullable=False)
    origin_room = Column(String, nullable=False)
    destination_department = Column(String, nullable=False)
    equipment_needed = Column(String, nullable=True)
    biohazard = Column(Boolean, nullable=False, default=False)
    transporters_required = Column(Integer, nullable=False, default=1)
    status = Column(String, nullable=False, default="active")
    created_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
    completed_at = Column(TIMESTAMP, nullable=True)
