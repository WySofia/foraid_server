from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.db import get_db
from src.models.usuario import Usuario
from src.schemas.schemas import UsuarioCreate
from src.utils.security import (
    verify_password,
    create_access_token,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    hash_password,
)
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta

auth_router = APIRouter(prefix="/auth", tags=["auth"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


@auth_router.post("/signup", response_model=UsuarioCreate)
def signup(user: UsuarioCreate, db: Session = Depends(get_db)):
    db_user = db.query(Usuario).filter(Usuario.correo == user.correo).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Correo ya registrado")

    hashed_password = hash_password(user.contrasenia)
    db_user = Usuario(
        nombre=user.nombre,
        apellido=user.apellido,
        correo=user.correo,
        contrasenia_hash=hashed_password,
        cargo=user.cargo,
        rango=user.rango,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@auth_router.post("/token")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = db.query(Usuario).filter(Usuario.correo == form_data.username).first()

    if not user:
        raise HTTPException(status_code=400, detail="Correo o contraseña incorrectos")
    if not verify_password(form_data.password, user.contrasenia_hash):
        raise HTTPException(status_code=400, detail="Correo o contraseña incorrectos")

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.correo}, expires_delta=access_token_expires
    )

    return {"access_token": access_token, "token_type": "bearer"}
