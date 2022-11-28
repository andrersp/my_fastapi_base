# -*- coding: utf-8 -*-

from functools import lru_cache
from os import environ as env

from pydantic import BaseSettings


class BaseConfig(BaseSettings):
    APP_TITLE: str = "Aplicativo BAse"
    EXTENSIONS: list = ["app.ext.exceptions", "app.routers.v1"]

    class Config:
        env_file = ".env"


class DevelopmentConfig(BaseConfig):
    DATABASE_URL: str = "sqlite"
    pass


class TestConfig(BaseConfig):
    DATABASE_URL: str = "sqlite:///database.sqlite"


@lru_cache()
def get_settings():
    config_name = env.get("FASTAPI_CONFIG", "development")
    config_cls_dict = {
        "development": DevelopmentConfig,
        "testing": TestConfig,
    }

    config_cls = config_cls_dict[config_name]
    return config_cls()


settings: BaseConfig = get_settings()
