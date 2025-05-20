from fastapi import FastAPI

app = FastAPI(
    title="API Usuarios",
    version="1.0.5",
    description="API ejemplo",
    contact={
        "name": "Roberto Uriel Martínez Martínez",
        "email": "r_uriel_mtz@outlook.com"
    }
)

@app.get("/", tags=["Inicio"])
def home():
    return {"mensaje": "Bienvenido"}
