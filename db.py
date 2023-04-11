import sqlite3

conn = sqlite3.connect("D:/testdb.db")
cursor = conn.cursor()
sql = """select name from sqlite_master where type='table' order by name"""
cursor.execute(sql)
result = cursor.fetchall()
print(result)
print(type(result))

sql = """select * from doors_login """
cursor.execute(sql)
result = cursor.fetchall()
print(result)
print(type(result))


sql = """pragma table_info(doors_login)"""
cursor.execute(sql)
result = cursor.fetchall()
print(result)
print(type(result))

sql = """select password from doors_login where username = '123' """
cursor.execute(sql)
result = cursor.fetchall()
print(result)
print(type(result))
print(result[0][0])
print(type(result[0][0]))
conn.close()
