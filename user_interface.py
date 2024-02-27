from tkinter import *
from u_open_1 import *
from u_open_2 import *
from u_open_3 import *
from test import center
class UInterface:
       def __init__(self, root, Uname = '王5'):
              self.Uname = Uname
              self.root = root
              self.root.title('用户购票系统')
              root.resizable(width = False, height = False)
              self.frame1 = Frame(root, relief = RAISED, borderwidth = 1)
              self.frame1.pack(side = LEFT, fill = Y, ipady = 100, ipadx = 20)

              frame1 = self.frame1
              Button(frame1, text = '购票', borderwidth = 1, command = self.open21).pack(fill = X)
              Button(frame1, text = '我的', borderwidth = 1, command = self.open22).pack(fill = X)
              Button(frame1, text = '修改信息', borderwidth = 1, command = self.open23).pack(fill = X)
              self.open1()
              
       def open21(self):
              try:
                     self.close()
              except:
                     pass
              self.open1()
       def open22(self):
              try:
                     self.close()
              except:
                     pass
              self.open2()
       def open23(self):
              try:
                     self.close()
              except:
                     pass
              self.open3()
       def open1(self):
              self.fm1 = Open1(self.root, self)
              
       def open2(self):
              self.fm2 = Open2(self.root, self)
              
       def open3(self):
              self.fm3 = Open3(self.root, self)
              pass
       def close1(self):
              self.fm1.close()
       def close2(self):
              self.fm2.close()
       def close3(self):
              self.fm3.close()
       def close(self):
              self.close1()
              self.close2()
              self.close3()
if __name__ == '__main__':
       root = Tk()
       UInterface(root,'王5')
