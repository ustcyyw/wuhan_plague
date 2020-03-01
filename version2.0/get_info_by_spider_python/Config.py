# -*- coding: utf-8 -*-
# @Time    : 2020/1/21 0021 下午 10:45
# @Author  : yyw@ustc
# @E-mail  : yang0@mail.ustc.edu.cn
# @Github  : https://github.com/ustcyyw
# @desc    : 配置类


class Setting:
    """数据库相关配置：host user 及密码"""
    host = 'localhost'
    user = 'root'
    password = ''
    db = 'plague_info'

    """瘟疫信息首页url"""
    base_url = 'https://3g.dxy.cn/newh5/view/pneumonia'

    """请求url的限定时间"""
    timeout = 10

    """url 请求头"""
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/' \
                      '537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
    }

    """存放瘟疫图示的文件夹地址"""
    path = 'C:/Users/Administrator/Desktop/plague/'

    """获取信息的时间间隔"""
    loop_time = 3600
