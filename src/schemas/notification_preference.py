from pydantic import BaseModel
from typing import Optional

class NotificationPreferenceUpdate(BaseModel):
    event_type: str
    push_enabled: Optional[bool] = None
    email_enabled: Optional[bool] = None
