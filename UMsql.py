import pymysql

from tkinter import *

class UMTable:
       def __init__(self):
              self.dbhost = 'localhost'
              self.dbuser = 'root'
              self.dbpass = 'y1565629372D'
              self.dbname = 'mydata'
              self.db = pymysql.connect(host=self.dbhost,user=self.dbuser,passwd=self.dbpass,db=self.dbname,charset='utf8')
              self.cur = self.db.cursor()
              self.List = []
              self.results = []
              self.title = ['Uname', 'Uphone', 'Mname', 'num']
       def um_insert(self, x):
              try:
                     self.db.ping(reconnect=True)
                     sql = 'insert into um values(%s, %s, %s, %s)'
                     self.cur.execute(sql,(x[0], x[1], x[2], x[3]))
                     self.db.commit()
                     print('数据插入成功')
              except pymysql.Error as e:
                     print('数据库插入失败' + str(e))
                     self.db.rollback()
              self.db.close()
              
       def um_update(self, x, y):
              try:
                     self.db.ping(reconnect=True)
                     sql = 'update um set Uname = %s, Uphone = %s, Mname = %s, num = %s where Uname = %s and Mname = %s'
                     self.cur.execute(sql,(x[0], x[1], x[2], x[3], y[0], y[2]))
                     self.db.commit()
                     print('数据插入成功')
              except pymysql.Error as e:
                     print('数据库插入失败' + str(e))
                     self.db.rollback()
              self.db.close()
              
       def um_print(self):
              try:
                     self.db.ping(reconnect=True)
                     sql = 'select * from um'

                     self.cur.execute(sql)
                     results = self.cur.fetchall()
                     print(results)
                     self.List = self.getresults(results)
                     
              except pymysql.Error as e:
                     print("数据查询失败"+str(e))
                     self.db.rollback()
              self.db.close()
              
       def um_select(self, x):
              text = ''
              for i in range(4):
                     if  x[i] != '':
                            text += " %s = '%s' and" % (self.title[i], x[i])
                            
              text = text[:-3]
              
              try:
                     self.db.ping(reconnect=True)
                     sql = 'select * from um where%s' % text
                     self.cur.execute(sql)
                     results = self.cur.fetchall()
                     self.results = list(results)
                     self.List = self.getresults(results)
                     
              except pymysql.Error as e:
                     print("数据查询失败"+str(e))
                     self.db.rollback()
              self.db.close()
              
       def um_delete(self, x):
              try:
                     self.db.ping(reconnect=True)
                     sql = 'delete from um where Uname = %s and Mname = %s'
                     self.cur.execute(sql, (x[0], x[2]))
                     self.db.commit()
                     print('数据删除成功')
              except pymysql.Error as e:
                     print("数据删除失败" + str(e))
                     self.db.rollback()
              self.db.close()
       
       def getresults(self, results):
              x = []
              for row in results:
                     x1 = spacenum(row[0])
                     x2 = spacenum(row[1])
                     x3 = spacenum(row[1])
                     x4 = spacenum(str(row[2]))
                     allstr = row[0]  + x1 * ' ' + row[1] + x2 * ' ' + row[2] + x3 * ' ' + str(row[3]) + x4 * ' '
                     x.append(allstr)
              return x

       
 
       def um_update1(self, x):
              try:
                     self.db.ping(reconnect=True)
                     sql = "update um set num = %s where Uname = %s and Mname = %s"
                     self.cur.execute(sql,(x[0], x[1], x[2]))
                     self.db.commit()
                     print('数据插入成功')
              except pymysql.Error as e:
                     print('数据库插入失败' + str(e))
                     self.db.rollback()
              self.db.close()

       def um_update2(self, x):
              try:
                     self.db.ping(reconnect=True)
                     sql = "update um set Uname = %s, Uphone = %s where Uname = %s"
                     self.cur.execute(sql,(x[0], x[1], x[2]))
                     self.db.commit()
                     print('数据插入成功')
              except pymysql.Error as e:
                     print('数据库插入失败' + str(e))
                     self.db.rollback()
              self.db.close()
def spacenum(string):
       x = 0
       for i in string:
              if  '\u4e00' <= i <= '\u9fff':
                     x += 1
       y = len(string) - x
       cal = (21 - x * 1.8 - y) * 1.8
       return int(cal)
              
# tm = UMTable()
# tm.um_print()
# List = tm.List
# print(List)