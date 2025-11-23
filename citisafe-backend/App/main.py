from fastapi import FastAPI
from App.Routers import upload, cameras, hazards, routing

app = FastAPI(
    title = "CitiSafe API",
    description = "Real-time multi-modal hazard detection service",
)

app.include_router(upload.router, prefix="/api")
app.include_router(cameras.router, prefix="/api")
app.include_router(hazards.router, prefix="/api")
app.include_router(routing.router, prefix="/api")

app.get("/")
def root():
    return {"message": "CitiSafe API running"}