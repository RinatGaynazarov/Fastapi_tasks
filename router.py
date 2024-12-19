from fastapi import APIRouter
from typing import Annotated
from fastapi import FastAPI, Depends

from repository import TaskRepository
from shemas import STaskAdd, STask, STaskid

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"],
)



@router.post("")
async def add_task(
        task : Annotated[STaskAdd, Depends()]
) -> STaskid:
    task_id = await  TaskRepository.add_one(task)
    return {"ok" : True, "task_id" : task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await  TaskRepository.find_all()
    return tasks