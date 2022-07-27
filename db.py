#!/usr/bin/env python3
#コメントテスト 2022.7.6 
import time
import mysql.connector

#--------------------
#主処理
#
#-------------------
def main():
    print("test")
    #dbから値を取り出す
    db_select()

#--------------------
# テスト用関数
#　テストテーブルに接続し値を全件取り出し接続を切る
#-------------------
def db_select():
    conn = mysql.connector.connect(host='localhost',port='3306',user='soma',password='Souma1993##',database='soma')
    conn.ping(reconnect=True)
    print(conn.is_connected())
    cur = conn.cursor()
    cur.execute("select * from cm_employ")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
