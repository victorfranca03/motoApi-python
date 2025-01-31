from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.moto_service import MotoService

router = APIRouter()

@router.get("/motos")
def listar_motos(db: Session = Depends(get_db)):
    service = MotoService(db)
    return service.listar_motos()

@router.post("/motos")
def criar_moto(moto: dict, db: Session = Depends(get_db)):
    service = MotoService(db)
    return service.criar_moto(moto)


