import hashlib
from enum import Enum
from dataclasses import dataclass
from dateutil import parser, tz

import arrow

@dataclass
class DataStructure:
    """Class for data"""
    RULES = []
    SUBSTITUTION = ''
    TARGET_TIMEZONE = tz.gettz('UTC')
    FORMAT = 'YYYY-MM-DD HH:mm:ss ZZ'

    author: str
    title: str
    content: str
    date: str
    hash_val: str
    url: str
    timezones: dict

    def __init__(self, author:str, title:str, content:str, date:str, url:str):
        self.author = author
        self.title = title
        self.content = content
        self.date = date
        self.url = url

        self.hash_val = ""

        tz_utc = tz.gettz('UTC')
        tz_et = tz.gettz('US/Eastern')
        tz_ct = tz.gettz('US/Central')
        tz_mt = tz.gettz('US/Mountain')
        tz_pt = tz.gettz('US/Pacific')

        self.timezones = {
            'CST': tz_ct, 'CDT': tz_ct,
            'EST': tz_et, 'EDT': tz_et,
            'MST': tz_mt, 'MDT': tz_mt,
            'PST': tz_pt, 'PDT': tz_pt,
            'UTC': tz_utc,
        }

        self.normalize()
        self.hash_val = self.get_hash()

    @classmethod
    def init_rules(cls, rules:list, val:str):
        cls.RULES = [item.lower() for item in rules]
        cls.SUBSTITUTION = val

    @classmethod
    def set_target_timezone(cls, val:str):
        cls.TARGET_TIMEZONE = tz.gettz(val)

    @classmethod
    def set_datetime_format(cls, val:str):
        cls.FORMAT = val

    def normalize(self):
        if self.author.lower() in DataStructure.RULES:
            self.author = DataStructure.SUBSTITUTION

        if self.title.lower() in DataStructure.RULES:
            self.title = DataStructure.SUBSTITUTION

        dt = parser.parse(self.date, tzinfos=self.timezones)
        self.date = arrow.get(dt).to(DataStructure.TARGET_TIMEZONE).format(self.FORMAT)

        self.content = self.content.strip()


    def get_hash(self):
        if not self.hash_val:
            hstr = self.author + self.title + self.date + self.content
            hash_val = hashlib.md5(hstr.encode()).hexdigest()
        else:
            hash_val = self.hash_val

        return hash_val


class StorageType(Enum):
    SQLITE = 0
    REDIS = 1
    POSTGRES = 2

class CrawlerType(Enum):
    PASTEBIN = 0
    TINYPASTE = 1
    GIST = 2
