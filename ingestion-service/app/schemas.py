from pydantic import BaseModel
from datetime import datetime


class WaterSensorEvent(BaseModel):
    event_id: str
    sensor_id: str
    timestamp: datetime
    latitude: float
    longitude: float
    water_level_m: float
