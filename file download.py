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


#class test:
#    def modifyip(tfile, deviceAddress):  # tfile为目标文件，deviceAddress为要查找的条件
#        desktop_path = 'E:\learning\itp1.1'  # 新创建的txt文件的存放路径
#        full_path = desktop_path + deviceAddress + '.txt'  # 以deviceAddress为文件名
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
#         modifyip('E:\learning\itp1.1\test.txt','test0')  # 在'C:/Users/JiajunHu/Desktop/log_4.txt'中查找'8akDIW5BSG0U'
#         print("have done")

#class Ddocx:
#    from docx import Document
#    doc = Document()                #以默认模板建立文档对象
#    doc = Document('a.docx')     # 读取a.docx文档，建立文档对象
#    from docx.shared import Inches,Pt
#    def chg_font(obj,fontname='微软雅黑',size=None):## 设置字体函数
#        obj.font.name = fontname
#        obj._element.rPr.rFonts.set(qn('w:eastAsia'),fontname)
#        if size and isinstance(size,Pt):
#            obj.font.size = size
#            distance = Inches(0.3)
#            sec = doc.sections[0]             # sections对应文档中的“节”
#            sec.left_margin = distance     # 以下依次设置左、右、上、下页面边距
#            sec.right_margin = distance
#            sec.top_margin = distance
#            sec.bottom_margin = distance
#            sec.page_width =Inches(12)        #设置页面宽度
#            sec.page_height = Inches(20)       #设置页面高度
#            ##设置默认字体
#            chg_font(doc.styles['Normal'],fontname='宋体')
#            ##添加段落文本
#            paragraph =doc.add_paragraph('text....')
#            ph_format =paragraph.paragraph_format
#            ph_format.space_before =Pt(10)     #设置段前间距
#            ph_format.space_after =Pt(12)       #设置段后间距
#            ph_format.line_spacing=Pt(19)       #设置行间距
#            ##如果希望同一段落中的文本格式不同，就需要使用Run对象(可以理解为可以单独设置格式的段落内对象)。
#            run = paragraph.add_run('text...')
#            run.bold = True #设置字体为粗体
#            chg_font(run,fontname='微软雅黑', size=Pt(12))  #设置字体和字号


#from pdfminer.converter import PDFPageAggregator
#from pdfminer.layout import LTTextBoxHorizontal, LAParams
#from pdfminer.pdfparser import PDFParser
#from pdfminer.pdfdocument import PDFDocument
#from pdfminer.pdfpage import PDFPage
#from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
#from pdfminer.pdfpage import PDFTextExtractionNotAllowed

#import logging

## 不显示warning
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

## 检测文档是否提供txt转换，不提供就忽略
#if not doc.is_extractable:
#    raise PDFTextExtractionNotAllowed
#else:
#    with open(txt_filename, 'w', encoding="utf-8") as fw:
#        print(1)
#        print("num page:{}".format(len(list(PDFPage.create_pages(doc)))))
#        for i, page in enumerate(PDFPage.create_pages(doc)):
#            interpreter.process_page(page)
#            # 接受该页面的LTPage对象
#            layout = device.get_result()
#            # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象
#            # 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等
#            # 想要获取文本就获得对象的text属性，
#            for x in layout:
#                if isinstance(x, LTTextBoxHorizontal):
#                    results = x.get_text()
#                    fw.write(results)


from fpdf import FPDF
import os
import re
class test:
    def txtToPdf():
        i = 1
        #以列表的方式打开所有txt文件的路径
        for filename in os.listdir("E:\learning\itp1.1\txt"):
            print("第%d开始" % i)
            pdf = FPDF()
            #读取字体文件
            pdf.add_font('fangzhengzhunyuan', '', 'fangzhengzhunyuan.TTF', True)
            pdf.add_page()
            #设置pdf字体大小
            pdf.set_font("fangzhengzhunyuan", size=12)
            #打开txt文本
            with open("E:\learning\itp1.1\txt" + filename, encoding='utf-8') as f:
                ms = re.sub(r'.txt', '.pdf', filename)
                try:
                    #按行读取txt文本内容
                    for line in f.readlines():
                        str=line
                        num=len(str)
                        temp=45#判断标志，实现pdf文件每行最多村45个字符
                        for j in range(0,num,temp):
                            if(j+temp<num):
                                data=str[j:j+temp]
                            else:
                                data=str[j:num]
                            pdf.cell(0, 5, data, ln=1)
                        f.close()
                except Exception as e:
                    print(e)
                print(ms)
                pdf.output("E:\learning\itp1.1\txt" + ms)
            print("第%d完成" % i)
            i = i + 1
    txtToPdf()