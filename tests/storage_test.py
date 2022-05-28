"""
    test of sqlite tools
"""
import pytest

from modules.common import DataStructure, StorageType
from modules.storages.storage import Storage


def test_storage():
    storage = Storage(storage_type=StorageType.SQLITE, path_to_db='tests/db_test.sqlite')

    rules = 'Guest Unknown anonymous hidden'.split()
    subst_val = ''
    DataStructure.init_rules(rules, subst_val)
    DataStructure.set_target_timezone('UTC')

    ds1 = DataStructure("Anonymous", "Title 2", "\n\tcontext 1\n\n   \t   ", "Thursday 26th of May 2022 11:11:11 PM CDT", "url1")
    ds2 = DataStructure("RealAuthor", "", "context 2", "Thursday 26th of May 2022 11:11:11 AM CDT", "url2")

    count_before = storage.count()
    storage.save([ds1, ds2])
    count_after = storage.count()

    assert count_after - count_before == 2

    with pytest.raises(Exception) as e_info:
        _ = Storage(storage_type=StorageType.REDIS, path_to_db='tests/db_test.sqlite')

    with pytest.raises(Exception) as e_info:
        _ = Storage(path_to_db='tests/db_test.sqlite')

