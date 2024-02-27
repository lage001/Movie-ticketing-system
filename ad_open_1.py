from tkinter import *
from Msql import *
from test import *


class Open1:
       def __init__(self,root):
              self.root = root
              self.frame2 = Frame(root,relief = RAISED, borderwidth = 1)
              self.frame2.pack(side = TOP, fill = X, ipadx = 100)

              frame2 = self.frame2
              Label(frame2, text = '电影名:').pack(side = LEFT)
              self.e1 = Entry(frame2)
              self.e1.pack(side = LEFT)
              Label(frame2, text = '类型:').pack(side = LEFT)
              self.e2 = Entry(frame2)
              self.e2.pack(side = LEFT)
              Label(frame2, text = '时长>=:').pack(side = LEFT)
              self.e3 = Entry(frame2)
              self.e3.pack(side = LEFT)
              Label(frame2, text = '日期:').pack(side = LEFT)
              self.e4 = Entry(frame2)
              self.e4.pack(side = LEFT)
              Label(frame2, text = '评分>=:').pack(side = LEFT)
              self.e5 = Entry(frame2)
              self.e5.pack(side = LEFT)
              Label(frame2, text = '剩余票数>=:').pack(side = LEFT)
              self.e6 = Entry(frame2)
              self.e6.pack(side = LEFT)
              Button(frame2, text = '搜索', width = 10, command = self.select).pack(side = LEFT)

              self.frame3 = Frame(root, relief = RAISED, borderwidth = 1)
              self.frame3.pack(side = TOP, fill = X)
              
              frame3 = self.frame3
              Button(frame3, text = '电影名', borderwidth =1, width = 20).pack(side = LEFT, fill = Y)
              Button(frame3, text = '类型', borderwidth =1, width = 20).pack(side = LEFT, fill = Y)
              Button(frame3, text = '时长/分钟', borderwidth =1, width = 20).pack(side = LEFT, fill = Y)
              Button(frame3, text = '日期', borderwidth =1, width = 20).pack(side = LEFT, fill = Y)
              Button(frame3, text = '评分', borderwidth =1, width = 20).pack(side = LEFT, fill = Y)
              Button(frame3, text = '剩余票数', borderwidth =1, width = 20).pack(side = LEFT, fill = Y)

              Button(frame3, borderwidth =1, width = 18).pack(side = LEFT, fill = Y)
              
              self.frame4 = Frame(root)
              self.frame4.pack(side = RIGHT, fill = Y)
              
              frame4 = self. frame4
              Button(frame4,text = '刷新', command = self.lbrefresh, width = 15).pack(pady = 5)
              Button(frame4,text = '修改', command = self.lbupdate, width = 15).pack(pady = 5)
              Button(frame4,text = '添加', command = self.insert, width = 15).pack(pady = 5)
              Button(frame4,text = '删除', command = self.lbdelete, width = 15).pack(pady = 5)

              self.frame5 = Frame(root)
              self.frame5.pack(fill = BOTH)

              frame5 = self.frame5
              sb = Scrollbar(frame5)
              sb.pack(side = RIGHT, fill = Y)
              self.lb = Listbox(frame5, yscrollcommand = sb.set)
              self.lb.pack(fill = BOTH)

              self.lbrefresh()
              
       def insert(self):
              root = Tk()
              MovieInsert(root = root, parent = self)
              
       def close(self):
              self.frame2.destroy()
              self.frame3.destroy()
              self.frame4.destroy()
              self.frame5.destroy()
              
       def lbdelete(self):
              tm = MovieTable()
              string = self.lb.get(ACTIVE)
              x = getlist(string)
              tm.movie_delete(x[0])
              self.lb.delete(ACTIVE)

       def lbrefresh(self):
              tm = MovieTable()
              tm.movie_print()
              List = tm.List
              self.lb.delete(0, END)
              for each in List:
                     self.lb.insert(END, each)

       def lbupdate(self):
              string = self.lb.get(ACTIVE)
              self.x = getlist(string)
              x = self.x
              root = Tk()
              MI = MovieInsert(root, self, x[0], x[1], x[2], x[3], x[4], x[5])
              MI.b.configure(command = MI.finish1)
              
       def select(self):
              self.lb.delete(0, END)
              t = [self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get(), self.e5.get(), self.e6.get()]
              self.e1.delete(0, END)
              self.e2.delete(0, END)
              self.e3.delete(0, END)
              self.e4.delete(0, END)
              self.e5.delete(0, END)
              self.e6.delete(0, END)
              tm = MovieTable()
              tm.movie_select(t)
              List = tm.List
              for each in List:
                     self.lb.insert(END, each)


              
class MovieInsert:
       def __init__(self, root, parent, str1 = '', str2 = '', str3 = '', str4 = '', str5 = '', str6 = ''):
              self.parent = parent
              self.root = root

              
              
              Label(root, text = '电影名:').grid(row = 0, column = 0, padx = 10, pady =10)
              Label(root, text = '类型:').grid(row = 1, column = 0, padx = 10, pady =10)
              Label(root, text = '时长:').grid(row = 2, column = 0, padx = 10, pady =10)
              Label(root, text = '日期:').grid(row = 3, column = 0, padx = 10, pady =10)
              Label(root, text = '评分:').grid(row = 4, column = 0, padx = 10, pady =10)
              Label(root, text = '剩余票数:').grid(row = 5, column = 0, padx = 10, pady =10)
              testCMD = self.root.register(self.test)
              
              self.e1 = Entry(root)
              self.e1.grid(row = 0, column = 1, padx = 10, pady =10)
              self.e1.insert(0, str1)
              self.e2 = Entry(root)
              self.e2.grid(row = 1, column = 1, padx = 10, pady =10)
              self.e2.insert(0, str2)
              self.e3 = Entry(root)
              self.e3.grid(row = 2, column = 1, padx = 10, pady =10)
              self.e3.insert(0, str3)
              self.e4 = Entry(root) 
              self.e4.grid(row = 3, column = 1, padx = 10, pady =10)
              self.e4.insert(0, str4)
              self.e5 = Entry(root) 
              self.e5.grid(row = 4, column = 1, padx = 10, pady =10)
              self.e5.insert(0, str5)
              self.e6 = Entry(root, validate = 'key' , validatecommand = (testCMD, '%P')) 
              self.e6.grid(row = 5, column = 1, padx = 10, pady =10)
              self.e6.insert(0, str6)
              
              self.b = Button(root, text = '完成', width = 10, command = self.finish0)
              self.b.grid(row = 6, column = 0, padx = 25)
              self.a = Button(root, text = '取消', width = 10, command = self.cancel)
              self.a.grid(row = 6, column = 1,padx = 25)

              self.l1 = Label(root, text = '电影名不能为空')
              self.l2 = Label(root, text = '类型不能为空')
              self.l3 = Label(root, text = '时长为空')
              self.l4 = Label(root, text = '日期不能为空')
              self.l5 = Label(root, text = '评分不能为空')
              self.l6 = Label(root, text = '剩余票数不能为空')
              self.List = [self.l1, self.l2, self.l3, self.l4, self.l5, self.l6]
              
       def finish0(self):
              tm = MovieTable()
              x = [self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get(), self.e5.get(), self.e6.get()]
              ck = check3(self.List, x)
              
              if ck == 0:
                     tm.movie_insert(x)
                     self.parent.lbrefresh()
                     self.root.destroy()
                     
       def finish1(self):
              tm = MovieTable()
              z = [self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get(), self.e5.get(), self.e6.get()]
              ck = check3(self.List, z)
              
              if ck == 0:
                     y = self.parent.x[0]
                     tm.movie_update(z, y)
                     self.parent.lbrefresh()
                     self.root.destroy()
                     
                     
       def cancel(self):
              self.root.destroy()
              
       def test(self, content):
              return check1(content)




