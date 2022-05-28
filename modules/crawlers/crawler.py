from .pastebin_com import PastebinComCrawler
from modules.common import CrawlerType


class Crawler:
    crawler = None

    def __init__(self, **params):
        self.crawler_type = params.get('crawler_type', False)

        fail = False
        if self.crawler_type:
            if self.crawler_type == CrawlerType.PASTEBIN:
                self.crawler = PastebinComCrawler()
            else:
                fail = True
        else:
            fail = True

        if fail:
            raise Exception("you have to define crawler's type correctly ")

    def start(self):
        self.crawler.start()
