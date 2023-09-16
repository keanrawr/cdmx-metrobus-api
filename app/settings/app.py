from app import __version__
from typing import Any, Dict
from pydantic_settings import BaseSettings, SettingsConfigDict

class AppSetting(BaseSettings):
    mb_username: str
    mb_password: str

    title: str = 'CDMX Metrobus API'
    version: str = '0.0.0'

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            'title': self.title,
            'version': self.version,
        }
