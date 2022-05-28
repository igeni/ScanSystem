# """
#     test of sqlite tools
# """
# from modules.common import DataStructure
# from modules.storages.sqlite_tools import SQLiteStorage
#
# def test_data_structure():
#     storage = SQLiteStorage('tests/db_test.sqlite')
#
#     rules = 'Guest Unknown anonymous hidden'.split()
#     subst_val = ''
#     DataStructure.init_rules(rules, subst_val)
#     DataStructure.set_target_timezone('UTC')
#
#     ds1 = DataStructure("Anonymous", "Title 2", "\n\tcontext 1\n\n   \t   ", "Thursday 26th of May 2022 11:11:11 PM CDT", "url1")
#     ds2 = DataStructure("RealAuthor", "", "context 2", "Thursday 26th of May 2022 11:11:11 AM CDT", "url2")
#
#     count_before = storage.count()
#     storage.save([ds1, ds2])
#     count_after = storage.count()
#     assert count_after - count_before == 2
