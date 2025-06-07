from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database.db import get_db
from src.schemas.fcm_token import FCMTokenRequest, FCMTokenResponse
from src.service.user_fcm_token import register_fcm_token, get_fcm_tokens
from src.common.result import Failure

router = APIRouter()


@router.post("/token", status_code=201, response_model=str)
def save_token(request: FCMTokenRequest, db: Session = Depends(get_db)):
    result = register_fcm_token(db, request)

    if isinstance(result, Failure):
        error = result.error
        raise HTTPException(status_code=error.http_status_code, detail=error.message)

    return result.value


@router.get("/tokens", status_code=200, response_model=list[FCMTokenResponse])
def list_tokens(uid: str, db: Session = Depends(get_db)):
    result = get_fcm_tokens(db, uid)

    if isinstance(result, Failure):
        error = result.error
        raise HTTPException(status_code=error.http_status_code, detail=error.message)

    return result.value
