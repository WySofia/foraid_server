from dotenv import load_dotenv
from fastapi import FastAPI
from src.routers.auth import auth_router
from src.routers.users import users_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(users_router)


# ruta de prueba
@app.get("/")
def read_root():
    return {"Hello": "World"}
