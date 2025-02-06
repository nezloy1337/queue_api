from datetime import datetime
from typing import Any, Dict, Optional

from bson import ObjectId
from pydantic import BaseModel, Field


class ObjectIdTimeActionMixin(BaseModel):
    action: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class ActionLog(ObjectIdTimeActionMixin, BaseModel):
    status: str
    parameters: Dict[str, Any]
    error: str | None = None


class QueueEntryLog(ObjectIdTimeActionMixin, BaseModel):
    user_uuid: str
    queue_id: int
    position: int
    details: dict[str, Any] | None = None


class ExceptionLogTemplate(BaseModel):
    description: Optional[str] = None
    timestamp: Optional[datetime] = None
