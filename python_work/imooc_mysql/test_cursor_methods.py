#_*_ coding:utf-8 _*_
import pymysql

conn = pymysql.Connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = '123456',
    db = 'stu_class',
    charset = 'utf8'
    )

#
cursor = conn.cursor()


sql = "select * from student"
cursor.execute(sql)
#此时本地缓冲区中已存放表的数据

print(cursor.rowcount)#打印行数
rs = cursor.fetchone()#获取结果的下一行
print(rs)
print(cursor.fetchone())#打印结果的下一行

print(cursor.fetchmany(2))#打印结果的下两行

print(cursor.fetchall())#打印结果的剩余行

#关闭资源
cursor.close()
conn.close()