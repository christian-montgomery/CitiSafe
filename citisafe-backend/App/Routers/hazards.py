from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from geoalchemy2.shape import from_shape, to_shape
from shapely.geometry import Point

from App.Db.database import get_db
from App.Models.hazard import Hazard
from App.Schemas.hazard import HazardCreate, HazardResponse

router = APIRouter(
    prefix="/hazards",
    tags=["Hazards"],
)

@router.post("/", response_model=HazardResponse)
def create_hazard(payload: HazardCreate, db: Session = Depends(get_db)):
    point = from_shape(Point(payload.longitude, payload.latitude), srid=4326)
    
    hazard = Hazard(
        type=payload.type,
        severity=payload.severity,
        description=payload.description,
        location=point
    )
    
    db.add(hazard)
    db.commit()
    db.refresh(hazard)
    
    point = to_shape(hazard.location)
    lon, lat = point.x, point.y

    
    return HazardResponse(
        id=hazard.id,
        type=hazard.type,
        severity=hazard.severity,
        description=hazard.description,
        longitude=lon,
        latitude=lat,
    )
    
@router.get("/", response_model=list[HazardResponse])
def list_hazards(db: Session = Depends(get_db)):
    hazards = db.query(Hazard).all()
    response = []
    
    for hazard in hazards:
        point = to_shape(hazard.location)
        lon, lat = point.x, point.y

        response.append(
            HazardResponse(
                id=hazard.id,
                type=hazard.type,
                severity=hazard.severity,
                description=hazard.description,
                longitude=lon,
                latitude=lat,
            )
        )
    
    return response
