from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
import uuid

class TokenBase(SQLModel):
    token: str = Field(primary_key=True)
    user_id: uuid.UUID = Field(nullable=False, index=True)
    expires_at: datetime = Field(nullable=False, index=True)
    is_revoked: bool = Field(default=False, index=True)

class Token(TokenBase, table=True):
    created_at: datetime = Field(default=datetime.utcnow(), index=True)

class TokenCreate(TokenBase):
    pass

class TokenRead(TokenBase):
    created_at: datetime