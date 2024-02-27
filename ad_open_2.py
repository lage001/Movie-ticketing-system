from tkinter import *
from UMsql import *
from test import *

class Open2:
       def __init__(self,root):
              self.frame2 = Frame(root,relief = RAISED, borderwidth = 1)
              self.frame2.pack(side = TOP, fill = X, ipadx = 100)
              frame2 = self.frame2

              Label(frame2, text = '用户名:').pack(side = LEFT)
              self.e1 = Entry(frame2)
              self.e1.pack(side = LEFT)
              Label(frame2, text = '手机号码:').pack(side = LEFT)
              self.e2 = Entry(frame2)
              self.e2.pack(side = LEFT)
              Label(frame2, text = '电影名:').pack(side = LEFT)
              self.e3 = Entry(frame2)
              self.e3.pack(side = LEFT)
              Label(frame2, text = '张数:').pack(side = LEFT)
              self.e4 = Entry(frame2)
              self.e4.pack(side = LEFT)
              
              Button(frame2, text = '搜索', width = 10, command = self.select).pack(side = LEFT)

              self.frame3 = Frame(root, relief = RAISED, borderwidth = 1)
              self.frame3.pack(side = TOP, fill = X)
              
              frame3 = self.frame3
              Button(frame3, text = '用户名', borderwidth =1, width = 20).pack(side = LEFT, fill = Y)
              Button(frame3, text = '手机号码', borderwidth =1, width = 20).pack(side = LEFT, fill = Y)
              Button(frame3, text = '电影名', borderwidth =1, width = 20).pack(side = LEFT, fill = Y)
              Button(frame3, text = '张数', borderwidth =1, width = 20).pack(side = LEFT, fill = Y)
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
              sb = Scrollbar(self.frame5)
              sb.pack(side = RIGHT, fill = Y)
              self.lb = Listbox(self.frame5, yscrollcommand = sb.set)
              self.lb.pack(fill = BOTH)

              self.lbrefresh()
       def insert(self):
              root = Tk()
              MI = UserInsert(root = root,parent = self)
       def close(self):
              self.frame2.destroy()
              self.frame3.destroy()
              self.frame4.destroy()
              self.frame5.destroy()
              
       def lbdelete(self):
              string = self.lb.get(ACTIVE)
              x = getlist(string)
              tm = UMTable()
              tm.um_delete(x)
              self.lb.delete(ACTIVE)

       def lbrefresh(self):
              tm = UMTable()
              tm.um_print()
              List = tm.List
              self.lb.delete(0, END)
              for each in List:
                     self.lb.insert(END, each)

       def lbupdate(self):
              string = self.lb.get(ACTIVE)
              self.x = getlist(string)
              x = self.x
              root = Tk()
              MI = UserInsert(root, self, x[0], x[1], x[2], x[3])
              MI.b.configure(command = MI.finish1)
              
       def select(self):
              self.lb.delete(0, END)
              t = [self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get()]
              self.e1.delete(0, END)
              self.e2.delete(0, END)
              self.e3.delete(0, END)
              self.e4.delete(0, END)
              tm = UMTable()
              tm.um_select(t)
              List = tm.List
              for each in List:
                     self.lb.insert(END, each)


              
class UserInsert:
       def __init__(self, root, parent,str1 = '', str2 = '', str3 = '', str4 = ''):
              self.parent = parent
              self.root = root
              Label(root, text = '用户名:').grid(row = 0, column = 0, padx = 10, pady =10)
              Label(root, text = '手机号码:').grid(row = 1, column = 0, padx = 10, pady =10)
              Label(root, text = '电影名:').grid(row = 2, column = 0, padx = 10, pady =10)
              Label(root, text = '张数:').grid(row = 3, column = 0, padx = 10, pady =10)
              
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

              self.b = Button(root, text = '完成',command = self.finish0)
              self.b.grid(row = 4, column = 0, padx = 25)
              self.a = Button(root, text = '取消', command = self.cancel, width = 10)
              self.a.grid(row = 4, column = 1,padx = 25)
              self.l1 = Label(root, text = '用户名不能为空')
              self.l2 = Label(root, text = '电话号码不能为空')
              self.l3 = Label(root, text = '电影名为空')
              self.l4 = Label(root, text = '票数不能为空')

              self.List = [self.l1, self.l2, self.l3, self.l4]
       def finish0(self):
              tm = UMTable()
              x = [self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get()]
              tm.um_insert(x)
              self.parent.lbrefresh()
              self.root.destroy()

       def finish1(self):
              tm = UMTable()
              z = [self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get()]
              ck = check3(self.List, z)
              if ck == 0:
                     y = self.parent.x
                     tm.um_update(z, y)
                     self.parent.lbrefresh()
                     self.root.destroy()

       def cancel(self):
              self.root.destroy()

       

