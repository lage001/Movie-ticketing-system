from tkinter import *
from login_interface import UserLogin

class Register:
       def __init__(self, root):
              List = ['用户名:', '手机号码:', '创建密码:', '确认密码:']
              i = 0
              for each in List:
                     Label(root, text = each, justify = LEFT).grid(row = i, column = 0,padx = 10, pady = 10, sticky = E)
                     i += 1
              for j in range(3):
                     Entry(root).grid(row = j, column = 1, padx = 10, pady = 10)

              e = Entry(root).grid(row = 3, column = 1, padx = 10, pady = 10)
              Button(root, text = '完成注册并登录', command = self.open_UserLogin).grid(columnspan = 3)
              
       def open_UserLogin(self):
                     root = Tk()
                     UserLogin(root)
