from sqlalchemy import Column, Date, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from src.db import Base


class Caso(Base):
    __tablename__ = "casos"

    id_caso = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, ForeignKey("usuarios.id_usuario"), nullable=False)
    fecha = Column(Date, nullable=False)
    titulo = Column(String(100), nullable=False)
    descripcion = Column(Text)
    id_tipo_caso = Column(Integer, ForeignKey("tipo_caso.id_tipo_caso"), nullable=False)
    calle_principal = Column(String(100))
    calle_secundaria = Column(String(100))
    provincia = Column(String(50))
    canton = Column(String(50))

    usuario = relationship("src.models.usuario.Usuario", back_populates="casos")
    tipo_caso = relationship("src.models.tipo_caso.TipoCaso", back_populates="casos")
    identikits = relationship("src.models.identikit.Identikit", back_populates="caso")
