from fastapi import APIRouter

from src.controller.notifications_preferences import (
    router as notifications_preferences_router,
)
from src.controller.user_fcm_token import router as fcm_token_router

router = APIRouter()


router.include_router(
    notifications_preferences_router,
    prefix="/preferences",
    tags=["Notification Preferences"],
)


router.include_router(
    fcm_token_router,
    prefix="user",
    tags=["FCM Token"],
)
