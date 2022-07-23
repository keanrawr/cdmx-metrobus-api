import json
import pathlib
from fastapi import APIRouter
from app.models import MetrobusLines
from app.models import MetrobusStops

router = APIRouter(
    prefix='/infra',
    tags=['Infrastructure'],
)


def read_json(file_name:str):
    read_path = pathlib.Path(__file__).parent.parent / 'data' / file_name
    with open(read_path, 'r') as f:
        data = json.load(f)

    return data


@router.get('/lines', response_model=MetrobusLines, response_model_exclude_none=True)
def mb_lines():
    return read_json('lines-geojson.json')


@router.get('/stops', response_model=MetrobusStops, response_model_exclude_none=True)
def mb_stops():
    return read_json('stops-geojson.json')
