from fastapi import FastAPI
from app.controllers.moto_controller import router as moto_router
from app.database import Base, engine

# Criar as tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluir rotas
app.include_router(moto_router, prefix="/api")
