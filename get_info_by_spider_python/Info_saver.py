# -*- coding: utf-8 -*-
# @Time    : 2020/1/22 0022 下午 1:01
# @Author  : yyw@ustc
# @E-mail  : yang0@mail.ustc.edu.cn
# @Github  : https://github.com/ustcyyw
# @desc    : 辅助函数:主要用于存储数据
import datetime

from Config import Setting
from Info_save import ImgSaver, MySQLSaver
from URLDealer import URLDealer
from Plague_info import PlagueInfo


def get_count():
    mySQL = MySQLSaver(Setting.db)
    sql = "SELECT MAX(count) FROM detailed_info"
    result = mySQL.select(sql)
    if result is None:
        return 0
    else:
        return result[0][0]


def get_info_once(count, time_now):
    # 基础页面的解析
    base_info_url_dealer = URLDealer(Setting.base_url, Setting.timeout)
    base_info_soup = base_info_url_dealer.get_soup()
    plague_info = PlagueInfo(base_info_soup)

    # 获取全国信息，分省信息，图片url
    detailed_info = plague_info.detailed_info()
    total_info = plague_info.total_info(detailed_info)
    # img_url = plague_info.img_url()

    # 全国信息，分省信息的存储
    mySQL = MySQLSaver(Setting.db)
    save_total_info(mySQL, total_info)
    save_detailed_info(mySQL, detailed_info, count)
    mySQL.close()

    # 图片的存储
    # save_img(img_url, time_now)


def save_total_info(mySQL, total_info):
    total_sql = "INSERT INTO total_info(diagnosis_num, suspect_num, cure_num, death_num, recording_time)" \
                + " VALUES ({}, {}, {}, {}, '{}')".format(
        total_info.get('确诊', 0), total_info.get('疑似', 0), total_info.get('治愈', 0), total_info.get('死亡', 0),
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    mySQL.execute_idu(total_sql)


def save_detailed_info(mySQL, detailed_info, count):
    detailed_sql_pattern = "INSERT INTO detailed_info(count, province, " \
                           "diagnosis_num, suspect_num, cure_num, death_num, recording_time)" \
                           + " VALUES ({}, '{}', {}, {}, {}, {}, '{}')"
    for province, info in detailed_info.items():
        detailed_sql = detailed_sql_pattern.format(
            count, province, info.get('确诊', 0), info.get('疑似', 0), info.get('治愈', 0), info.get('死亡', 0),
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
        mySQL.execute_idu(detailed_sql)


# def save_img(img_url, time_now):
#     img_content = URLDealer(img_url, Setting.timeout).get_response().content
#     img_save = ImgSaver(Setting.path + str(time_now) + '.jpg', img_content)
#     img_save.save()