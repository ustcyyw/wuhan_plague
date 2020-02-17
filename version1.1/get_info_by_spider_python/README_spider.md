# 爬虫分项目介绍

[toc]

## 项目简介

​	项目开启于2020年1月23日，从肥科回到家后一天。丁香园制作了一个[疫情信息网站](https://3g.dxy.cn/newh5/view/pneumonia)，可以查看确诊人数，疑似病例，治愈人数，死亡人数。于是决定定时爬取网站上的人数信息(全国/各省区)。一开始的目的仅仅是为了练习一下**爬虫**，后来疫情信息越来越严重就感觉这些信息可以记录一下这段历史，或许会有用呢？（大雾）:sweat_smile:。我设定1个小时爬取一次信息，不过由于丁香园的web一直在迭代经常半夜就报错，所以爬取的信息是有遗漏的。:black_heart:

----

## 各文件简介

1. Config.py：配置文件
2. URLDealer.py：处理http请求获得response
3. Plague_info.py ：解析提取页面数据
4. MySQL_service.py：进行数据库操作的类及存储二进制文件的类
5. Info_saver.py：函数模块，与数据库交互存储数据到数据库中
6. select_data.py：提供一个可扩展的查询数据类
7. main.py：本项目的函数入口
8. test.py：本项目的单元测试模块

----

## 各文件详细介绍

#### 	Config.py

​		进行数据库配置；URL请求地址，timeout及请求头；爬取间隔

#### 	URLDealer.py： `URLDealer`类

  1. `get_response()`方法：通过死循环保证http请求成功时(status_code = 200)时得到response对象，在遇到异常或者请求错误时仅打印错误信息。这样就避免程序在面临复杂网络环境时抛出非必要异常。

  2. `get_soup()`方法：将response对象封装为bs4包中的`BeautifulSoup`实例

     ​	**个人感觉这个类在爬虫项目中进行get请求时可以直接复用**

#### Plague_info.py : `PlagueInfo`类

1. 这个类其实很鸡肋 因为各种页面都是不一样的 包括这个项目爬取的丁香园疫情网页，从23号开始爬取到现在我已经修改了5.6次了
2. `detailed_info()`方法：提取各个省区的信息：确诊人数，疑似人数，治愈人数，死亡人数。将str取出后剩下的就是使用正则表达式将自己需要的信息提取，放入字典中。再将每个省的数据放入字典中，以省区名字为键。
3. `total_info()`类方法：将各省信息汇总为全国信息。

#### MySQL_service.py

1. `MySQLSaver`类：对`pymysql`中数据库连接类简单封装，可以执行查询与增删改，直接写入SQL语句。在本项目中为了将全国信息及各省市的信息存入数据库中
2. `ImgSaver`类：存储二进制文件，原本是拿来存储jpg文件的，不过后来我解析不到图片链接了 :angry:.

#### Info_saver.py

1. `get_count()`函数：从存储各省信息的库中得到上次存储的序号，用于标记当前存储的序号。
2. `save_total_info(mySQL, total_info)`函数：单次存储全国信息进数据库
3. `save_detailed_info(mySQL, detailed_info, count)`函数：单次存储各省区信息进数据库
4. `get_info_once(count, time_now)`函数：单次从web获得数据后解析并存储信息进数据库

#### select_data.py

1. 构造函数传入要查询的表，及要查询的数据：column_index: 可变参数 可写 1 2 3 4。至少选择一列，至多选择4列，参数按从小到大的顺序

2. `get_base_sql(self)`函数：构造得到sql语句

3. `get_data(self, sql)`函数：执行sql语句，得到查询结果并存放在`self.data`中

    **此基础类可以扩展数据的进一步处理，也可通过继承创建查询指定数据的类**

#### main.py

​	程序*入口*：通过死循环及`time.sleep()`阻塞主进程以按设定间隔运行程序

#### test.py

​	项目单元测试模块。`@test_decorator`装饰器提示测试开始，测试结束及测试结果等信息。在这个文件中可以对各个方法进行单元测试，方便写程序时一个接口一个接口的排除bug

****

## 注意事项

* 数据库的设计及介绍见 [SQL_mysql](https://github.com/ustcyyw/wuhan_plague/tree/master/version1.1/SQL_mysql) 中，必须开启数据库服务，配置好数据库，建好数据表才能运行本项目，否则数据库异常。
* 丁香园的网页进行改版后可能需要更新 Plague_info.py 不要改变返回值的形式及类型，这样可以保证别的文件完全不需要更改

    









​	

