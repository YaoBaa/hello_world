#_*_ coding:utf-8 _*_
import pymysql

conn = pymysql.Connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = 'YaoBa1996723',
    db = 'stu_class',
    charset = 'utf8'
    )

#
cursor = conn.cursor()

print(conn)
print(cursor)

#关闭资源
cursor.close()
conn.close()