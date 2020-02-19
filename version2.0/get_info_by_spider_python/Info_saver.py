# -*- coding: utf-8 -*-
# @Time    : 2020/1/22 0022 下午 1:01
# @Author  : yyw@ustc
# @E-mail  : yang0@mail.ustc.edu.cn
# @Github  : https://github.com/ustcyyw
# @desc    : 存储数据的类
import datetime

from Config import Setting
from MySQL_service import MySQLCurSor


class MySQLSaver:
    def __init__(self, plague_info):
        self.mysql = MySQLCurSor(Setting.db)
        self.info = plague_info

    def __get_count(self, table_name):
        """
        从指定数据库中查找当前是第几次记录。
        :param table_name:
        :return:
        """
        sql = "SELECT MAX(count) FROM {}".format(table_name)
        result = self.mysql.select(sql)
        if result[0][0] is None:
            return 1
        else:
            return result[0][0] + 1

    def __get_china_detail_count(self):
        return self.__get_count("china_detail_info")

    def __get_world_detail_count(self):
        return self.__get_count("world_detail_info")

    def __save_detail_info(self, table_name, detailed_info):
        """
        单次存储中国省区或者世界各国（除中国）的详细信息
        :param detailed_info:指定存储中国还是全世界
        :param table_name:
        :return:
        """
        if table_name == 'china_detail_info':
            count = self.__get_china_detail_count()
        else:
            count = self.__get_world_detail_count()
        detailed_sql_pattern = "INSERT INTO {}(count, province, " \
                               "diagnosis_num, suspect_num, cure_num, death_num, recording_time)" \
                               + " VALUES ({}, '{}', {}, {}, {}, {}, '{}')"
        for area, info in detailed_info.items():
            detailed_sql = detailed_sql_pattern.format(table_name,
                                                       count, area, info.get('确诊', 0), info.get('疑似', 0),
                                                       info.get('治愈', 0), info.get('死亡', 0),
                                                       datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                                       )
            self.mysql.execute_idu(detailed_sql)

    def __save_china_detail_info(self, detail_info):
        self.__save_detail_info('china_detail_info', detail_info)

    def __save_world_detail_info(self, detail_info):
        self.__save_detail_info('world_detail_info', detail_info)

    def __save_total_info(self, table_name, total_info):
        """
        单次存储中国/全世界（除了中国）的汇总信息
        :param total_info: 指定存储中国还是全世界
        :param table_name:
        :return:
        """
        total_sql = "INSERT INTO {}(diagnosis_num, suspect_num, cure_num, death_num, recording_time)".format(table_name) \
                    + " VALUES ({}, {}, {}, {}, '{}')".format(
            total_info.get('确诊', 0), total_info.get('疑似', 0),
            total_info.get('治愈', 0), total_info.get('死亡', 0),
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.mysql.execute_idu(total_sql)

    def __save_china_total_info(self, total_info):
        self.__save_total_info('china_total_info', total_info)

    def __save_world_total_info(self, total_info):
        self.__save_total_info('world_total_info', total_info)

    def save_info_once(self):
        # 获取全国信息，分省信息，世界信息，各国信息
        china_detail_info = self.info.china_info()
        world_detail_info = self.info.world_info()
        china_total_info = self.info.total_info(china_detail_info)
        world_total_info = self.info.total_info(world_detail_info)

        # 信息存储
        self.__save_china_detail_info(china_detail_info)
        self.__save_world_detail_info(world_detail_info)
        self.__save_china_total_info(china_total_info)
        self.__save_world_total_info(world_total_info)

        self.mysql.close()


class ImgSaver:
    def __init__(self, filename, content):
        """

        :param filename: 文件绝对路径名 应该为JPG格式
        :param content: 二进制数据
        """
        self.filename = filename
        self.content = content

    def save(self):
        with open(self.filename, 'wb') as f:
            f.write(self.content)
        print('have saved file:' + self.filename)
