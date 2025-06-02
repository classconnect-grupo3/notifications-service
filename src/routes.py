from fastapi import APIRouter

from src.controller.notifications_preferences import (
    router as notifications_preferences_router,
)


router = APIRouter()


router.include_router(
    notifications_preferences_router,
    prefix="/preferences",
    tags=["Notification Preferences"],
)
