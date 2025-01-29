from sqlalchemy.orm import Session
from app.models.moto import Moto
from app.repositories.moto_repository import MotoRepository

class MotoService:
    def __init__(self, db: Session):
        self.repository = MotoRepository(db)

    def listar_motos(self):
        return self.repository.get_all()

    def criar_moto(self, dados_moto: dict):
        nova_moto = Moto(**dados_moto)
        return self.repository.create(nova_moto)
