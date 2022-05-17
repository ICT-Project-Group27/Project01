
import os
import os.path
import re
from tkinter.constants import TRUE
class Judge:#获取文件后缀
    def __init__(self,file) :
        self.f=file
    def judge(self,file):
        suffix=os.path.splitext(file)[-1][1:]
        return (suffix)


class Open:
    def traverse(filepath):#删除空文件夹
        a = True
        files = os.listdir(filepath)
        for fi in files:#遍历
            fi_d = os.path.join(filepath, fi)
            if os.path.isdir(fi_d):#判断是否为文件夹
                if not os.listdir(fi_d):#如果为空
                    print("Please upload a non-empty folder")
                    a = False
                else:
                    print("The folder is opeaning")
            else:
                if os.path.getsize(fi_d)==0:#判断文件大小
                    print("Please upload non-empty file")
                else:
                    p = False
                    while p==False:
                        f=open(fi_d, 'r')
                        j=Judge(fi).judge(fi)
                        if j=="txt":
                            p=True
                            print(fi)
                            for i in f:
                                print(i)
                        else:
                            print("The system just can read .txt file")
                            p=True
                    f.close()
    if __name__ == '__main__':
        path = input("Road")
        traverse(path)


    #def read():
    #    p = False
    #    while p==False:
    #        n=input("Please input the folder road: ")   
    #    f=open(n, 'r')
    #    z=os.path.basename(n)#获取文件名
    #    j=Judge(z).judge(z)
    #    if j=="txt":
    #        p = True
    #        for i in f:
    #            print(i)
    #    else:
    #        print("Please input txt file")
    #f.close()
