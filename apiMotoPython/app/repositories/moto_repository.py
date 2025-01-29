from sqlalchemy.orm import Session
from app.models.moto import Moto

class MotoRepository:
    def __init__(self, db: Session):
        self.db = db
    
    
    def get_all(self):
        return self.db.query(Moto).all()


    def get_by_id(self, moto_id: int):
        return self.db.query(Moto).filter(Moto.id == moto_id).first()
    
    def create(self, moto: Moto):
        self.db.add(moto)
        self.db.commit()
        self.db.refresh(moto)
        return moto
    
    def delete(self, moto: Moto):
        self.db.delete(moto)
        self.db.commit()