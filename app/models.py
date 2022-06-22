from datetime import datetime
from typing import List
from pydantic import BaseModel
from geojson_pydantic import Feature, FeatureCollection, Point, LineString


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
    type:str = 'Feature'
    geometry: Point
    properties: TransportProperties

class TransportLocations(FeatureCollection):
    features: List[TransportLocation]


class LineProperties(BaseModel):
    id: str
    line: str
    name: str
    short_name: str
    operating: str
    serv_side: str
    bus_length: str
    oper_days: str

class MetrobusLine(Feature):
    type: str = 'Feature'
    geometry: LineString
    properties: LineProperties

class MetrobusLines(FeatureCollection):
    features: List[MetrobusLine]


class StopProperties(BaseModel):
    stop_id: str
    stop_name: str

class MetrobusStop(Feature):
    type: str = 'Feature'
    geometry: Point
    properties: StopProperties

class MetrobusStops(FeatureCollection):
    features: List[MetrobusStop]
