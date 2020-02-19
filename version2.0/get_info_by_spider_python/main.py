# -*- coding: utf-8 -*-
# @Time    : 2020/1/21 0021 下午 11:05
# @Author  : yyw@ustc
# @E-mail  : yang0@mail.ustc.edu.cn
# @Github  : https://github.com/ustcyyw
# @desc    :

import time

from Config import Setting
from Plague_info import PlagueInfo
from URLDealer import URLDealer
from Info_saver import MySQLSaver


def main():
    while True:
        # 基础页面的解析
        base_info_url_dealer = URLDealer(Setting.base_url, Setting.timeout)
        base_info_soup = base_info_url_dealer.get_soup()
        plague_info = PlagueInfo(base_info_soup)

        mysql_saver = MySQLSaver(plague_info)
        mysql_saver.save_info_once()

        time.sleep(Setting.loop_time)


if __name__ == '__main__':
    main()
