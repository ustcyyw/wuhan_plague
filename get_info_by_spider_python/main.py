# -*- coding: utf-8 -*-
# @Time    : 2020/1/21 0021 下午 11:05
# @Author  : yyw@ustc
# @E-mail  : yang0@mail.ustc.edu.cn
# @Github  : https://github.com/ustcyyw
# @desc    :

from Config import Setting
import assist_func as af
import time


def main():
    count = af.get_count()
    while True:
        count += 1
        af.get_info_once(count, time.time())
        time.sleep(Setting.loop_time)


if __name__ == '__main__':
    main()
