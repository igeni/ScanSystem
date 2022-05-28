"""
    test of common tools
"""
from modules.common import DataStructure


def test_data_structure():
    rules = 'Guest Unknown anonymous hidden'.split()
    subst_val = ''
    DataStructure.init_rules(rules, subst_val)
    DataStructure.set_target_timezone('UTC')

    ds = DataStructure("Anonymous", "Title 2", "\n\tcontext 2\n\n   \t   ", "Thursday 26th of May 2022 11:11:11 PM CDT", "url1")
    assert ds.author == ""
    assert ds.title == "Title 2"
    assert ds.content == "context 2"
    assert ds.date == '2022-05-27 04:11:11 +00:00'
    assert ds.get_hash() == ds.hash_val

    ds2 = DataStructure("Anonymous", "Unknown", "\n\tcontext 2\n\n   \t   ", "Thursday 26th of May 2022 11:11:11 PM CDT", "url1")
    assert ds2.title == ''


