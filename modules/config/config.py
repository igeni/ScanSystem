"""
Provides tools to manage config
"""

import configparser
from modules.exceptions import MissingConfigKeyError


class Config:
    """
    base config class
    """
    def __init__(self, filename:str='../../settings.cfg'):
        self.configfile = filename
        self.config = configparser.ConfigParser()
        self.config.read(filename)

    def get_param(self, section:str,  key:str) -> str:
        """
        operate with config params
        """
        try:
            return self.config[section][key]
        except:
            raise MissingConfigKeyError(f"[{section}][{key}] not found in file '{self.configfile}'")
