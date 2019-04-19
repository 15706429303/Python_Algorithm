# -*- coding:UTF-8 -*-
import MySQLdb


class OperateDatabase(object):
    def __init__(self, host, port, user, passwd, db):
        self.conn = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db,charset='utf8')
        self.cur = self.conn.cursor()

    def executeSQL(self, sql):
        try:
            self.cur.execute(sql)
        except:
            print 'your sql was wrong'


main = OperateDatabase('localhost',None,'root','root','mytest')
main.executeSQL("select column_name from test1")
res = main.cur.fetchall()
print res
main.conn.close()