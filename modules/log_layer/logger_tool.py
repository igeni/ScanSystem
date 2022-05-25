"""
Additional layer for logging
"""

from loguru import logger

from modules.config.config import Config

class LoggingLayer:
    """
    base logging class
    """

    def __init__(self, cfg_val):
        if cfg_val is not None:
            self.cfg = cfg_val
        else:
            self.cfg = Config('../settings.cfg')

        tgt = f"{self.cfg.get_param('LOGS', 'Folder')}/{self.cfg.get_param('LOGS', 'Filename')}"
        fmt = self.cfg.get_param('LOGS', 'Format')
        lvl = self.cfg.get_param('LOGS', 'Level')
        rot = self.cfg.get_param('LOGS', 'Rotation')

        self.tgt = tgt

        logger.add(self.tgt, format=fmt, level=lvl, rotation=rot, enqueue=True)


    def debug(self, val:str):
        logger.debug(val)

    def info(self, val:str):
        logger.info(val)




