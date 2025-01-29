from sqlalchemy import Column, Integer, String
from app.database import Base

class Moto(Base):
    __tablname__ = "motos"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    marca = Column(String)
    cilindrada = Column(String)
    ano = Column(Integer)
    valor = Column(Integer)
    