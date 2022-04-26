import os
import sys
import string
#def getFile(file,model):
#    print("open file")
#    print(file)
#    print(model)
#def getProFile(path):
#    return os.listdir(path)
#def issTrue(outFile,s):
#    findStr1 = "LINE_COUNT_UPDATE INTEGER := 0;"
#    writeStr1 = "LINE_COUNT_ERROR INTEGER := 0; --错误数据XX条"
#    findStr2 = "DBMS_OUTPUT.PUT_LINE('处理完毕")"
#    writeStr2 = "DBMS_OUTPUT.PUT_LINE('错误数据['||LINE_COUNT_ERROR||']条.');"
#    findStr3 = "DBMS_OUTPUT.PUT_LINE('插入数据['||CUR_RESULT.INT_ID||']时发生异常...');"
#    writeStr3 = "LINE_COUNT_ERROR := LINE_COUNT_ERROR+1;"
#    findStr4 = "DBMS_OUTPUT.PUT_LINE('更新数据['||CUR_RESULT.INT_ID||']时发生异常...');"
#    if s.find(findStr1) != -1:
#        outFile.write(s)
#        outFile.write(writeStr1+"\n")
#    elif s.find(findStr2) != -1:
#        outFile.write(s)
#        outFile.write(writeStr2+"\n")
#    elif s.find(findStr3) != -1:
#        outFile.write(s)
#        outFile.write("\t\t\t\t"+writeStr3+"\n")
#    elif s.find(findStr4) != -1:
#        outFile.write(s)
#        outFile.write("\t\t\t\t"+writeStr3+"\n")
#    elif s.find("CS_OSLGIS") != -1:
#        outFile.write(s.replace("CS_OSLGIS","CQ_RMW"))
#    elif s.find("AND A.LONGITUDE >") != -1:
#        outFile.write("\t\t\tAND A.LONGITUDE IS NOT NULL\n\t\t\tAND A.LONGITUDE IS NOT NULL\n\t\t\tAND ROWNUM<2\n")
#    elif s.find(") LOOP") != -1:
#        outFile.write("\t\t) LOOP\n")
#    else:
#        outFile.write(s.replace("||')',2","||')',3"))
#def getAndProc(inFileIns,outFileIns):
#    lines = inFileIns.readlines()
#    for s in lines:
#        #print(s)
#        isTrue(outFileIns,s)
#        if __name__=="__main__":
#            inFileMod = "r"
#            outFileMod = "w"
#            path = "D:\\rmsdata2gis"
#            for tmpFile in os.listdir(path):
#                inFilePath = path+"\\"+tmpFile
#                outFilePath = path+"\\BAK_"+tmpFile
#                inFileIns = getFileIns(inFilePath,inFileMod)
#                outFileIns = getFileIns(outFilePath,outFileMod)
#                getAndProc(inFileIns,outFileIns)
#                inFileIns.close()
#                outFileIns.close()


class test:
    def modifyip(tfile, deviceAddress):  # tfile为目标文件，deviceAddress为要查找的条件
        desktop_path = 'E:\learning\itp1.1'  # 新创建的txt文件的存放路径
        full_path = desktop_path + deviceAddress + '.txt'  # 以deviceAddress为文件名
        try:
            lines = open(tfile, 'r', encoding='utf-8').readlines()
            flen = len(lines) - 1
            print(flen)
            for i in range(flen):
                if deviceAddress in lines[i]:
                    file = open(full_path, 'a')
                    file.write(lines[i - 5] + "\n" +lines[i - 4] + "\n" + lines[i - 3]+ "\n" + lines[i] + "\n" + lines[i + 4])
                    except Exception as e:
                        print(e)
     if __name__=="__main__":
         modifyip('E:\learning\itp1.1\test.txt','test0')  # 在'C:/Users/JiajunHu/Desktop/log_4.txt'中查找'8akDIW5BSG0U'
         print("have done")

