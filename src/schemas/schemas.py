from datetime import date
from typing import List, Optional
from pydantic import BaseModel, EmailStr


class UsuarioBase(BaseModel):
    nombre: str
    apellido: str
    correo: EmailStr
    cargo: Optional[str] = None
    rango: Optional[str] = None


class UsuarioCreate(UsuarioBase):
    contrasenia: str


class Usuario(UsuarioBase):
    id_usuario: int

    class Config:
        from_attributes = True


class UsuarioRead(UsuarioBase):
    pass


class UsuarioRead(UsuarioBase):
    id_usuario: int

    class Config:
        from_attributes = True


class TipoCasoBase(BaseModel):
    nombre: str


class TipoCaso(TipoCasoBase):
    id_tipo_caso: int

    class Config:
        from_attributes = True


class MetodoCreacionBase(BaseModel):
    nombre: str


class MetodoCreacion(MetodoCreacionBase):
    id_metodo_creacion: int

    class Config:
        from_attributes = True


class CasoBase(BaseModel):
    fecha: date
    titulo: str
    descripcion: Optional[str] = None
    id_tipo_caso: int
    calle_principal: Optional[str] = None
    calle_secundaria: Optional[str] = None
    provincia: Optional[str] = None
    canton: Optional[str] = None


class CasoCreate(CasoBase):
    pass


class Caso(CasoBase):
    id_caso: int
    id_usuario: int

    class Config:
        from_attributes = True


class IdentikitBase(BaseModel):
    fecha_creacion: date
    id_metodo_creacion: int
    imagen: Optional[str] = None


class IdentikitCreate(IdentikitBase):
    pass


class Identikit(IdentikitBase):
    id_identikit: int
    id_caso: int

    class Config:
        from_attributes = True


class CaracteristicaBase(BaseModel):
    nombre_caracteristica: str
    descripcion: Optional[str] = None


class CaracteristicaCreate(CaracteristicaBase):
    pass


class Caracteristica(CaracteristicaBase):
    id_caracteristica: int
    id_identikit: int

    class Config:
        from_attributes = True
