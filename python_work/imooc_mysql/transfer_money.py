#_*_ coding:utf-8 _*_
import sys
import pymysql

class TransferMoney(object):
    def __init__(self,conn):
        self.conn = conn

    #验证账号是否存在
    def check_acct_availablez(self,acctid):
        cursor = self.conn.cursor()#获取会话指针
        try:
            sql = "select * from account where acctid=%s"%acctid
            #执行sql语句
            cursor.execute(sql)
            print("check_acct_availablez:" + sql)#把sql打印出来用于调试
            #把结果放在变量里
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("账号%s不存在"%acctid)#抛出异常
        finally:
            cursor.close()

    #判断账户余额是否充足
    def has_enough_money(self,acctid,money):
        cursor = self.conn.cursor()
        try:
            sql = "select * from account where acctid=%s and money>=%s" %(acctid,money)
            # 执行sql语句
            cursor.execute(sql)
            print("has_enough_money:" + sql)  # 把sql打印出来用于调试
            # 把结果放在变量里
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception("账号%s余额不足" % acctid)
        finally:
            cursor.close()

    def reduce_money(self,acctid,money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money=money-%s where acctid=%s " % ( money,acctid)
            # 执行sql语句
            cursor.execute(sql)
            print("reduce_money:" + sql)  # 把sql打印出来用于调试
            if cursor.rowcount != 1:#看操作影响了多少行数据，若不唯一，说明操作失败
                raise Exception("账号%s减款失败" % acctid)
        finally:
            cursor.close()

    def add_money(self,acctid,money):
        cursor = self.conn.cursor()
        try:
            sql = "update account set money=money+%s where acctid=%s " % (money, acctid)
            # 执行sql语句
            cursor.execute(sql)
            print("add_money:" + sql)  # 把sql打印出来用于调试
            if cursor.rowcount != 1:  # 看操作影响了多少行数据，若不唯一，说明操作失败
                raise Exception("账号%s加款失败" % acctid)
        finally:
            cursor.close()

    def transfer(self,source_acctid,target_acctid,money):
        try:
            #检查账号ID是否可用
            self.check_acct_availablez(source_acctid)
            self.check_acct_availablez(target_acctid)

            #检查付款人余额是否充足
            self.has_enough_money(source_acctid,money)

            #付款人减少余额
            self.reduce_money(source_acctid,money)

            #收款人增加余额
            self.add_money(target_acctid,money)

            #提交事务
            self.conn.commit()

        except Exception as e:
            print(e)
            self.conn.rollback()


#如果程序被直接执行，那么运行下列代码，如果作为模块被导入，则不执行
if __name__ == "__main__":
    source_acctid = sys.argv[1]#第一个参数，付款人的ID
    target_acctid = sys.argv[2]#收款人ID
    money = sys.argv[3]#转账金额


    conn = pymysql.Connect(
        host = 'localhost',
        port = 3306,
        user = 'root',
        passwd = '123456',
        db = 'imooc',
        charset = 'utf8'
        )
    tr_money = TransferMoney(conn)

    try:
        tr_money.transfer(source_acctid,target_acctid,money)
    except Exception as e:
        print(e)
    finally:
        conn.close()