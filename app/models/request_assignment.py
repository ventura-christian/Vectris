from sqlalchemy import Column, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func
from app.database.session import Base


class RequestAssignment(Base):
    """SQLAlchemy model for the request_assignment table."""

    __tablename__ = "request_assignment"

    id = Column(Integer, primary_key=True)
    transport_request_id = Column(
        Integer, ForeignKey("transport_requests.id"), nullable=False
    )
    transporter_id = Column(Integer, ForeignKey("transporters.id"), nullable=False)
    assigned_at = Column(TIMESTAMP, nullable=False, server_default=func.now())
