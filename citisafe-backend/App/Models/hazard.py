import uuid
from sqlalchemy import Column, Float, String, DateTime
from geoalchemy2 import Geometry
from datetime import datetime
from App.Db.database import Base

class Hazard(Base):
    __tablename__ = "hazards"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    type = Column(String, nullable=False)  # e.g., 'fire', 'flood'
    severity = Column(Float, nullable=False)
    description = Column(String)
    location = Column(Geometry(geometry_type='POINT', srid=4326))
    timestamp = Column(DateTime, default=datetime.utcnow)