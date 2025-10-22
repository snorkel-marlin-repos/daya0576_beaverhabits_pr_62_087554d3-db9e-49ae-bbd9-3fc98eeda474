from typing import Optional

from nicegui import context

from beaverhabits.storage.storage import Habit

ROOT_PATH_KEY = "root_path"
ROOT_PATH_DEFAULT = "/"

DEMO_ROOT_PATH = "/demo"
GUI_ROOT_PATH = "/gui"


def is_page_demo() -> bool:
    return context.client.page.path.startswith(DEMO_ROOT_PATH)


def get_root_path() -> str:
    path = context.client.page.path
    return DEMO_ROOT_PATH if path.startswith(DEMO_ROOT_PATH) else GUI_ROOT_PATH


def get_habit_page_path(habit: Habit) -> str:
    return f"{get_root_path()}/habits/{habit.id}"


def get_habit_heatmap_path(habit: Habit) -> str:
    return f"{get_root_path()}/habits/{habit.id}/streak"


def get_page_title(path: Optional[str] = None) -> str:
    path = path or context.client.page.path
    return "Demo" if path.startswith(DEMO_ROOT_PATH) else "Habits"


def is_demo() -> bool:
    return context.client.page.path.startswith(DEMO_ROOT_PATH)
