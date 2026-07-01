from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.transporter import TransporterCreate, TransporterOut
from app.services import transporter_service

router = APIRouter()


@router.post('/', response_model=TransporterOut)
def create_transporter(data: TransporterCreate, db: Session = Depends(get_db)):
    return transporter_service.create_transporter(db, data)


@router.get('/', response_model=list[TransporterOut])
def list_transporters(db: Session = Depends(get_db)):
    return transporter_service.get_all_transporters(db)


@router.patch('/{transporter_id}/status', response_model=TransporterOut)
def update_transporter_status(
    transporter_id: int, new_status: str, db: Session = Depends(get_db)
):
    try:
        transporter = transporter_service.update_transporter_status(
            db, transporter_id, new_status
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    if transporter is None:
        raise HTTPException(status_code=404, detail='Transporter not found')

    return transporter
