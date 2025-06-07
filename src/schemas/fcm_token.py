from pydantic import BaseModel
from datetime import datetime

class FCMTokenRequest(BaseModel):
    uid: str
    fcm_token: str

class FCMTokenResponse(BaseModel):
    fcm_token: str
    uid: str
    last_updated: datetime
