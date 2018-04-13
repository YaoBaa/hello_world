#_*_ coding:utf-8 _*_
import pymysql

conn = pymysql.Connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = 'YaoBa1996723',
    db = 'imooc',
    charset = 'utf8'
    )

#
cursor = conn.cursor()

sql_insert = 'insert into users(uid,uname) values(10,"name10")'
sql_update = 'update users set uname="name91" where uid=9'
sql_delete = 'delete from users where ud<3'

try:
    cursor.execute(sql_insert)
    print(cursor.rowcount)#查看上一条语句对数据库有多少行的影响
    cursor.execute(sql_update)
    print(cursor.rowcount)
    cursor.execute(sql_delete)
    print(cursor.rowcount)
    #此时数据库还没有更新，因为连接自动做了事物

    conn.commit()#提交事物，此时才真正执行
except Exception as e:
    print(e)
    conn.rollback()#删除语句修改为错误语句，在事物最后一个操作发现错误之后所有操作都不执行。
#关闭资源
cursor.close()
conn.close()