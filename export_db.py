#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import sqlite3

# 连接到数据库
def connect():
    conn = None
    try:
        conn = sqlite3.connect('D:\MyPython\study_project\SysEngDataDB.db')
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# 查询数据
def query_data(conn):
    df = None
    try:
        df = pd.read_sql_query("SELECT * from data_module_info", conn)
    except pd.errors.DatabaseError as e:
        print(f"Error querying data: {e}")
    return df

# 将数据写入Excel文件
def write_to_excel(df):
    try:
        df.to_excel("data_module.xlsx", index=False)
    except pd.errors.ExcelWriter as e:
        print(f"Error writing to Excel file: {e}")

# 关闭连接
def close_connection(conn):
    if conn:
        try:
            conn.close()
        except sqlite3.Error as e:
            print(f"Error closing database connection: {e}")

# 主函数
def main():
    conn = connect()
    if conn:
        df = query_data(conn)
        if df is not None:
            write_to_excel(df)
        close_connection(conn)
    else:
        print("Failed to connect to database.")

if __name__ == '__main__':
    main()
