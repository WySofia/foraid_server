from sqlalchemy import Column, Integer
from sqlalchemy.sql.sqltypes import String
from sqlalchemy.orm import relationship
from src.db import Base


class MetodoCreacion(Base):
    __tablename__ = "metodo_creacion"

    id_metodo_creacion = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), unique=True, nullable=False)

    identikits = relationship("Identikit", back_populates="metodo_creacion")
