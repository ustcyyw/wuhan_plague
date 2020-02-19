# -*- coding: utf-8 -*-
# @Time    : 2020/1/23 0023 下午 4:45
# @Author  : yyw@ustc
# @E-mail  : yang0@mail.ustc.edu.cn
# @Github  : https://github.com/ustcyyw
# @desc    : 将数据按json格式传给前端


from MySQL_service import MySQLCurSor
from Config import Setting


class BaseSelector:
    index_column_dict = {
        1: 'diagnosis_num',
        2: 'suspect_num',
        3: 'cure_num',
        4: 'death_num'
    }

    def __init__(self, table, *column_index):
        """

        :param table: 要查询的表的名称
        :param column_index: 可变参数 可写 1 2 3 4。至少选择一列，至多选择4列，参数按从小到大的顺序
        """
        self.mysql_saver = MySQLCurSor(Setting.db)
        self.column_index = column_index
        self.table = table

        self.sql = self.get_base_sql()
        self.data = None

    def get_base_sql(self):
        """
        得到基础的 SELECT 语句
        :return: SELECT语句，无WHERE GROUP ORDER
        """
        if len(self.column_index) == 0:
            return "SELECT * FROM {}".format(self.table)
        else:
            sql = "SELECT "
            for i in range(len(self.column_index)):
                sql += self.index_column_dict.get(self.column_index[i]) + ", "
            sql += "recording_time" + " "
            sql += "FROM " + self.table
        return sql

    def get_data(self, sql):
        """
        将sql语句的查询结果按列归类
        :param sql: 执行的sql语句
        """
        original_data = self.mysql_saver.select(sql)
        result_date = []
        count_column = len(original_data[0])
        for i in range(count_column):
            temp_list = []
            result_date.append(temp_list)
        for one_record in original_data:
            for i in range(count_column):
                if i == count_column - 1:
                    result_date[i].append(one_record[i].strftime("%m-%d %H:%M"))
                else:
                    result_date[i].append(one_record[i])
        self.data = result_date
