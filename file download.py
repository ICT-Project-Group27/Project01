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
#    writeStr1 = "LINE_COUNT_ERROR INTEGER := 0; --��������XX��"
#    findStr2 = "DBMS_OUTPUT.PUT_LINE('�������")"
#    writeStr2 = "DBMS_OUTPUT.PUT_LINE('��������['||LINE_COUNT_ERROR||']��.');"
#    findStr3 = "DBMS_OUTPUT.PUT_LINE('��������['||CUR_RESULT.INT_ID||']ʱ�����쳣...');"
#    writeStr3 = "LINE_COUNT_ERROR := LINE_COUNT_ERROR+1;"
#    findStr4 = "DBMS_OUTPUT.PUT_LINE('��������['||CUR_RESULT.INT_ID||']ʱ�����쳣...');"
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
    def modifyip(tfile, deviceAddress):  # tfileΪĿ���ļ���deviceAddressΪҪ���ҵ�����
        desktop_path = 'E:\learning\itp1.1'  # �´�����txt�ļ��Ĵ��·��
        full_path = desktop_path + deviceAddress + '.txt'  # ��deviceAddressΪ�ļ���
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
         modifyip('E:\learning\itp1.1\test.txt','test0')  # ��'C:/Users/JiajunHu/Desktop/log_4.txt'�в���'8akDIW5BSG0U'
         print("have done")

