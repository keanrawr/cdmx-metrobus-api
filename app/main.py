from fastapi import FastAPI
from app import __version__
from app.routers import realtime
from app.settings.app import AppSetting

settings = AppSetting(version=__version__)

app = FastAPI(**settings.fastapi_kwargs)
app.include_router(realtime.router)


@app.get('/', tags=['Root'])
def root():
    return 'ok'


@app.get('/version', tags=['Root'])
def api_version():
    return settings.version


@app.get('/healthcheck', tags=['Root'])
def health_check():
    return 'ok'
