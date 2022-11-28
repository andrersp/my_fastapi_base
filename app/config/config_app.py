# -*- coding: utf-8 -*-
from importlib import import_module

from fastapi import FastAPI

from app.config.settings import settings


def config_app(app: FastAPI) -> None:
    app.title = settings.APP_TITLE
    app.description = "Base for FastAPI Application"

    for extension in settings.EXTENSIONS:
        mod = import_module(extension)
        mod.init_app(app)
