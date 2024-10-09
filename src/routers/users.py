from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.db import SessionLocal
from src.models.usuario import Usuario
from src.schemas.schemas import UsuarioRead, UsuarioCreate
from src.utils.security import oauth2_scheme, SECRET_KEY, ALGORITHM
from jose import JWTError, jwt

users_router = APIRouter(prefix="/users", tags=["users"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        correo: str = payload.get("sub")
        if correo is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(Usuario).filter(Usuario.correo == correo).first()
    if user is None:
        raise credentials_exception
    return user


@users_router.get("/me", response_model=UsuarioRead)
def read_users_me(current_user: Usuario = Depends(get_current_user)):
    return current_user
