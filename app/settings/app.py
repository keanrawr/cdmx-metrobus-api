from pydantic import BaseSettings

class AppSetting(BaseSettings):
    mb_username: str
    mb_password: str

    class Config:
        env_file = '.env'
