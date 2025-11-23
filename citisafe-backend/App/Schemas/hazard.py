from pydantic import BaseModel

class HazardCreate(BaseModel):
    type: str  # e.g., 'fire', 'flood'
    severity: float
    description: str | None = None
    latitude: float
    longitude: float
    
class HazardResponse(BaseModel):
    id: str
    type: str
    severity: float
    description: str | None = None
    latitude: float
    longitude: float

    class Config:
        orm_mode = True