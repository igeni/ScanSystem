from modules.crawlers.crawler import Crawler
from modules.common import CrawlerType


crawler = Crawler(crawler_type=CrawlerType.PASTEBIN)


if __name__ == "__main__":
    crawler.start()