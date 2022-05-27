"""
Additional layer for databases
"""

from .sqlite_tools import SQLiteStorage


class Storage:
    db = None

    def __init__(self, **params):
        pass
        self.storage_type = params.get('storage_type', False)
        self.path_to_db = params.get('path_to_db', '')

        if self.storage_type:
            if self.storage_type == 'sqlite' and self.path_to_db:
                self.db = SQLiteStorage(self.path_to_db)
        else:
            raise Exception("other storage types except 'sqlite' are not supported yet")

    def save(self, values:list):
        self.db.save(values)


