from sqlalchemy.orm import Session
from src.api.schemas.notification_preference import NotificationPreferenceUpdate
from src.api.common.result import Success, Failure
from src.api.repository.notifications_preferences import create_or_update_notification_preference

async def update_notification_preference(db: Session, user_id: str, data: NotificationPreferenceUpdate):
    try:
        updated_pref = create_or_update_notification_preference(
            db,
            uid=user_id,
            event_type=data.event_type,
            push_enabled=data.push_enabled,
            email_enabled=data.email_enabled
        )

        return Success(updated_pref)

    except Exception as e:
        return Failure(e)
