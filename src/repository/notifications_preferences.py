from sqlalchemy.orm import Session
from src.model.notifications_preferences import NotificationPreference


def get_notification_preference(
    db: Session, uid: str, event_type: str
) -> NotificationPreference:
    return (
        db.query(NotificationPreference)
        .filter_by(uid=uid, event_type=event_type)
        .first()
    )


def create_or_update_notification_preference(
    db: Session,
    uid: str,
    event_type: str,
    push_enabled: bool = None,
    email_enabled: bool = None,
) -> NotificationPreference:
    pref = get_notification_preference(db, uid, event_type)

    if not pref:
        pref = NotificationPreference(uid=uid, event_type=event_type)

    if push_enabled is not None:
        pref.push_enabled = push_enabled

    if email_enabled is not None:
        pref.email_enabled = email_enabled

    db.add(pref)
    db.commit()
    db.refresh(pref)

    return pref
