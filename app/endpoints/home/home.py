# -*- coding:utf-8 -*-

from fastapi import APIRouter

router_home = APIRouter(tags=["HOME"], prefix="/home")


@router_home.get(
    "/{username}/{passw}",
    summary="Home Endpoint",
    description="Get detail about home",
)
def get_home(username: int, passw: int):
    return {"success": True}
