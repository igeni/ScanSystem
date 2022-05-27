import sqlite3
from typing import List

from .interface import StorageInterface
from modules.common import DataStructure as pasteStructures


class SQLiteStorage(StorageInterface):
    def __init__(self, filename:str):
        self.filename = filename
        self.conn = sqlite3.connect(filename)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def save(self, values:List[pasteStructures]) -> sqlite3.Cursor:
        sql_head = 'INSERT INTO pastes(author, title, content, posted) VALUES'
        sql_tail = ''
        for item in values:
            sql_tail += f"('{item.author}','{item.title}','{item.content}','{item.date}'),"

        return self.exec(f"{sql_head}{sql_tail[:-1]}")

    def get_result(self, script:str) -> sqlite3.Cursor:
        return self.cur.execute(script)

    def exec(self, script:str) -> sqlite3.Cursor:
        return self.cur.executescript(script)

