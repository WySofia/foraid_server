from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from src.db import Base


class Identikit(Base):
    __tablename__ = "identikits"

    id_identikit = Column(Integer, primary_key=True, index=True)
    id_caso = Column(Integer, ForeignKey("casos.id_caso"), nullable=False)
    fecha_creacion = Column(Date, nullable=False)
    id_metodo_creacion = Column(
        Integer, ForeignKey("metodo_creacion.id_metodo_creacion"), nullable=False
    )
    imagen = Column(String(255))

    caso = relationship("src.models.caso.Caso", back_populates="identikits")
    metodo_creacion = relationship("src.models.metodo_creacion.MetodoCreacion", back_populates="identikits")
    caracteristicas = relationship("src.models.caracteristica.Caracteristica", back_populates="identikit")
