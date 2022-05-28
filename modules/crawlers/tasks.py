from typing import List
from modules.common import DataStructure


class Tasks:
    """
    active tasks storage
    """
    tasks = {}

    def add(self, val:DataStructure):
        self.tasks[val.url] = val

    def remove(self, key:str):
        self.tasks.pop(key, None)

    def check(self, key:str):
        return bool(self.tasks.get(key, False))

    def all_tasks(self) -> List[DataStructure]:
        result = []
        for key, val in self.tasks.items():
            result.append(val)

        return result

    def all_tasks_keys(self) -> list:
        result = []
        for key, val in self.tasks.items():
            result.append(key)

        return result
