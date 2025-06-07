from sqlalchemy import Column, String, DateTime
from datetime import datetime
from src.database.db import Base

class UserToken(Base):
    __tablename__ = "user_tokens"

    token = Column(String, primary_key=True)  # token único generado por Firebase
    uid = Column(String, index=True)
    last_updated = Column(DateTime, default=datetime.now)
