from app import __version__
from typing import Any, Dict
from pydantic import BaseSettings

class AppSetting(BaseSettings):
    mb_username: str
    mb_password: str

    title = 'CDMX Metrobus API'
    version: str = '0.0.0'

    class Config:
        env_file = '.env'

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            'title': self.title,
            'version': self.version,
        }
