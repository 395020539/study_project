#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

# 连接到数据库
conn = sqlite3.connect("D:\MyPython\study_project\SysEngDataDB.db")
# 创建一个游标对象
cursor = conn.cursor()

sql = """select name from sqlite_master where type='table' order by name"""
cursor.execute(sql)
result = cursor.fetchall()
print(result)
print(type(result))

sql = """select * from data_module_info """
cursor.execute(sql)
result = cursor.fetchall()
print(result)
print(type(result))


sql = """pragma table_info(doors_login)"""
cursor.execute(sql)
result = cursor.fetchall()
print(result)
print(type(result))

data_name = "TORQUE_CHANGE_INPUT_SHAFT_1"
sql = """select data_path from data_module_info where data_name = '{}' """.format(data_name)
# sql = """select data_path from data_module_info where data_name = 'TORQUE_CHANGE_INPUT_SHAFT_1' """
cursor.execute(sql)
result = cursor.fetchall()
print(result)
print(type(result))
print(result[0][0])
print(type(result[0][0]))


# cursor.execute("INSERT INTO data_module_info (data_path) VALUES ('123') ")

# 关闭游标和连接
cursor.close()
conn.close()