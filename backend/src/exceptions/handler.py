from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from typing import Union
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError

async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()},
    )

async def integrity_exception_handler(request: Request, exc: IntegrityError):
    return JSONResponse(
        status_code=400,
        content={"detail": "Integrity constraint violation"},
    )

exception_handlers = {
    HTTPException: http_exception_handler,
    ValidationError: validation_exception_handler,
    IntegrityError: integrity_exception_handler,
}