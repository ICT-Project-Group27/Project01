
import os
from tkinter.constants import TRUE
class Judge:#获取文件后缀
    def __init__(self,file) :
        self.f=file
    def judge(self,file):
        suffix=os.path.splitext(file)[-1][1:]
        return (suffix)

class Open:
    p = False
    while p==False:
        n=input("Please input the txt file road: ")
        f=open(n, 'r')
        z=os.path.basename(n)#获取文件名
        j=Judge(z).judge(z)
        if j=="txt":
            p = True
            for i in f:
                print(i)
        else:
            print("Please input txt file")
    f.close()
