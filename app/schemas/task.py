from pydantic import BaseModel, ConfigDict
from datetime import date
from enum import Enum


class TaskPriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class TaskType(str, Enum):
    bug = "bug"
    task = "task"

class TaskStatus(str, Enum):
    new = "new"
    in_progress = "in_progress"
    ready_for_staged = "ready_for_staged"
    rejected_by_qa = "rejected_by_qa"
    ready_for_qa = "ready_for_qa"
    closed = "closed"

class TaskBase(BaseModel):
    title: str
    status: TaskStatus
    type: TaskType
    priority: TaskPriority
    description: str
    due_date: date | None = None
    assignee: str | None = None
    screen_shot: str | None = None

class TaskCreate(TaskBase):
    user_id: int


class TaskUpdate (TaskBase):
    title: str | None = None
    status: TaskStatus | None = None
    type: TaskType | None = None
    priority: TaskPriority | None = None
    description: str | None = None
    due_date: date | None = None
    assignee: str | None = None
    screen_shot: str | None = None

class TaskResponse(TaskBase):
    id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)