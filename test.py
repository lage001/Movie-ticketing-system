def check1(content):
       if content=='':
              return True
       else:
              return content.isdigit()

def check2(content):
       if '\u4e00' <= content <= '\u9fff':
            return False
       else:
              return True
       
def check3(l, e):
       j = 0
       i = 0
       for each in e:
              if each.replace(' ', '') == '':
                     l[i].grid(row = i, column = 2, padx = 10, pady = 10)
                     j += 1
              else:
                     l[i].grid_forget()
              i += 1
       return j
       
def getlist(string):
       List = string.split(' ')
       x = []
       for i in List:
              if i !='':
                     x.append(i)
       return x

def center(root, width, height):
       screenwidth = root.winfo_screenwidth()
       screenheight = root.winfo_screenheight()
       size = "%dx%d+%d+%d" % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
       root.geometry(size)
