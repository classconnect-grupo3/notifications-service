from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

from src.schemas.error_response import ErrorResponse


def configure_exception_handlers(app: FastAPI):
    @app.exception_handler(HTTPException)
    async def http_error_handler(request: Request, exc: HTTPException):
        title = exc.headers.get("X-Error", "Error") if exc.headers else "Error"
        error_response = ErrorResponse(
            type="https://example.com/errors/"
            + (
                exc.detail.replace(" ", "-").lower()
                if isinstance(exc.detail, str)
                else "unknown-error"
            ),
            title=title,
            status=exc.status_code,
            detail=exc.detail,
            instance=str(request.url),
        )
        return JSONResponse(
            status_code=exc.status_code, content=error_response.model_dump()
        )
    
