from login_interface import *
from tkinter import *
from test import center
class Main:
       def __init__(self,root):
              self.root = root
              root.title('电影系统主界面')
              Button(root,text = '管理员登录', command = self.open_window_1).pack(padx = 20, pady = 20,anchor = CENTER)
              Button(root,text = '用户登录', command = self.open_window_2).pack(padx = 20, pady = 20,anchor =CENTER)
              
              center(root, 320, 160)
              root.mainloop()
       def open_window_1(self):
              self.root.destroy()
              root = Tk()
              AdminLogin(root)
              
       
       def open_window_2(self):
              self.root.destroy()
              root = Tk()
              UserLogin(root)

if __name__ == '__main__':
       root = Tk()
       Main(root)

