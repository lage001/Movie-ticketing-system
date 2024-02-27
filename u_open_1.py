from tkinter import *
from Msql import *
from UMsql import *
from user_interface import *
from Usql import *
class Open1:
       def __init__(self, root, parent):
              self.parent = parent
              
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
              self.bb = Button(frame4,text = '购买', command = self.lbbuy, width = 15)
              self.bb.pack(pady = 5)

              self.frame5 = Frame(root)
              self.frame5.pack(fill = BOTH)
              sb = Scrollbar(self.frame5)
              sb.pack(side = RIGHT, fill = Y)
              self.lb = Listbox(self.frame5, yscrollcommand = sb.set)
              
              self.lb.pack(fill = BOTH)
              self.lbrefresh()
              
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
       
       def lbrefresh(self):
              tm = MovieTable()
              tm.movie_print()
              List = tm.List
              self.lb.delete(0, END)
              for each in List:
                     self.lb.insert(END, each)
                     
       def lbbuy(self):
              
              string = self.lb.get(ACTIVE)
              x = getlist(string)
              if int(x[5]) == 0:
                     pass
              else:
                     tm = MovieTable()
                     y = int(x[5]) - 1
                     tm.movie_update1(y, x[0])
                     self.lbrefresh()
                     um = UMTable()
                     name = self.parent.Uname
                     try:
                            um.um_select([name, '', x[0], ''])
                            num = um.results[0][3]
                            um.um_update1([num + 1, name, x[0]])
                     except:
                            rm = UserTable()
                            rm.users_select(name)
                            phone = rm.results[0][1]
                            um.um_insert([name, phone, x[0], 1])
                    
                     
                     
       def close(self):
              self.frame2.destroy()
              self.frame3.destroy()
              self.frame4.destroy()
              self.frame5.destroy()
              
def getlist(string):
       List = string.split(' ')
       x = []
       for i in List:
              if i !='':
                     x.append(i)
       return x

if __name__ == '__main__':
       root = Tk()
       ui = UInterface(root)
       Open1(root, ui)
