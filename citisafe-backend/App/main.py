from fastapi import FastAPI
from App.Routers.hazards import router as hazards_router
from App.Db.database import Base, engine
from App.Models import hazard

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CitiSafe API",
    version="0.1.0"
)

app.include_router(hazards_router)

@app.get("/")
def root():
    return {"message": "CitiSafe backend is running"}