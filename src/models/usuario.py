from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.db import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    apellido = Column(String(50), nullable=False)
    correo = Column(String(100), unique=True, nullable=False, index=True)
    contrasenia_hash = Column(String, nullable=False)
    cargo = Column(String(50))
    rango = Column(String(50))

    casos = relationship("src.models.caso.Caso", back_populates="usuario")