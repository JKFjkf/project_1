import tkinter
import time


def second_10():
    a = [0,1,2,3,4,5,6,7,8,9,10,]
    i = a[::-1]
    #print(i)

    for k in i :
        time.sleep(1)
        return k

def gettime():
      var.set(time.strftime("%H:%M:%S"))   # 获取当前时间
      root.after(1000,gettime)   # 每隔1s调用函数 gettime 自身获取时间

root = tkinter.Tk()
root.title('时钟')
var=tkinter.StringVar()

lb = tkinter.Label(root,textvariable=var,fg='black',font=("黑体",80))
lb.pack()
gettime()
#root.resizable(width=False,height=False)
second_10()
#root.attributes('-alpha',0.5)
root.mainloop()
