import pymysql
from tkinter import *

class MovieTable:
       def __init__(self):
              self.dbhost = 'localhost'
              self.dbuser = 'root'
              self.dbpass = 'y1565629372D'
              self.dbname = 'mydata'
              self.db = pymysql.connect(host=self.dbhost,user=self.dbuser,passwd=self.dbpass,db=self.dbname,charset='utf8')
              self.cur = self.db.cursor()
              self.List = []
              self.results = []
              self.title = ['Mname', 'Mtype', 'Mduration', 'Mdate', 'Mscore', 'Mallowance']
       def movie_insert(self, x):
              try:
                     self.db.ping(reconnect=True)
                     sql = 'insert into movies values(%s, %s, %s, %s, %s, %s)'
                     self.cur.execute(sql,(x[0], x[1], x[2], x[3], x[4], x[5]))
                     self.db.commit()
                     print('数据插入成功')
              except pymysql.Error as e:
                     print('数据库插入失败' + str(e))
                     self.db.rollback()
              self.db.close()
              
       def movie_update(self, x, y):
              try:
                     self.db.ping(reconnect=True)
                     sql = 'update movies set Mname = %s, Mtype = %s, Mduration = %s, Mdate = %s, Mscore = %s, Mallowance = %s where Mname = %s'
                     self.cur.execute(sql,(x[0], x[1], x[2], x[3], x[4], x[5], y))
                     self.db.commit()
                     print('数据插入成功')
              except pymysql.Error as e:
                     print('数据库插入失败' + str(e))
                     self.db.rollback()
              self.db.close()
              
       def movie_print(self):
              try:
                     self.db.ping(reconnect=True)
                     sql = 'select * from movies order by Mscore DESC'
                     self.cur.execute(sql)
                     results = self.cur.fetchall()
                     self.List = self.getresults(results)
                     
              except pymysql.Error as e:
                     print("数据查询失败"+str(e))
                     self.db.rollback()
              self.db.close()
              
       def movie_select(self, x):
              text = ''
              if x[0] != '':
                     text += " %s = '%s' and" % (self.title[0], x[0])
              if x[1] != '':
                     text += " %s = '%s' and" % (self.title[1], x[1])
              if x[2] != '':
                     text += " %s >= %s and" % (self.title[2], x[2])
              if x[3] != '':
                     text += " %s = '%s' and" % (self.title[3], x[3])
              if x[4] != '':
                     text += " %s >= %s and" % (self.title[4], x[4])
              if x[5] != '':
                     text += " %s >= %s and" % (self.title[5], x[5])
              text = text[:-3]
              
              try:
                     self.db.ping(reconnect=True)
                     sql = 'select * from movies where%s' % text
                     self.cur.execute(sql)
                     results = self.cur.fetchall()
                     self.results = list(results)
                     self.List = self.getresults(results)
                     
              except pymysql.Error as e:
                     print("数据查询失败"+str(e))
                     self.db.rollback()
              self.db.close()
              
       def movie_delete(self, x):
              try:
                     self.db.ping(reconnect=True)
                     sql = 'delete from movies where Mname = %s'
                     value=(x)
                     self.cur.execute(sql,value)
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
                     
                     x3 = spacenum(str(row[2]))
                     x4 = spacenum(row[3])
                     x5 = spacenum(str(row[4]))
                     x6 = spacenum(str(row[5]))
                     allstr = row[0]  + x1 * ' ' + row[1] + x2 * ' ' + str(row[2]) + x3 * ' ' + row[3] + x4 * ' ' + str(row[4]) + x5 * ' ' + str(row[5]) + x6 * ' '
                     x.append(allstr)
              return x

       
       
       def movie_update1(self, b, a):
              try:
                     self.db.ping(reconnect=True)
                     sql = "update movies set Mallowance = %s where Mname = %s"
                     self.cur.execute(sql,(b, a))
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
              
