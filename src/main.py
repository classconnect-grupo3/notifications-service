from src.database.db_init import initialize_database
from src.errors.exceptions_handler import configure_exception_handlers
from fastapi import FastAPI
from src.routes import router as api_router

app = FastAPI()

# Initialize the database (create tables if they don't exist)
initialize_database()

app.include_router(api_router)

# Register custom exception handlers
configure_exception_handlers(app)
