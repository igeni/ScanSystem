import sqlite3
from typing import List

import arrow

from .interface import StorageInterface
from modules.common import DataStructure


class SQLiteStorage(StorageInterface):
    def __init__(self, filename:str, timezone:str):
        self.timezone = timezone
        self.datetime_format = 'YYYY-MM-DD HH:mm:ss ZZ'
        self.filename = filename
        self.conn = sqlite3.connect(filename)
        self.cur = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def save(self, values:List[DataStructure]) -> sqlite3.Cursor:
        sql_head = 'INSERT INTO pastes(author, title, content, posted, url) VALUES'
        sql_tail = ''
        for item in values:
            sql_tail += f'("{item.author}","{item.title}","{item.content}","{item.date}","{item.url}"),'

        if sql_tail:
            res = self.exec(f'{sql_head}{sql_tail[:-1]}')
            return res
        else:
            return self.cur

    def get_result(self, script:str) -> sqlite3.Cursor:
        return self.cur.execute(script)

    def exec(self, script:str) -> sqlite3.Cursor:
        try:
            return self.cur.executescript(script)
        except Exception as e:
            return None

    def count(self) -> int:
        res0 = self.get_result('SELECT COUNT(*) FROM pastes')
        return res0.fetchall()[0][0]

    def get_all_by_depth(self, hours:int) -> list:
        tz = self.timezone
        depth = arrow.now(tz).shift(hours=-hours).format(self.datetime_format)
        res_db = self.get_result(f"SELECT url FROM pastes WHERE posted >= '{depth}'")

        result = []
        for item in res_db.fetchall():
            result.append(item[0])

        return result

    def clean(self):
        _ = self.get_result(f"DELETE FROM pastes WHERE 1")

    def close(self):
        self.conn.close()
