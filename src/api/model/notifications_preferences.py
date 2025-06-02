from sqlalchemy import Column, String, Boolean
from src.api.database.db import Base

class NotificationPreference(Base):
    __tablename__ = "notification_preferences"

    uid = Column(String, primary_key=True)
    event_type = Column(String, primary_key=True) 
    push_enabled = Column(Boolean, default=True, nullable=False)
    email_enabled = Column(Boolean, default=True, nullable=False)
