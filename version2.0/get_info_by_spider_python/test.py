# -*- coding: utf-8 -*-
# @Time    : 2020/1/21 0021 下午 9:08
# @Author  : yyw@ustc
# @E-mail  : yang0@mail.ustc.edu.cn
# @Github  : https://github.com/ustcyyw
# @desc    : 单元测试模块

from URLDealer import URLDealer
from Plague_info import PlagueInfo
from MySQL_service import MySQLCurSor
from Config import Setting
from select_date import BaseSelector


def test_decorator(function):
    def decorated_test(*args, **kwargs):
        print('测试开始: ' + function.__name__)
        try:
            result = function(*args, **kwargs)
        except Exception as e:
            print('发生异常: ' + str(e))
            raise e
        else:
            print('测试返回值为：' + str(result))
        print('测试结束: ' + function.__name__)

    return decorated_test


@test_decorator
def test_world_info():
    soup = URLDealer(Setting.base_url, Setting.timeout).get_soup()
    plague_info = PlagueInfo(soup)
    return plague_info.world_info()


def main():
    test_world_info()


if __name__ == '__main__':
    main()
