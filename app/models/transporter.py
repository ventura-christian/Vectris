from sqlalchemy import Column, Integer, String
from app.database.session import Base


class Transporter(Base):
    """SQLAlchemy model for the transporters table."""

    __tablename__ = "transporters"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    status = Column(String, nullable=False, default="available")
