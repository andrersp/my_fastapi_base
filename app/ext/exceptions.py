# -*- coding: utf-8 -*-
from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.ext.default_errors import ERRORS


async def exception_handler(req: Request, exc: Exception):

    if not f"{exc}":
        exc = Exception("INTERNAL_ERROR")
    status_code = 400

    match (len(exc.args)):
        case 1:
            error_name = f"{exc}"
            error_detail = ERRORS[error_name]
        case 2:
            error_detail = ERRORS[exc.args[0]]
            error_detail["detail"] = exc.args[1]
        case 3:
            error_detail = ERRORS[exc.args[0]]
            error_detail["detail"] = exc.args[1]
            status_code = int(exc.args[2])
        case _:
            error_detail = ERRORS["INTERNAL_ERROR"]

    return JSONResponse(
        status_code=status_code, content=jsonable_encoder(error_detail)
    )


def error_payload_handler(req: Request, exc: RequestValidationError):
    error_detail = ERRORS["INVALID_PAYLOAD"]
    error_param = exc.errors()[0]["loc"][1]
    erro_message = exc.errors()[0]["msg"]
    error_detail["detail"] = f"{error_param}: {erro_message}"

    return JSONResponse(
        status_code=400, content=jsonable_encoder(error_detail)
    )


def init_app(app: FastAPI):
    app.add_exception_handler(Exception, exception_handler)
    app.add_exception_handler(RequestValidationError, error_payload_handler)
    pass
