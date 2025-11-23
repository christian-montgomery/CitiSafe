from sqlalchemy import Column, Float, String, DateTime
from geoalchemy2 import Geometry
from datetime import datetime
from App.Database import Base

class Hazard(Base):
    __tablename__ = "hazards"

    id = Column(String, primary_key=True)
    type = Column(String, nullable=False)  # e.g., 'fire', 'flood'
    score = Column(Float, nullable=False)
    description = Column(String)
    location = Column(Geometry(geometry_type='POINT', srid=4326))
    timestamp = Column(DateTime, default=datetime.utcnow)
    source = Column(String)  # e.g., 'camera_1', 'satellite'