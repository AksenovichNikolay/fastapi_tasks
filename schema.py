from pydantic import BaseModel

class TaskAdd(BaseModel):
    name: str
    description: str | None = None

class Task(TaskAdd):
    id: int

class TaskID(BaseModel):
    ok: bool = True
    task_id: int