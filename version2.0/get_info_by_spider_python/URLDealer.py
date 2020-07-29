# -*- coding: utf-8 -*-
# @Time    : 2020/1/21 0021 下午 9:03
# @Author  : yyw@ustc
# @E-mail  : yang0@mail.ustc.edu.cn
# @Github  : https://github.com/ustcyyw
# @desc    : 获得指定url得到的response或者soup
import time

import requests
import datetime

from bs4 import BeautifulSoup

from Config import Setting


class URLDealer:
    default_headers = Setting.headers

    def __init__(self, url, timeout):
        self.url = url
        self.timeout = timeout

    def get_response(self):
        """
        获得url的response
        :return:
        """
        while True:
            try:
                response = requests.get(self.url, headers=self.default_headers, timeout=self.timeout)
            except requests.exceptions.RequestException as exc:
                print("RequestException url: {}. Try again --time: {}".format(self.url, datetime.datetime.now()))
                print(str(exc))
                time.sleep(1)
            else:
                if response.status_code == 200:
                    response.encoding = response.apparent_encoding
                    print("Success url: {} --time: {}".format(self.url, datetime.datetime.now()))
                    return response
                else:
                    print("Error url: {}. Error code: {} --time: {}".format(self.url, response.status_code,
                                                                            datetime.datetime.now()))
                    time.sleep(1)

    def get_response_text(self):
        return self.get_response().text

    def get_soup(self):
        """
        获得url的response
        :return:
        """
        response = self.get_response()
        if response is not None:
            return BeautifulSoup(response.text, 'html.parser')
        else:
            print('response is None, can not make a soup')
            return None
