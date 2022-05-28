import arrow
from lxml import html

from .interface import CrawlerInterface
from modules.common import DataStructure as DataStruct


class PastebinComCrawler(CrawlerInterface):
    name = 'PASTEBIN'
    tasks_list_url = 'https://pastebin.com/archive'
    task_prefix = 'https://pastebin.com'
    ScanNewTasksInterval = 0

    @staticmethod
    def get_from_tree(tree, val:str, default_val='Unknown') -> str:
        raw_res = tree.xpath(val)
        return str(raw_res[0]) if len(raw_res) > 0 else default_val

    def get_new_tasks(self) -> list:
        page = self.transport.get(self.tasks_list_url, need_proxy=self.need_proxy, need_change_header=self.need_change_header, interval_sec=self.ScanNewTasksInterval)
        tree = html.fromstring(page.content)

        main_table_urls = tree.xpath('//table[@class="maintable"]//tr/td//span/parent::node()/a/@href')

        res = []
        for link in main_table_urls:
            res.append(link)

        return res


    def start(self):

        # FIXME Включить таймер на 120 секунд



        self.need_proxy = self.cfg.get_param('CRAWLER.Pastebin', 'RotateProxies').lower() == 'yes'
        self.need_change_header = self.cfg.get_param('CRAWLER.Pastebin', 'RotateHeaders').lower() == 'yes'
        self.ScanNewTasksInterval = self.cfg.get_param('CRAWLER.Pastebin', 'ScanNewTasksInterval')

        # FIXME Удалить ограничение для get_new_tasks()[]
        for task_url in self.get_new_tasks()[:10]:
            if not self.cache.check(task_url):
                task_raw = self.transport.get(f'{self.task_prefix}{task_url}', need_proxy=self.need_proxy, need_change_header=self.need_change_header, interval_sec=0)

                tree = html.fromstring(task_raw.content)

                author = self.get_from_tree(tree, '//div[@class="info-bottom"]/div/a//text()')
                title = self.get_from_tree(tree, '//div[@class="info-bar"]/div/h1//text()')

                default_date = arrow.now(DataStruct.get_target_timezone()).format(DataStruct.get_datetime_format())
                date = self.get_from_tree(tree, '//div[@class="info-bottom"]/div/span//@title', default_val=default_date)

                content_raw = tree.xpath('//div[@class="highlighted-code"]/div[@class="source"]//text()')
                content = ''.join(content_raw)

                self.tasks.add(
                    DataStruct(author=author, title=title, content=content, date=date, url=task_url)
                )

        all_tasks_list = self.tasks.all_tasks()
        self.storage.save(all_tasks_list)
        self.log.info(f'[{self.name}] got {len(all_tasks_list)} new tasks')

        for task_key in self.tasks.all_tasks_keys():
            self.tasks.remove(task_key)
            self.cache.add(task_key)

            self.log.info(f'[{self.name}]    saved {task_key} ')
