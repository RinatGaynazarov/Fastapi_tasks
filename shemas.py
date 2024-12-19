from pydantic import BaseModel


class STaskAdd(BaseModel):
    name : str
    description: str = "Описание по умолчанию"

class STask(STaskAdd):
    id : int


class STaskid(BaseModel):
    ok : bool = True
    task_id: int