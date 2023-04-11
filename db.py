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


import sqlite3
import time

# 连接到数据库
def connect():
    conn = None
    attempts = 0
    while attempts < 3:
        try:
            conn = sqlite3.connect('example.db')
            break
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            attempts += 1
            time.sleep(1)
    return conn

# 创建一个表
def create_table(conn):
    cursor = conn.cursor()
    try:
        cursor.execute('''CREATE TABLE IF NOT EXISTS stocks
                        (date text, trans text, symbol text, qty real, price real)''')
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

# 插入一些数据
def insert_data(conn):
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO stocks VALUES ('2022-01-05', 'BUY', 'AAPL', 100, 135.5)")
        cursor.execute("INSERT INTO stocks VALUES ('2022-02-15', 'SELL', 'AAPL', 50, 145.0)")
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error inserting data: {e}")
        conn.rollback()

# 查询数据
def query_data(conn):
    cursor = conn.cursor()
    try:
        for row in cursor.execute('SELECT * FROM stocks ORDER BY price'):
            print(row)
    except sqlite3.Error as e:
        print(f"Error querying data: {e}")

# 关闭游标和连接
def close_connection(conn):
    if conn:
        conn.close()

# 主函数
def main():
    conn = connect()
    if conn:
        create_table(conn)
        insert_data(conn)
        query_data(conn)
        close_connection(conn)
    else:
        print("Failed to connect to database.")

if __name__ == '__main__':
    main()

