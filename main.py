from modules.crawlers.crawler import Crawler
from modules.common import CrawlerType


crawler = Crawler(crawler_type=CrawlerType.PASTEBIN)





# from modules.config.config import Config
# from modules.log_layer.logger_tool import LoggingLayer
#
# from modules.common import DataStructure, StorageType
# from modules.storages.storage import Storage
#
# cfg = Config('settings.cfg')
# log = LoggingLayer(cfg)
# # storage = SQLiteStorage('db.sqlite')
# storage = Storage(storage_type=StorageType.SQLITE, path_to_db='db.sqlite')
#
#
#
#
# log.debug("kjyugujhbhjb")
# log.info("kjbuyijmnjio")
#
# # init system
# rules = cfg.get_param('RULES', 'NormalizationRules').split()
# subst_val = cfg.get_param('RULES', 'SubstitutionString')
# DataStructure.init_rules(rules, subst_val)
# DataStructure.set_target_timezone(cfg.get_param('DEFAULT', 'SystemTimezone'))
#
# aaa = DataStructure("auth", "Title", "cont", "Thursday 26th of May 2022 11:11:11 PM CDT", "url1")
# # aaa = DataStructure("auth", "Title", "cont", "Thursday 26th of May 2022 21:21:21 CDT")
# bbb = DataStructure("Anonymous", "Title2", "\n\tcontext 2\n\n   \t   ", "Thursday 26th of May 2022 02:02:02 AM CDT", "url2")
#
# storage.save([aaa, bbb])
#
#
# print(aaa, bbb)


# from modules.crawlers.pastebin_com import PastebinComCrawler
# crawler = PastebinComCrawler()





# import sched, time
# s = sched.scheduler(time.time, time.sleep)
# def do_something(sc):
#     print("Doing stuff...")
#     # do your stuff
#     sc.enter(60, 1, do_something, (sc,))
#
# s.enter(60, 1, do_something, (s,))
# s.run()


if __name__ == "__main__":
    crawler.start()