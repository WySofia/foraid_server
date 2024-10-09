from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from src.db import Base


class Caracteristica(Base):
    __tablename__ = "caracteristicas"

    id_caracteristica = Column(Integer, primary_key=True, index=True)
    id_identikit = Column(
        Integer, ForeignKey("identikits.id_identikit"), nullable=False
    )
    nombre_caracteristica = Column(String(50), nullable=False)
    descripcion = Column(Text)

    identikit = relationship("Identikit", back_populates="caracteristicas")
