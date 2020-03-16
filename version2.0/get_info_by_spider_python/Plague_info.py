# -*- coding: utf-8 -*-
# @Time    : 2020/1/21 0021 下午 9:32
# @Author  : yyw@ustc
# @E-mail  : yang0@mail.ustc.edu.cn
# @Github  : https://github.com/ustcyyw
# @desc    : 疫情信息获得

import re


class PlagueInfo:
    """
    属于页面解析类 完全不可扩展
    """

    def __init__(self, soup):
        self.soup = soup

    def china_info(self):
        """
        获得全国分省区的瘟疫情况
        :return:
        """
        content = self.soup.find('script', id='getAreaStat').text
        march_data = re.search("window\\.getAreaStat = \\[(.*)\\]", content)
        str_data = march_data.group(1)
        pattern = re.compile('"provinceShortName":"(.*?)","currentConfirmedCount":\\d*?,"confirmedCount":(\\d*?),'
                             '"suspectedCount":(\\d*?),"curedCount":(\\d*?),"deadCount":(\\d*?),')
        province_datas = pattern.findall(str_data)
        print('check!!', province_datas)
        result_dict = {}
        for province_data in province_datas:
            province = province_data[0]
            diagnosis_num = int(province_data[1])
            suspect_num = int(province_data[2])
            cure_num = int(province_data[3])
            death_num = int(province_data[4])

            num_dict = {'确诊': diagnosis_num, '疑似': suspect_num, '死亡': death_num, '治愈': cure_num}
            result_dict[province] = num_dict

        return result_dict

    def world_info(self):
        """
        获取全球各个国家及地区的信息
        :return:
        """
        content = self.soup.find('script', id='getListByCountryTypeService2true').text
        march_data = re.search("window\\.getListByCountryTypeService2true = \\[(.*)\\]", content)
        str_data = march_data.group(1)
        pattern = re.compile('"provinceName":"(.*?)".*?"confirmedCount":(\\d*?),'
                             '"suspectedCount":(\\d*?),"curedCount":(\\d*?),"deadCount":(\\d*?),')
        area_datas = pattern.findall(str_data)
        print('check!!', area_datas)
        result_dict = {}
        for area_data in area_datas:
            if area_data[0] == "中国":
                continue
            area = area_data[0]
            diagnosis_num = int(area_data[1])
            suspect_num = int(area_data[2])
            cure_num = int(area_data[3])
            death_num = int(area_data[4])

            num_dict = {'确诊': diagnosis_num, '疑似': suspect_num, '死亡': death_num, '治愈': cure_num}
            result_dict[area] = num_dict

        return result_dict

    @classmethod
    def total_info(cls, detailed_info):
        """
        获得全国的瘟疫情况，返回值为字典。
        :param detailed_info: self.detailed_info()或者self.world_info()的返回值
        :return:
        """
        diagnosis_num, suspect_num, cure_num, death_num = 0, 0, 0, 0
        for num_dict in detailed_info.values():
            diagnosis_num += num_dict["确诊"]
            suspect_num += num_dict["疑似"]
            cure_num += num_dict["治愈"]
            death_num += num_dict["死亡"]
        total_info = {"确诊": diagnosis_num, "疑似": suspect_num, "治愈": cure_num, "死亡": death_num}
        return total_info
