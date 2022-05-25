import configparser

from modules.config.config import Config
from modules.log_layer.logger_tool import LoggingLayer

cfg = Config('settings.cfg')
log = LoggingLayer(cfg)


log.debug("kjyugujhbhjb")
log.info("-kjbuyijmnjio")


if __name__ == "__main__":
    print("-+-")