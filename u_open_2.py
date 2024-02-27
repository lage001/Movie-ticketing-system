from tkinter import *
from Usql import *
from UMsql import *
from Msql import *
from test import *

class Open2:
       def __init__(self, root, parent):
              self.root = root
              self.parent = parent
              self.frame1 = Frame(root, relief = RAISED, borderwidth = 1)
              self.frame1 .pack(side = TOP, fill = X, ipadx = 100)
              frame1 = self.frame1
              Label(frame1, text = '已购买').pack(pady = 5)

              self.frame2 = Frame(root, relief = RAISED, borderwidth = 1)
              self.frame2.pack(side = TOP, fill = X)
              
              frame2 = self.frame2
              Button(frame2, text = '电影名', borderwidth =1, width = 20).pack(side = LEFT, fill = Y)
              Button(frame2, text = '类型', borderwidth =1, width = 20).pack(side = LEFT, fill = Y)
              Button(frame2, text = '时长', borderwidth =1, width = 20).pack(side = LEFT, fill = Y)
              Button(frame2, text = '日期', borderwidth =1, width = 20).pack(side = LEFT, fill = Y)
              Button(frame2, text = '评分', borderwidth =1, width = 20).pack(side = LEFT, fill = Y)
              Button(frame2, text = '张数', borderwidth =1, width = 20).pack(side = LEFT, fill = Y)
              Button(frame2, borderwidth =1, width = 18).pack(side = LEFT, fill = Y)

              self.frame3 = Frame(root)
              self.frame3.pack(side = RIGHT, fill = Y)
              
              frame3 = self. frame3
              Button(frame3,text = '刷新', command = self.lbrefresh, width = 15).pack(pady = 5)
              self.bb = Button(frame3,text = '退票', command = self.lbrefund, width = 15)
              self.bb.pack(pady = 5)

              self.frame4 = Frame(root)
              self.frame4.pack(fill = BOTH)
              sb = Scrollbar(self.frame4)
              sb.pack(side = RIGHT, fill = Y)
              self.lb = Listbox(self.frame4, yscrollcommand = sb.set)
              
              self.lb.pack(fill = BOTH)
              self.lbrefresh()
              
       def close(self):
              self.frame1.destroy()
              self.frame2.destroy()
              self.frame3.destroy()
              self.frame4.destroy()
              
       def lbrefresh(self):
              tm = UserTable()
              print(self.parent.Uname)
              tm.select(self.parent.Uname)
              List = tm.List
              self.lb.delete(0, END)
              for each in List:
                     self.lb.insert(END, each)
              
       def lbrefund(self):
              string = self.lb.get(ACTIVE)
              x = getlist(string)
              um = UMTable()
              if int(x[5]) <= 1:
                     um.um_delete([self.parent.Uname, '', x[0]])
                     self.lbrefresh()
              else:
                     um.um_update1([int(x[5]) - 1, self.parent.Uname, x[0]])
                     m =  MovieTable()
                     m.movie_select([x[0], '', '', '', '', ''])
                     num = m.results[0][5]
                     m.movie_update1(num + 1, x[0])
                     self.lbrefresh()
