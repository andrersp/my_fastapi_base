# -*- coding: utf-8 -*-

from fastapi import FastAPI

from .config.config_app import config_app


def minimal_app() -> FastAPI:

    app = FastAPI(docs_url="/v1/docs", openapi_url="/v1/openapi.json")
    return app


def create_app() -> FastAPI:

    app = minimal_app()
    config_app(app=app)
    return app
