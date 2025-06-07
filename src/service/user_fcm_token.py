from sqlalchemy.orm import Session
from src.repository.user_fcm_token import save_token, get_tokens_by_uid, delete_token
from src.schemas.fcm_token import FCMTokenRequest, FCMTokenResponse
from src.common.result import Success, Failure


def register_fcm_token(db: Session, request: FCMTokenRequest):
    try:
        save_token(db, request.uid, request.fcm_token)
        return Success({"message": "Token registrado con éxito"})
    except Exception as e:
        return Failure(e)


def get_fcm_tokens(db: Session, uid: str) -> list[FCMTokenResponse]:
    try:
        tokens = get_tokens_by_uid(db, uid)
        token_responses = [
            FCMTokenResponse(
                fcm_token=t.fcm_token,
                uid=t.uid,
                platform=t.platform,
                last_updated=t.last_updated,
            )
            for t in tokens
        ]
        return Success(token_responses)
    except Exception as e:
        return Failure(e)


def remove_fcm_token(db: Session, fcm_token: str):
    try:
        deleted = delete_token(db, fcm_token)
        if not deleted:
            return Failure(Exception("Token no encontrado"))
        return Success({"message": "Token eliminado con éxito"})
    except Exception as e:
        return Failure(e)
