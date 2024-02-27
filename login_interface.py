from tkinter import *
from Usql import *
from admin_interface import *
from user_interface import *
from test import *
class UserLogin:
       def __init__(self, root):
              self.root = root
              root.title('用户登录')
              
              self.v1 = StringVar()
              self.v2 = StringVar()
              Label(root,text = '账号:').grid(row = 0,column = 0,padx = 10,pady = 10)
              Label(root,text = '密码:').grid(row = 1,column = 0)
              self.e1 = Entry(root)
              self.e2 = Entry(root,show = '*')
              self.e1.grid(row = 0,column = 1)
              self.e2.grid(row = 1,column = 1)
              self.l1 = Label(root, textvariable = self.v1)
              self.l1.grid(row = 0, column = 2, padx = 10, pady = 10)
              self.l2 = Label(root, textvariable = self.v2)
              self.l2.grid(row = 1, column = 2, padx = 10, pady = 10)
              self.button1 = Button(root,text = '登录', command = self.check)
              self.button1.grid(row = 2,column = 0,sticky = W,padx = 10,pady = 10)
              Button(root,text = '注册', command = self.open_register).grid(row = 2,column = 1, sticky = E,padx = 10,pady =10)

              center(root, 320, 150)
              
              
       def check(self):
              if self.e1.get() == '':
                     self.v1.set('用户名不能为空！')
              else:
                     um = UserTable()
                     u = um.users_select(self.e1.get())
                     if u == False:
                            self.v1.set('')
                            if self.e2.get() == um.results[0][2]:
                                   self.v2.set('')
                                   self.open_UI(self.e1.get())
                                   self.root.destroy()
                            else:
                                   self.v2.set('密码错误')
                     else:
                            self.v1.set('用户不存在')

       
       def open_register(self):
              self.root.destroy()
              
              root = Tk()
              Register(root)
       def open_UI(self, string):
              root = Tk()
              ui = UInterface(root, string)
              
class AdminLogin:
       def __init__(self, root):
              self.root = root
              root.title('管理员登录')
              Label(root,text = '账号:').grid(row = 0,column = 0,padx = 10,pady = 10)
              Label(root,text = '密码:').grid(row = 1,column = 0,padx = 10)

              self.e1 = Entry(root)
              self.e2 = Entry(root,show = '*')
              self.e1.grid(row = 0,column = 2,padx =10)
              self.e2.grid(row = 1,column = 2,padx =10)

              Button(root,text = '登录',command = self.check).grid(row = 2,column = 0, padx = 10,pady = 10, sticky = W)
              Button(root, text="Quit", command = root.destroy).grid(row = 2,column = 2, padx = 10,pady =10, sticky = E)
              center(root, 219, 116)
       def check(self):
              if self.e1.get() != '杨亮':
                     Label(self.root, text = '用户名错误,请重新输入。').grid(columnspan = 3)
                     self.e1.delete(0, END)
              if self.e2.get() != '123456':
                     Label(self.root, text = '密码错误,请重新输入。').grid(columnspan = 3)
                     self.e2.delete(0, END)
              else:
                     self.root.destroy()
                     root = Tk()
                     AdInterface(root)
                     

class Register:
       def __init__(self, root):
              self.root = root
              root.title('用户注册')
              self.name_List = ['用户名', '手机号码', '创建密码', '确认密码']
              self.entry_List = []
              
              
              self.v = [StringVar(), StringVar(), StringVar(), StringVar()]
              v1 = StringVar()
              self.l = Label(self.root, textvariable = self.v[0])
              self.l.grid(row = 0, column = 2, padx = 10, pady = 10)
              i = 0
              for each in self.name_List:
                     Label(root, text = each + ':', justify = LEFT).grid(row = i, column = 0,padx = 10, pady = 10, sticky = E)              
                     if i >= 2:
                            e = Entry(root, show = '*')
                            self.entry_List.append(e)
                            e.grid(row = i, column = 1, padx = 10, pady = 10)
                     else:
                            e = Entry(root)
                            self.entry_List.append(e)
                            e.grid(row = i, column = 1, padx = 10, pady = 10)       
                     i += 1
              testCMD1 = self.root.register(self.test1)
              testCMD2 = self.root.register(self.test2)
              Button(root, text = '完成注册并登录', command = self.check).grid(row = 4, column = 0)
              Button(root, text = '取消', command = self.cancel).grid(row = 4, column = 1)
              self.entry_List[0].configure(validate = "focusout", validatecommand = self.test)
              self.entry_List[1].configure(textvariable = v1, validate = 'key', validatecommand = (testCMD1, '%P'))
              self.entry_List[2].configure(validate = 'key', validatecommand = (testCMD2, '%P'))
              self.entry_List[3].configure(validate = 'key', validatecommand = (testCMD2, '%P'))

              center(root, 380, 202)
       def check(self):
              j = 0
              for i in range(1,4):
                     self.v[i].set('') 
                     Label(self.root, textvariable = self.v[i]).grid(row = i, column = 2, padx = 10, pady = 10, sticky = W)
                     
              for i in range(4):
                     if self.entry_List[i].get() == '':
                            self.v[i].set('%s不能为空！' % self.name_List[i])
                            j += 1
       
              if self.entry_List[3].get() != self.entry_List[2].get():
                     self.v[3].set('两次输入不一样！')
                     j += 1
                     
              if self.v[0].get() != '':
                     j += 1
                     
              if j == 0:
                     table = UserTable()
                     x = [self.entry_List[0].get(), self.entry_List[1].get(), self.entry_List[2].get()]
                     table.users_insert(x)
                     self.cancel()
       def cancel(self):
              self.root.destroy()
              root = Tk()
              UserLogin(root)
       
       def test(self):
              um = UserTable()
              u = um.users_select(self.entry_List[0].get())
              if u == False:
                     self.v[0].set('用户已存在')
              else:
                     self.v[0].set('')
              return u
       
       def test1(self, content):
              return check1(content)
       
       def test2(self, content):
              return check2(content)
       

