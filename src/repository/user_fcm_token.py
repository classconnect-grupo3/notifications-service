from sqlalchemy.orm import Session
from src.model.user_fcm_token import UserToken
from datetime import datetime


def save_token(db: Session, uid: str, fcm_token: str) -> UserToken:
    token = db.query(UserToken).filter_by(fcm_token=fcm_token).first()
    if token:
        token.last_updated = datetime.now()
    else:
        token = UserToken(
            uid=uid,
            fcm_token=fcm_token,
            last_updated=datetime.now(),
        )
        db.add(token)
    db.commit()
    db.refresh(token)
    return token


def get_tokens_by_uid(db: Session, uid: str) -> list[UserToken]:
    return db.query(UserToken).filter_by(uid=uid).all()
