from errors.exceptions_handler import configure_exception_handlers
from fastapi import FastAPI
from src.api.routes import router as api_router

app = FastAPI()


app.include_router(api_router)

# Register custom exception handlers
configure_exception_handlers(app)