"""
Additional layer for databases
"""

from .sqlite_tools import SQLiteStorage
from modules.common import StorageType


class Storage:
    db = None
    timezone: str

    def __init__(self, **params):
        self.storage_type = params.get('storage_type', False)
        self.path_to_db = params.get('path_to_db', '')
        self.path_to_db = params.get('path_to_db', '')
        self.timezone = params.get('timezone', 'UTC')

        fail = False
        if self.storage_type:
            if self.storage_type == StorageType.SQLITE and self.path_to_db:
                self.db = SQLiteStorage(self.path_to_db, timezone=self.timezone)
            else:
                fail = True
        else:
            fail = True

        if fail:
            raise Exception("other storage types except 'sqlite' are not supported yet")

    def save(self, values:list):
        self.db.save(values)

    def count(self) -> int:
        return self.db.count()

    def get_all_by_depth(self, hours:int) -> list:
        return self.db.get_all_by_depth(hours)

    def clean(self):
        self.db.clean()

    def clean(self):
        self.db.cl