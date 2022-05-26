"""
    test of sqlite tools
"""
from modules.common import DataStructure
from modules.storage.sqlite_tools import SQLiteStorage

def test_data_structure():

    storage = SQLiteStorage('tests/db_test.sqlite')

    rules = 'Guest Unknown anonymous hidden'.split()
    subst_val = ''
    DataStructure.init_rules(rules, subst_val)
    DataStructure.set_target_timezone('UTC')

    ds1 = DataStructure("Anonymous", "Title 2", "\n\tcontext 1\n\n   \t   ", "Thursday 26th of May 2022 11:11:11 PM CDT")
    ds2 = DataStructure("RealAuthor", "", "context 2", "Thursday 26th of May 2022 11:11:11 AM CDT")

    try:
        res0 = storage.get_result('SELECT COUNT(*) FROM pastes')
        count_before = res0.fetchall()[0][0]

        storage.save([ds1, ds2])

        res1 = storage.get_result('SELECT COUNT(*) FROM pastes')
        count_after = res1.fetchall()[0][0]

        assert count_after - count_before == 2

    except:
        assert False
