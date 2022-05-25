"""
    logger's test
"""
from time import sleep

from modules.config.config import Config
from modules.log_layer.logger_tool import LoggingLayer


FILENAME = 'tests/settings_test.cfg'
cfg = Config(FILENAME)
log = LoggingLayer(cfg)


def get_last_line(filename:str) -> str:
    with open(filename, 'r') as f:
        lines = f.readlines()

    return lines[-1] if len(lines)>0 else ""


def check_logging(msg:str, mark:str):
    if mark == 'debug':
        log.debug(msg)
    elif mark == 'info':
        log.info(msg)
    else:
        log.debug(msg)

    sleep(0.1)

    last_line = get_last_line(log.get_target())

    if msg not in last_line and last_line != '':
        assert False

def test_debug():
    check_logging("debug-test", 'debug')

def test_info():
    check_logging("info-test", 'info')
