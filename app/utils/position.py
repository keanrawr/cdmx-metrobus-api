import requests
from google.transit import gtfs_realtime_pb2
from app.models import TransportLocation
from app.models import TransportLocations
from app.settings.app import AppSetting
from app.utils.parsers import parse_current_position


def query_current_position():
    settings = AppSetting()
    usr = settings.mb_username
    pwd = settings.mb_password
    url = 'http://app.citi-mb.mx/GTFS-RT/vehiculosPosicion'

    res = requests.get(url, auth=(usr, pwd))
    if res.status_code != 200:
        raise ValueError('Something went wrong, cannot fetch current position data')

    feed = gtfs_realtime_pb2.FeedMessage()
    feed.ParseFromString(res.content)

    positions = list()
    for entity in feed.entity:
        parsed_position = parse_current_position(entity)
        positions.append(TransportLocation(**parsed_position))

    return TransportLocations(features=positions)
