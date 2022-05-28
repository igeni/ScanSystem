"""
Transport
"""

import requests
import time
from typing import List


class TransportLayer:
    """
    transport layer with using proxy and changing headers
    """
    proxies = []
    proxy_counter = 0

    headers = [
        {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36"},
    ]
    headers_counter = 0

    first_time = True

    def __init__(self, headers_list:List[dict]):
        if headers_list:
            self.set_headers(headers_list)

    def set_proxies(self, values:list):
        self.proxies = values

    def set_headers(self, values:List[dict]):
        if values:
            self.headers = values
        else:
            print("- empty headers list, we will use header by default -")

    def set_not_first_time_status(self):
        self.first_time = False

    def get(self, url, need_proxy:bool=False, need_change_header:bool = False, interval_sec:int=0):
        """
        getting content with replacing headers and ip's by RoundRobin algorithm
        """
        try:
            if not self.first_time:
                # print(f'waiting {interval_sec} seconds...')
                time.sleep(int(interval_sec))

            proxy = None
            if need_proxy:
                if not self.proxies:
                    raise Exception("you have to set proxies")
                self.proxy_counter = (self.proxy_counter + 1) % len(self.proxies)
                proxy = {'http': f'http://{self.proxies[self.proxy_counter]}'}

            if need_change_header:
                self.headers_counter = (self.headers_counter + 1) % len(self.headers)
            header = self.headers[self.headers_counter]

            # TODO for production purposes we need not to use RoundRobin with weights for proxies because unstable connection
            req = requests.get(url, headers=header, proxies=proxy)       # only http proxies
            return req
        except Exception as e:
            return None

    @staticmethod
    def send_alive(url:str):
        try:
            _ = requests.get(url=url)
        except:
            pass
