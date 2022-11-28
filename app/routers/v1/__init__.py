# -*- coding: utf-8 -*-

from fastapi import APIRouter, FastAPI

from app.endpoints.home.home import router_home

router_v1 = APIRouter(prefix="/v1")
router_v1.include_router(router_home)


def init_app(app: FastAPI):
    app.include_router(router_v1)
