
import os
import os.path

class Judge:#Split upload file suffix
    def __init__(self,file) :
        self.f=file
    def judge(self,file):
        suffix=os.path.splitext(file)[-1][1:]
        return (suffix)


class Open:
    def traverse(filepath):#Upload files in folder
        files = os.listdir(filepath)
        for fi in files:#traverse folder
            fi_d = os.path.join(filepath, fi)
            if os.path.isdir(fi_d):#Determine whether it is a folder
                if not os.listdir(fi_d):#Determine whether it is an empty folder
                    print("Please upload a non-empty folder")
                    a = False
                else:
                    print("The folder is opeaning")
            else:
                if os.path.getsize(fi_d)==0:#Determine file size
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

