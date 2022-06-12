from datetime import date
from datetime import datetime


def parse_current_position(entity):

    start_date = entity.vehicle.trip.start_date
    start_time = entity.vehicle.trip.start_time

    start_date = date.today().strftime('%Y%m%d') if start_date == '' else start_date
    start_datetime = datetime.strptime(f'{start_date} {start_time}', '%Y%m%d %H:%M:%S')

    return {
        'type': 'Feature',
        'geometry': {
            'type': 'Point',
            'coordinates': [entity.vehicle.position.longitude, entity.vehicle.position.latitude]
        },
        'properties': {
            'vehicle_id': entity.vehicle.vehicle.id,
            'vehicle_label': entity.vehicle.vehicle.label,
            'bearing': entity.vehicle.position.bearing,
            'odometer': entity.vehicle.position.odometer,
            'speed': entity.vehicle.position.speed,
            'trip_id': entity.vehicle.trip.trip_id,
            'start_timestamp': start_datetime,
            'timestamp': entity.vehicle.timestamp,
        }
    }
