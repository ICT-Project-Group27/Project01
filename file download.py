import os
import sys
import string
import io
#def getFile(file,model):
#    print("open file")
#    print(file)
#    print(model)
#def getProFile(path):
#    return os.listdir(path)
#def issTrue(outFile,s):
#    findStr1 = "LINE_COUNT_UPDATE INTEGER := 0;"
#    writeStr1 = "LINE_COUNT_ERROR INTEGER := 0; --????????XX??"
#    findStr2 = "DBMS_OUTPUT.PUT_LINE('????????")"
#    writeStr2 = "DBMS_OUTPUT.PUT_LINE('????????['||LINE_COUNT_ERROR||']??.');"
#    findStr3 = "DBMS_OUTPUT.PUT_LINE('????????['||CUR_RESULT.INT_ID||']??????????...');"
#    writeStr3 = "LINE_COUNT_ERROR := LINE_COUNT_ERROR+1;"
#    findStr4 = "DBMS_OUTPUT.PUT_LINE('????????['||CUR_RESULT.INT_ID||']??????????...');"
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


#class test:
#    def modifyip(tfile, deviceAddress):  # tfile????????????deviceAddress??????????????
#        desktop_path = 'E:\learning\itp1.1'  # ????????txt??????????????
#        full_path = desktop_path + deviceAddress + '.txt'  # ??deviceAddress????????
#        try:
#            lines = open(tfile, 'r', encoding='utf-8').readlines()
#            flen = len(lines) - 1
#            print(flen)
#            for i in range(flen):
#                if deviceAddress in lines[i]:
#                    file = open(full_path, 'a')
#                    file.write(lines[i - 5] + "\n" +lines[i - 4] + "\n" + lines[i - 3]+ "\n" + lines[i] + "\n" + lines[i + 4])
#                    except Exception as e:
#                        print(e)
#    if __name__=="__main__":
#         modifyip('E:\learning\itp1.1\test.txt','test0')  # ??'C:/Users/JiajunHu/Desktop/log_4.txt'??????'8akDIW5BSG0U'
#         print("have done")

#class Ddocx:
#    from docx import Document
#    doc = Document()                #??????????????????????
#    doc = Document('a.docx')     # ????a.docx??????????????????
#    from docx.shared import Inches,Pt
#    def chg_font(obj,fontname='????????',size=None):## ????????????
#        obj.font.name = fontname
#        obj._element.rPr.rFonts.set(qn('w:eastAsia'),fontname)
#        if size and isinstance(size,Pt):
#            obj.font.size = size
#            distance = Inches(0.3)
#            sec = doc.sections[0]             # sections??????????????????
#            sec.left_margin = distance     # ??????????????????????????????????
#            sec.right_margin = distance
#            sec.top_margin = distance
#            sec.bottom_margin = distance
#            sec.page_width =Inches(12)        #????????????
#            sec.page_height = Inches(20)       #????????????
#            ##????????????
#            chg_font(doc.styles['Normal'],fontname='????')
#            ##????????????
#            paragraph =doc.add_paragraph('text....')
#            ph_format =paragraph.paragraph_format
#            ph_format.space_before =Pt(10)     #????????????
#            ph_format.space_after =Pt(12)       #????????????
#            ph_format.line_spacing=Pt(19)       #??????????
#            ##????????????????????????????????????????????Run????(??????????????????????????????????????)??
#            run = paragraph.add_run('text...')
#            run.bold = True #??????????????
#            chg_font(run,fontname='????????', size=Pt(12))  #??????????????


#from pdfminer.converter import PDFPageAggregator
#from pdfminer.layout import LTTextBoxHorizontal, LAParams
#from pdfminer.pdfparser import PDFParser
#from pdfminer.pdfdocument import PDFDocument
#from pdfminer.pdfpage import PDFPage
#from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
#from pdfminer.pdfpage import PDFTextExtractionNotAllowed

#import logging

## ??????warning
#logging.propagate = False
#logging.getLogger().setLevel(logging.ERROR)

#pdf_filename = "1.pdf"
#txt_filename = "out.txt"

#device = PDFPageAggregator(PDFResourceManager(), laparams=LAParams())
#interpreter = PDFPageInterpreter(PDFResourceManager(), device)


#parser = PDFParser(open(pdf_filename, 'rb'))
#doc = PDFDocument(parser,'')
#parser.set_document(doc)
## doc.set_parser(parser)
## doc.initialize()

## ????????????????txt??????????????????
#if not doc.is_extractable:
#    raise PDFTextExtractionNotAllowed
#else:
#    with open(txt_filename, 'w', encoding="utf-8") as fw:
#        print(1)
#        print("num page:{}".format(len(list(PDFPage.create_pages(doc)))))
#        for i, page in enumerate(PDFPage.create_pages(doc)):
#            interpreter.process_page(page)
#            # ????????????LTPage????
#            layout = device.get_result()
#            # ????layout??????LTPage???? ?????????? ????page????????????????
#            # ????????LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal ????
#            # ????????????????????????text??????
#            for x in layout:
#                if isinstance(x, LTTextBoxHorizontal):
#                    results = x.get_text()
#                    fw.write(results)
import colorama
from fpdf import FPDF
import os
import re
import numpy as np
import linecache
class download:

    # def txtToPdf():
    #     i = 1
    #     #????????????????????txt??????????
    #     for filename in os.listdir("E:\learning\itp1.1\txt"):
    #         print("??%d????" % i)
    #         pdf = FPDF()
    #         #????????????
    #         pdf.add_font('fangzhengzhunyuan', '', 'fangzhengzhunyuan.TTF', True)
    #         pdf.add_page()
    #         #????pdf????????
    #         pdf.set_font("fangzhengzhunyuan", size=12)
    #         #????txt????
    #         with open("E:\learning\itp1.1\txt" + filename, encoding='utf-8') as f:
    #             ms = re.sub(r'.txt', '.pdf', filename)
    #             try:
    #                 #????????txt????????
    #                 for line in f.readlines():
    #                     str=line
    #                     num=len(str)
    #                     temp=45#??????????????pdf??????????????45??????
    #                     for j in range(0,num,temp):
    #                         if(j+temp<num):
    #                             data=str[j:j+temp]
    #                         else:
    #                             data=str[j:num]
    #                         pdf.cell(0, 5, data, ln=1)
    #                     f.close()
    #             except Exception as e:
    #                 print(e)
    #             print(ms)
    #             pdf.output("E:\learning\itp1.1\txt" + ms)
    #         print("??%d????" % i)
    #         i = i + 1
    # txtToPdf()

    from colorama import Fore, Back, Style
    # ????txt??
    def text_create(name):
        # ????????
        desktop_path = os.path.join(os.path.expanduser('~'), "Desktop/")
        full_path = desktop_path + name + '.txt'
        return full_path



    def data_matrix(filename):
        file = open(filename,"r")
        row = file.readlines()
        print(row)
        l = []
        for line in row:
            str = list(line.rstrip())
            l.append(str)
        print(l)
        return l

    def text_write(filename, matrixname, searchmatri):
        row = np.array(matrixname).shape[0] #???
        col = np.array(matrixname).shape[1] #???

        rows = np.array(searchmatri).shape[0] #???
        cols = np.array(searchmatri).shape[1] #???

        with open(filename,'w') as f:
            for i in range(0,row): #?????
                n = 0 #Mark
                Frame = matrixname[i]


                for j in range(0,col): #????????
                    Num = str(Frame[j])
                    f.write(Num)

                for si in range(0,rows): #?????
                    sFrame = searchmatri[si]

                    for sj in range(0,cols-1): #????????
                        sNum = int(sFrame[sj])
                        if i == sNum:
                            if n == 0: #??????
                                f.write("   # The duplicate code is: ")
                                n += 1
                            sj = sj+1
                            dNum = int(sFrame[sj]) #get?????
                            endNum = str(Frame[dNum]) #get???
                            f.write(endNum)
                f.write("\n")
            f.close


    a = text_create("new")
    b = data_matrix(input("road"))
    text_write(a,b,[[0,1],[0,4],[1,3],[1,4],[2,0],[2,4]])

