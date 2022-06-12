from datetime import datetime
from typing import List
from pydantic import BaseModel
from geojson_pydantic import Feature, FeatureCollection, Point

class TransportProperties(BaseModel):
    vehicle_id: str
    vehicle_label: str
    bearing: float
    odometer: float
    speed: float
    trip_id: str
    start_timestamp: datetime
    timestamp: datetime

class TransportLocation(Feature):
    type:str = 'Feature',
    geometry: Point
    properties: TransportProperties


class TransportLocations(FeatureCollection):
    features: List[TransportLocation]
