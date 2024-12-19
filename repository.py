from ctypes import windll

from sqlalchemy import select

from database import new_session, TaskOrm
from shemas import STaskAdd, STask


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)
            session.add(task)
            await session.commit()
            await session.flush()
            return task.id

    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            quary = select(TaskOrm)
            result = await session.execute(quary)
            task_models = result.scalars().all()
            task_shemas = [STask.model_validate(task_model) for task_model in task_models]
            return task_shemas


