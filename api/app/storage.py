from app.models import Task

_tasks: dict[str, Task] = {}


def save(task: Task) -> Task:
    _tasks[task.id] = task
    return task


def get(task_id: str) -> Task | None:
    return _tasks.get(task_id)


def list_all() -> list[Task]:
    return list(_tasks.values())
