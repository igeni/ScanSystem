"""
    logger's test
"""

import pytest

from modules.config.config import Config
from modules.log_layer.logger_tool import LoggingLayer


FILENAME = 'tests/settings_test.cfg'
cfg = Config(FILENAME)
log = LoggingLayer(cfg)


@pytest.mark.skip(reason="no need to test")
def test_debug():
    log.debug("test")

@pytest.mark.skip(reason="no need to test")
def test_info():
    log.info("test")
