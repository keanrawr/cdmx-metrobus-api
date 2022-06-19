from fastapi import FastAPI
from app.routers import realtime


app = FastAPI(title='CDMX Metrobus Location')
app.include_router(realtime.router)


@app.get('/', tags=['Root'])
def root():
    return 'ok'


@app.get('/version', tags=['Root'])
def api_version():
    return '0.0.0'


@app.get('/healthcheck', tags=['Root'])
def health_check():
    return 'ok'
