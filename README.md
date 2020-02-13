# wuhan_plague 项目

[toc]

## 项目简介

完整项目包括数据的爬取，数据的存储，及数据的读取。

数据爬取及存储使用python进行编写，在本仓库[get_info_by_spider_python](https://github.com/ustcyyw/wuhan_plague/tree/master/get_info_by_spider_python)中。DBMS使用mysql，表格结果及部分数据在本仓库[SQL_mysql](https://github.com/ustcyyw/wuhan_plague/tree/master/SQL_mysql)中。web后端使用java编写,提供几个查看数据的非常方便的接口，放在另外一个仓库 wuhan_plague_web 中。

## 项目目的

* 作为这个事情的亲历者，希望记录一些东西，或许之后会有用处
* 用于疫情结束之后分析原因，提供用于可视化的详细数据
* 在家宅着不能出门做一点东西

## 更改日志

* 2020年2月13日11:27:33 更改Plague_info.py第27~28行。修改原因：数据来源网站细微变更，原正则表达式匹配失败。

## 其它

* 武汉加油，中国加油！:heart:

* 疫情结束之后，如果觉得有用有意思的话给我一个star吧,请随意fork。欢迎讨论 微信Y154578009 /QQ154578009 