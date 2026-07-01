from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.assignment import AssignmentCreate, AssignmentOut
from app.services import assignment_service

router = APIRouter()


@router.post('/', response_model=AssignmentOut)
def create_assignment(data: AssignmentCreate, db: Session = Depends(get_db)):
    try:
        return assignment_service.create_assignment(
            db, data.transport_request_id, data.transporter_id
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get('/{request_id}', response_model=list[AssignmentOut])
def get_assignments(request_id: int, db: Session = Depends(get_db)):
    return assignment_service.get_assignments_for_request(db, request_id)
