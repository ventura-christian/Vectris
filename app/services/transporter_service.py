from sqlalchemy.orm import Session
from app.models.transporter import Transporter
from app.schemas.transporter import TransporterCreate
from typing import Optional

# The three valid status values for a transporter.
VALID_STATUSES = {"available", "on_job", "on_break"}


def create_transporter(db: Session, data: TransporterCreate) -> Transporter:
    # Build a new SQLAlchemy model instance from the validated Pydantic input.
    transporter = Transporter(
        name=data.name,
    )
    db.add(transporter)
    db.commit()
    db.refresh(transporter)
    return transporter


def get_all_transporters(db: Session) -> list[Transporter]:
    # Return every row in the transporters table.
    return db.query(Transporter).all()


def update_transporter_status(
    db: Session, transporter_id: int, new_status: str
) -> Optional[Transporter]:
    # Find the transporter or return None if it doesn't exist.
    transporter = db.query(Transporter).filter(Transporter.id == transporter_id).first()

    if transporter is None:
        return None

    if new_status not in VALID_STATUSES:
        raise ValueError(f"'{new_status}' is not a valid transporter status.")

    transporter.status = new_status
    db.commit()
    db.refresh(transporter)
    return transporter
