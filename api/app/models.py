from pydantic import BaseModel
from enum import Enum
from datetime import datetime
import uuid


class TaskStatus(str, Enum):
    pending = "pending"
    processing = "processing"
    done = "done"


class TaskCreate(BaseModel):
    title: str
    description: str | None = None


class Task(BaseModel):
    id: str
    title: str
    description: str | None = None
    status: TaskStatus = TaskStatus.pending
    created_at: datetime

    @staticmethod
    def new(data: TaskCreate) -> "Task":
        return Task(
            id=str(uuid.uuid4()),
            title=data.title,
            description=data.description,
            status=TaskStatus.pending,
            created_at=datetime.utcnow(),
        )
