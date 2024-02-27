import pymysql

class UserTable:
       def __init__(self):
              self.dbhost = 'localhost'
              self.dbuser = 'root'
              self.dbpass = 'y1565629372D'
              self.dbname = 'mydata'
              self.db = pymysql.connect(host=self.dbhost,user=self.dbuser,passwd=self.dbpass,db=self.dbname,charset='utf8')
              self.cur = self.db.cursor()
              self.List = []
              self.results = []
              self.title = ['Uname', 'Uphone', 'Ukey']
              
       def users_insert(self, x):
              try:
                     self.db.ping(reconnect=True)
                     sql = 'insert into users values(%s, %s, %s)'
                     self.cur.execute(sql,(x[0], x[1], x[2]))
                     self.db.commit()
                     print('数据插入成功')
              except pymysql.Error as e:
                     print('数据库插入失败' + str(e))
                     self.db.rollback()
              self.db.close()
              
       def users_print(self):
              try:
                     self.db.ping(reconnect=True)
                     sql = 'select * from users'
                     self.cur.execute(sql)
                     results = self.cur.fetchall()
                     self.List = self.getresults(results)
                     
              except pymysql.Error as e:
                     print("数据查询失败"+str(e))
                     self.db.rollback()
              self.db.close()

       def users_select(self, x):
              try:
                     self.db.ping(reconnect=True)
                     sql = 'select * from users where Uname = %s' 
                     self.cur.execute(sql, x)
                     results = self.cur.fetchall()
                     self.results = list(results)
                     self.List = self.getresults(results)
              
              except pymysql.Error as e:
                     print("数据查询失败"+str(e))
                     self.db.rollback()
              self.db.close()
              if self.results == []:
                     return True
              else:
                     return False
       def users_update(self, x, y):
              try:
                     self.db.ping(reconnect=True)
                     sql = 'update users set Uname = %s, Uphone = %s, Ukey = %s where Uname = %s'
                     self.cur.execute(sql,(x[0], x[1], x[2], y))
                     self.db.commit()
                     print('数据插入成功')
              except pymysql.Error as e:
                     print('数据库插入失败' + str(e))
                     self.db.rollback()
              self.db.close()
              
       def users_delete(self, str1, str2, str3):
              try:
                     self.db.ping(reconnect=True)
                     sql = 'delete from users where Uname = %s and Uphonenumber = %s and Upassword = %s'
                     value=(str1, str2, str3)
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
                     x3 = spacenum(row[2])
                     allstr = row[0]  + x1 * ' ' + row[1] + x2 * ' ' + row[2] + x3 * ' '
                     x.append(allstr)
              return x
       
       def select(self, x):
              try:
                     self.db.ping(reconnect=True)
                     sql = "select movies.Mname, movies.Mtype, movies.Mduration, movies.Mdate, \
movies.Mscore, um.num from movies, um where um.Mname = movies.Mname and um.Uname = '%s'  " % x
                     self.cur.execute(sql)
                     results = self.cur.fetchall()
                     self.List = self.getresults1(results)
              
              except pymysql.Error as e:
                     print("数据查询失败"+str(e))
                     self.db.rollback()
              self.db.close()

       def getresults1(self, results):
              x = []
              for row in results:
                     x1 = spacenum(row[0])
                     x2 = spacenum(row[1])
                     x3 = spacenum(str(row[2]))
                     x4 = spacenum(row[3])
                     x5 = spacenum(str(row[4]))
                     x6 = spacenum(str(row[5]))
                     allstr = row[0]  + x1 * ' ' + row[1] + x2 * ' ' + str(row[2]) + x3 * ' '\
                             + row[3]  + x4 * ' ' + str(row[4]) + x5 * ' ' + str(row[5]) + x6 * ' '
                     x.append(allstr)
              return x
       
def spacenum(string):
       x = 0
       for i in string:
              if  '\u4e00' <= i <= '\u9fff':
                     x += 1
       y = len(string) - x
       cal = (21 - x * 1.8 - y) * 1.8
       return int(cal)
              
