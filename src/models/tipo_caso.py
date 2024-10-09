from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.db import Base


class TipoCaso(Base):
    __tablename__ = "tipo_caso"

    id_tipo_caso = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), unique=True, nullable=False)

    casos = relationship("src.models.caso.Caso", back_populates="tipo_caso")
