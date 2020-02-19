# -*- coding: utf-8 -*-
# @Time    : 2020/1/21 0021 下午 10:42
# @Author  : yyw@ustc
# @E-mail  : yang0@mail.ustc.edu.cn
# @Github  : https://github.com/ustcyyw
# @desc    : 数据库链接类，简单的封装

import pymysql
from Config import Setting


class MySQLCurSor:
    host = Setting.host
    user = Setting.user
    password = Setting.password

    def __init__(self, db):
        self.__conn = pymysql.Connect(host=self.host, user=self.user,
                                      password=self.password, database=db, charset='utf8')
        self.__cursor = self.__conn.cursor()

    def execute(self, sql, args=None):
        """

        :param sql: 要执行的sql语句
        :param args: tuple, list or dict
        :return:
        """
        self.__cursor.execute(sql, args=args)

    def execute_idu(self, sql, args=None):
        """
        执行增删改操作
        :param sql:
        :param args:
        :return: None
        """
        try:
            self.execute(sql, args)
            self.__conn.commit()
        except Exception as e:
            self.__conn.rollback()
            raise e

    def select(self, sql, args=None):
        """
        执行查询操作
        :param sql:
        :param args:
        :return:  元组类型 元素为查询到的每一个记录
        """
        self.execute(sql, args)
        return self.__cursor.fetchall()

    def close(self):
        self.__cursor.close()
        self.__conn.close()
