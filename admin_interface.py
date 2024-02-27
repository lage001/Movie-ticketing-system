from tkinter import *
from ad_open_1 import *
from ad_open_2 import *
from test import center
class AdInterface:
       def __init__(self, root):
              self.root = root
              root.title('电影系统管理')
              root.resizable(width = False, height = False)
              self.frame1 = Frame(root, relief = RAISED, borderwidth = 1)
              self.frame1.pack(side = LEFT, fill = Y, ipady = 100, ipadx = 20)

              frame1 = self.frame1
              Button(frame1, text = '电影信息', borderwidth = 1, command = self.open21).pack(fill = X)
              Button(frame1, text = '观众信息', borderwidth = 1, command = self.open22).pack(fill = X)
              
              self.open1()
              

       def open21(self):
              try:
                     self.close1()
                     self.close2()
              except:
                     pass
              self.open1()
              
       def open1(self):
              self.fm1 = Open1(self.root)
              
       def close1(self):
              self.fm1.close()

       def open22(self):
              try:
                     self.close1()
                     self.close2()
              except:
                     pass
              self.open2()
              
       def open2(self):
              self.fm2 = Open2(self.root)
              
       def close2(self):
              self.fm2.close()

       

if __name__ == '__main__':
       root = Tk()
       AdInterface(root)
