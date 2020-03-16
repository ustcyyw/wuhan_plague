# 项目数据库结构介绍

[toc]

## 数据库结构介绍

#### 1.全国疫情信息表 china_total_info

![total_info.png](https://github.com/ustcyyw/wuhan_plague/blob/master/version2.0/SQL_mysql/total_info.png?raw=true)

#### 2.省区疫情信息表 china_detail_info

![detailed_info.png](https://github.com/ustcyyw/wuhan_plague/blob/master/version2.0/SQL_mysql/detailed_info.png?raw=true)

#### 3.世界疫情信息表 world_detail_info

结构同表1，只有表名不同

#### 4. 各国疫情信息表 world_detail_info

结构同表2，只有表名不同

---

## 数据库创建及数据导入

本项目使用的DBMS是 mysql，可以按上一节中的表格结构自己创建（使用的软件是Navicat），也可以直接运行本文件夹中的四个.sql文件建立表格，需要数据的话可以通过README中的联系方式私信我。

---

## 注意事项

* 要允许爬虫项目，需要打开自己的mysql服务，且在设置文件中设置自己的数据库信息，并且创建好上述结构的两个表格。
* 表格名称不可更改，需要命名为`total_info`及`detailed_info`