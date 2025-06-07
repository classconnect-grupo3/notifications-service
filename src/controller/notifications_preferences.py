from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database.db import get_db
from src.common.result import Failure
from src.schemas.notification_preference import NotificationPreferenceUpdate
from src.service.notifications_preferences import update_notification_preference

router = APIRouter()


@router.post("preferences", status_code=200)
async def update_user_notification_preference(
    uid: str, preference: NotificationPreferenceUpdate, db: Session = Depends(get_db)
):
    result = await update_notification_preference(db, uid, preference)

    if isinstance(result, Failure):
        error = result.error
        raise HTTPException(status_code=error.http_status_code, detail=error.message)

    return {"data": "Notification preferences updated successfully"}
