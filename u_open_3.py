from tkinter import *
from Usql import *
from test import *
from UMsql import *
class Open3:
       def __init__(self, root, parent):
              self.root = root
              self.parent = parent
              self.frame1 = Frame(root, relief = RAISED, borderwidth = 1)
              self.frame1.pack(side = LEFT, fill = Y, ipadx = 10)
              
              self.text1 = StringVar(root)
              self.text2 = StringVar(root)
              self.text3 = StringVar(root)
              
              self.l1 = Label(self.frame1, textvariable = self.text1)
              self.l1.pack(pady = 10)  
              self.l2 = Label(self.frame1, textvariable = self.text2)
              self.l2.pack(pady = 10)
              self.l3 = Label(self.frame1, textvariable = self.text3)
              self.l3.pack(pady = 10)
              
              self.Uname = self.parent.Uname
              self.refresh()

              Button(self.frame1, text = '修改基本信息', command = self.update).pack(fill = X, pady = 20)
              

       def update(self):
              root = Tk()
              uu = UserUpdate(root, self)
              
       def refresh(self):
              
              um = UserTable()
              um.users_select(self.Uname)
              self.Uphone = um.results[0][1]
              self.Ukey = um.results[0][2]
              
              
              self.text1.set('用户名:%s' % self.Uname)  
              self.text2.set('电话号吗:%s' %  self.Uphone)    
              self.text3.set('密码:%s' %  self.Ukey)
              self.parent.Uname = self.Uname
       def close(self):
              self.frame1.destroy()
              
class UserUpdate:
       def __init__(self, root, parent):
              self.root = root
              self.parent = parent
              Label(root, text = '用户名:').grid(row = 0, column = 0, padx = 10, pady =10)
              Label(root, text = '电话号:').grid(row = 1, column = 0, padx = 10, pady =10)
              Label(root, text = '密码:').grid(row = 2, column = 0, padx = 10, pady =10)

              self.e1 = Entry(root)
              self.e1.grid(row = 0, column = 1, padx = 10, pady =10)
              self.e1.insert(0, parent.Uname)
              self.e2 = Entry(root)
              self.e2.grid(row = 1, column = 1, padx = 10, pady =10)
              self.e2.insert(0, parent.Uphone)
              self.e3 = Entry(root)
              self.e3.grid(row = 2, column = 1, padx = 10, pady =10)
              self.e3.insert(0, parent.Ukey)
              
              self.b = Button(root, text = '完成', width = 10, command = self.finish)
              self.b.grid(row = 6, column = 0, padx = 25)
              self.a = Button(root, text = '取消', width = 10, command = self.cancel)
              self.a.grid(row = 6, column = 1,padx = 25)

              self.l1 = Label(root, text = '用户名不能为空')
              self.l2 = Label(root, text = '电话号码不能为空')
              self.l3 = Label(root, text = '密码不能为空')

              self.List = [self.l1, self.l2, self.l3]

       def finish(self):
              ut = UserTable()
              umt = UMTable()
              z = [self.e1.get(), self.e2.get(), self.e3.get()]
              ck = check3(self.List, z)
              
              if ck == 0:
                     y = self.parent.Uname
                     umt.um_update2([z[0],z[1], y])
                     ut.users_update(z, y)
                     self.parent.Uname = self.e1.get()
                     self.parent.refresh()
                     self.root.destroy()
              
       def cancel(self):
              self.root.destroy
