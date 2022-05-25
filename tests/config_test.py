"""
    config's test
"""
from modules.config.config import Config


FILENAME = 'tests/settings_test.cfg'
cfg = Config(FILENAME)


def test_config():
    """
    test of correct params
    """

    assert cfg.get_param('DEFAULT', 'Param1') == "123"
    assert cfg.get_param('BASE', 'Param2') == "lorem ipsum"

def test_exit():
    """
    not found param key
    """

    section = 'BASE'
    key = 'NotFoundKey'
    try:
        cfg.get_param(section, key)
    except Exception as not_found_key_err:
        assert not_found_key_err.args[0] == f"[{section}][{key}] not found in file '{FILENAME}'"
