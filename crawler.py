
from modules.config.config import Config
from modules.log_layer.logger_tool import LoggingLayer

from modules.common import DataStructure
# from modules.storage.sqlite_tools import SQLiteStorage
from modules.storage.storage import Storage

cfg = Config('settings.cfg')
log = LoggingLayer(cfg)
# storage = SQLiteStorage('db.sqlite')
storage = Storage(storage_type='sqlite', path_to_db='db.sqlite')




log.debug("kjyugujhbhjb")
log.info("kjbuyijmnjio")

# init system
rules = cfg.get_param('RULES', 'NormalizationRules').split()
subst_val = cfg.get_param('RULES', 'SubstitutionString')
DataStructure.init_rules(rules, subst_val)
DataStructure.set_target_timezone(cfg.get_param('DEFAULT', 'SystemTimezone'))

aaa = DataStructure("auth", "Title", "cont", "Thursday 26th of May 2022 11:11:11 PM CDT")
# aaa = DataStructure("auth", "Title", "cont", "Thursday 26th of May 2022 21:21:21 CDT")
bbb = DataStructure("Anonymous", "Title2", "\n\tcontext 2\n\n   \t   ", "Thursday 26th of May 2022 02:02:02 AM CDT")

storage.save([aaa, bbb])


print(aaa, bbb)

if __name__ == "__main__":
    print("-+-")