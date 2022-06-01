import sched, time

import arrow
from lxml import html

from .interface import CrawlerInterface
from modules.common import DataStructure as DataStruct


class PastebinComCrawler(CrawlerInterface):
    name = 'PASTEBIN'
    tasks_list_url = 'https://pastebin.com/archive'
    task_prefix = 'https://pastebin.com'
    ScanNewTasksInterval = 0

    alive_status_url = ''

    @staticmethod
    def get_from_tree(tree, val:str, default_val='Unknown') -> str:
        raw_res = tree.xpath(val)
        return str(raw_res[0]) if len(raw_res) > 0 else default_val

    def get_new_tasks(self) -> list:
        page = self.transport.get(self.tasks_list_url, need_proxy=self.need_proxy, need_change_header=self.need_change_header, interval=self.ScanNewTasksInterval)
        tree = html.fromstring(page.content)

        main_table_urls = tree.xpath('//table[@class="maintable"]//tr/td//span/parent::node()/a/@href')

        res = []
        for link in main_table_urls:
            res.append(link)

        return res

    def do_work(self):
        try:
            if not self.alive_status_url:
                self.alive_status_url = self.cfg.get_param('CRAWLER.Pastebin', 'AliveStatusURL')
            self.transport.send_alive(self.alive_status_url)

            self.need_proxy = self.cfg.get_param('CRAWLER.Pastebin', 'RotateProxies').lower() == 'yes'
            self.need_change_header = self.cfg.get_param('CRAWLER.Pastebin', 'RotateHeaders').lower() == 'yes'
            self.ScanNewTasksInterval = self.cfg.get_param('CRAWLER.Pastebin', 'ScanNewTasksInterval')

            for task_url in self.get_new_tasks():
                if not self.cache.check(task_url):
                    task_raw = self.transport.get(f'{self.task_prefix}{task_url}', need_proxy=self.need_proxy, need_change_header=self.need_change_header, interval=0)

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

            new_keys = self.tasks.all_tasks_keys()

            all_tasks_list = self.tasks.all_tasks()
            self.log.info(f'[{self.name}] got {len(all_tasks_list)} new tasks')

            if len(new_keys) > 0:
                before_save = self.storage.count()
                self.storage.save(all_tasks_list)
                after_save = self.storage.count()
                if after_save - before_save <= 0:
                    self.log.debug(f'[{self.name}] problem with data {all_tasks_list}')

            for task_key in new_keys:
                self.tasks.remove(task_key)
                self.cache.add(task_key)

                self.log.info(f'[{self.name}]    saved {task_key} ')
        except:
            pass

    def start(self):
        s = sched.scheduler(time.time, time.sleep)
        def do_tick(sc):
            self.do_work()
            sc.enter(int(self.ScanNewTasksInterval), 1, do_tick, (sc,))

        s.enter(int(self.ScanNewTasksInterval), 1, do_tick, (s,))
        s.run()
