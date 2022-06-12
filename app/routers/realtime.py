from fastapi import APIRouter
from app.models import TransportLocations
from app.utils.position import query_current_position

router = APIRouter(
    prefix='/realtime',
    tags=['Realtime Endpoints'],
)


@router.get('/current-location', response_model=TransportLocations)
def mb_current_location():
    return query_current_position()
