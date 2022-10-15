#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat April  5 23:36:17 2022

@author: Ghee, Zexi
"""
# importing tkinter gui
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, OptionMenu
from tkmacosx import Button
from tkinter.filedialog import askdirectory
from PIL import Image, ImageTk
import sys
import os
import inspect
import similarity_algorithm
import downloadFinal
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class UserInterface(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Plagiarism Checker")
        self.geometry('750x600')
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", lambda: UserInterface.on_closing(self))
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        self.sideBarContainer = tk.Frame(self)
        self.sideBarContainer.pack(side="left", fill="both", expand=0)
        self.mainContainer = tk.Frame(self)
        self.mainContainer.pack(side="right", fill="both", expand=1)
        self.mainContainer.grid_rowconfigure(0, weight=1)
        self.mainContainer.grid_columnconfigure(0, weight=1)
        self.sideBar()
        self.frames = {}

        page_name = MainPage.__name__
        frame = MainPage(parent=self.mainContainer)
        self.frames[page_name] = frame

        # put all of the pages in the same location;
        # the one on the top of the stacking order
        # will be the one that is visible.
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainPage")

    def show_frame(self, page_name):
        # Show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()

    def on_closing(self):
        if messagebox.askyesno("Quit", "Do you want to quit?"):
            self.destroy()
            self.quit()

    def sideBar(self):
        global btnState
        btnState = False
        global min_w
        min_w = 45  # Minimum width of the frame
        global max_w
        max_w = 120  # Maximum width of the frame
        global cur_width
        cur_width = min_w  # Increasing width of the frame
        global expanded
        expanded = False  # Check if it is completely expanded


        self.update()  # For the width to get updated

        sid_bar_frame = tk.Frame(self.sideBarContainer, bg="#191970", width=110, height=self.winfo_height())
        sid_bar_frame.pack(side=tk.LEFT)

        # Make the buttons with the icons to be shown
        menu_b = Button(sid_bar_frame,
            text="Welcome",
            bg="#191970",
            bordercolor="#191970",
            fg="white",
            width=90,
            bd=5,

                )

        home_b = Button(sid_bar_frame,
            text="Upload",
            bg="#191970",
            fg="white",
            width=90,
            bd=4,
            relief="flat",
            command=lambda: self.show_frame("MainPage"))


        info_b = Button(sid_bar_frame,
            text="Help",
            bg="#191970",
            fg="white",
            width=90,
            bd=4,
            relief="flat",
            command=lambda: self.infoButtonFunc())





        # Put them on the frame
        menu_b.grid(row=0, column=0, padx=1, pady=10)
        home_b.grid(row=1, column=0, padx=5, pady=30)
        info_b.grid(row=4, column=0, padx=5, pady=30)



        # So that it does not depend on the widgets inside the frame
        sid_bar_frame.grid_propagate(False)

    def infoButtonFunc(self):
        from tkinter import Text as txt
        from tkinter import Scrollbar as scroll

        top = tk.Toplevel(
            master=self,
            width=self.winfo_width(),
            height=self.winfo_height(),
        )
        top.title("help")

        top_side_frame = tk.Frame(
            top,
            bg="#191970",
            width=200,
            height=self.winfo_height(),
        )

        # So that it does not depend on the widgets inside the frame
        top_side_frame.grid_propagate(False)

        # button
        Description_and_introduction_b = tk.Button(
            top_side_frame,
            text="Description and introduction    ",
            bg="#D7E4F0",
            fg="black",
            width=25,
            relief="flat",
            command=lambda: switch_text("description.txt"),
        )

        Function_is_introduced_b = tk.Button(
            top_side_frame,
            text="Function and introduced  ",
            bg="#D7E4F0",
            fg="black",
            width=25,
            relief="flat",
            command=lambda: switch_text("func.txt"),
        )
        Support_b = tk.Button(
            top_side_frame,
            text="Support",
            bg="#D7E4F0",
            fg="black",
            width=25,
            relief="flat",
            command=lambda: switch_text("support.txt"),
        )
        Other_b = tk.Button(
            top_side_frame,
            text="Other",
            bg="#D7E4F0",
            fg="black",
            width=25,
            relief="flat",
            command=lambda: switch_text("other.txt"),
        )

        Description_and_introduction_b.grid(
            row=0,
            column=0,
            padx=5,
            pady=10,
        )
        Function_is_introduced_b.grid(
            row=1,
            column=0,
            padx=5,
            pady=30,
        )
        Support_b.grid(
            row=2,
            column=0,
            padx=5,
            pady=10,
        )
        Other_b.grid(
            row=3,
            column=0,
            padx=5,
            pady=30,
        )

        top_main = tk.Frame(
            top,
            bg="#F5F5F5",
            width=self.winfo_width() - 200,
            height=(self.winfo_height()),
        )

        def switch_text(file):
            show_data_area.delete(1.0, "end")
            with open(file, "r", encoding="utf-8") as read_p:
                line = read_p.readline()
                while line:
                    update_text(line.strip("\n"), show_data_area)
                    line = read_p.readline()

        def update_text(result, txt):
            txt.insert(tk.END, result + "\n")
            txt.update()

        s1 = scroll(top_main)

        show_data_area = txt(
            master=top_main,
            height=30,
            font=("Helvetica", 12),
            yscrollcommand=s1.set,
        )

        s1.config(command=show_data_area.yview)
        s1.pack(side=tk.RIGHT, fill=tk.Y, pady=(15, 15))
        show_data_area.pack(fill=tk.BOTH, padx=(1, 0), pady=(15, 15))

        top_main.grid_propagate(False)

        top_side_frame.pack(side=tk.LEFT)
        top_main.pack(side=tk.RIGHT)

        switch_text("description.txt")

        # Display until closed manually.
        top.mainloop()



class MainPage(tk.Frame):
    global names
    names = []
    global trans
    trans = []
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    global parentdir
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0, parentdir)
    global folderPath
    folderPath = None
    global transferDicList
    transferDicList = None

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        container = tk.Frame(self, bg="#F5F5F5")
        container.pack(side="right", fill="both", expand=True)

        topFrame = tk.Frame(container, bg='#F5F5F5', width=container.winfo_width(),
                            height=container.winfo_height() / 5 * 3)
        topFrame.pack(side=tk.TOP, fill="both", expand=1)
        middleFrame = tk.Frame(container,bg='#F5F5F5', width=container.winfo_width(),
                               height=container.winfo_height() / 5 * 1)
        middleFrame.pack(side=tk.TOP, expand=1)
        botFrame = tk.Frame(container, bg='#F5F5F5', width=container.winfo_width(),
                            height=container.winfo_height() / 5 * 2)
        botFrame.pack(side=tk.BOTTOM, fill="x", expand=1)

        # dropdown box
        stater = tk.IntVar()
        stater.set(0)

        def changeCode():
            #change code message
            num = stater.get()
            if num == 1:
                messagebox.askyesno(title='Attention', message="Please upload Python files")
            elif num == 2:
                messagebox.askyesno(title='Attention', message="Please upload Java files")
            elif num == 3:
                messagebox.askyesno(title='Attention', message="Pleas upload C++ files")
            elif num == 4:
                messagebox.askyesno(title='Attention', message="Pleas upload PHP files")
            elif num == 5:
                messagebox.askyesno(title='Attention', message="Pleas upload C files")
            elif num == 6:
                messagebox.askyesno(title='Attention', message="Pleas upload SQL files")

        #code change button
        dropDownFrame = tk.Frame(middleFrame, bg='#F5F5F5', width=100,
                                 height=5)
        dropDownFrame.pack(side=tk.TOP)
        codeButton1 = tk.Radiobutton(dropDownFrame, text='Python', variable=stater, value=1,
                                   command=changeCode)
        codeButton1.grid(column=0, row=4)
        codeButton2 = tk.Radiobutton(dropDownFrame, text='Java', variable=stater, value=2,
                                   command=changeCode)
        codeButton2.grid(column=1, row=4)
        codeButton3 = tk.Radiobutton(dropDownFrame, text='C++', variable=stater, value=3,
                                   command=changeCode)
        codeButton3.grid(column=2, row=4)
        codeButton4 = tk.Radiobutton(dropDownFrame, text='PHP', variable=stater, value=4,
                                   command=changeCode)
        codeButton4.grid(column=3, row=4)
        codeButton5 = tk.Radiobutton(dropDownFrame, text='C', variable=stater, value=5,
                                   command=changeCode)
        codeButton5.grid(column=4, row=4)
        codeButton6 = tk.Radiobutton(dropDownFrame, text='SQL', variable=stater, value=6,
                                   command=changeCode)
        codeButton6.grid(column=5, row=4)




        # listBox and upload button

        listBoxFrame = tk.Frame(topFrame, bg='#F5F5F5', width=100,
                                height=60)
        listBoxFrame.grid(column=0, row=3, padx=10, columnspan=2)
        studentWork = tk.Label(topFrame, text='\n\nStudent Files:\n\n', bg='#F5F5F5', fg='black', font=(0, 20))
        studentWork.grid(column=0, row=1, padx=10, columnspan=2)
        self.listBox = tk.Listbox(listBoxFrame, bg='white', fg='black', width=66)
        self.listBox.grid(column=0, row=1, padx=10, columnspan=2, rowspan=2)
        selection = Button(dropDownFrame, highlightbackground='#F5F5F5', text="Folder", width=60, bg='white',
                                command=lambda: self.openFile())
        selection.grid(column=2, row=0, rowspan=2)





        # button for start\cancel plagiarism check
        check = Button(botFrame, bg='#00FF7F', text="Confirm", fg="black", width=90,
                            command=lambda: self.checkFile(stater.get()))
        check.pack(side=tk.RIGHT, padx=50)

        cancel = Button(botFrame, bg="#FF0000", text="Cancel", fg="black", width=90,
                             command=lambda: self.cancelFile())
        cancel.pack(side=tk.LEFT, padx=50,)


    def checkFile(self, stater):
        global folderPath
        global transferDicList
        if folderPath is None:
            messagebox.showerror(title='Warning', message="Please a folder / files.")
        else:
            messagebox.showinfo(title="Report Generation", message="Plagiarism Result has been generated")
            if (stater == 1):
                transferDicList = similarity_algorithm.check_python(folderPath)
            elif (stater == 2):
                transferDicList = similarity_algorithm.check_java(folderPath)
            elif (stater == 3):
                transferDicList = similarity_algorithm.check_cpp(folderPath)
            elif (stater == 4):
                transferDicList = similarity_algorithm.check_PHP(folderPath)
            elif (stater == 5):
                transferDicList = similarity_algorithm.check_C(folderPath)
            elif (stater == 6):
                transferDicList = similarity_algorithm.check_sql(folderPath)
            self.repage()



    def transferList(self):
        #Declare global variables and pass parameters to result
        global transferDicList
        return transferDicList




    def openFile(self):
        global folderPath
        from tkinter import filedialog as fd
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )

        folderPath = fd.askdirectory() + '/'
        self.updateListBox()

    def cancelFile(self):
        #Cancel uploaded file
        global  folderPath
        #similarity_algorithm.deletFile()
        folderPath = None
        self.listBox.delete(0, tk.END)

    def tansFloder(self):
        global folderPath
        return folderPath

    def updateListBox(self):
        global names
        global trans #Global variables store uploaded files (Prevent redundant parameter input)
        self.listBox.delete(0, tk.END)
        names = similarity_algorithm.walk_dir(folderPath)
        print(names)
        names = [names[0][0:]]
        for i in names:
            for x in i:
                if not x.startswith("."):
                    self.listBox.insert(tk.END, x)
                    trans.append(x)

    def repage(self):
        global filename
        filename = None


        # setting frame
        Top = tk.Toplevel(self)
        Top.resizable(False, False)
        Top.geometry('700x600')

        container = tk.Frame(Top, bg="#F5F5F5")
        container.pack(side="right", fill="both", expand=True)

        topFrame = tk.Frame(container, bg='#F5F5F5', width=container.winfo_width(),
                            height=(container.winfo_height() / 5 * 4))
        topFrame.pack(side=tk.TOP, fill="both", expand=1)
        botFrame = tk.Frame(container, bg='#F5F5F5', width=container.winfo_width(),
                            height=(container.winfo_height() / 5 * 1))
        botFrame.pack(side=tk.BOTTOM, fill="x", expand=1)

        tittleFrame = tk.Frame(topFrame, bg='#F5F5F5', width=100,
                               height=30)
        tittleFrame.pack(side=tk.TOP)
        studentWork_l = tk.Label(tittleFrame, text='\nResult:\n\n', bg='#F5F5F5', fg='black', font=(0, 30))
        studentWork_l.grid(column=0, row=0, padx=30)

        # setting treeview

        listBoxFrame = tk.Frame(topFrame, bg='#F5F5F5', width=80,
                                height=60)
        listBoxFrame.pack(side=tk.TOP)
        colums = ['File Name', 'Rate']  # the treeview head setting
        self.resultListBox = ttk.Treeview(listBoxFrame, columns=colums, show='headings', heigh=10)
        self.resultListBox.grid(column=1, row=1, padx=20, columnspan=2)
        self.resultListBox.heading('File Name', text='File Name', )
        self.resultListBox.heading('Rate', text='Rate', )
        self.resultListBox.column('File Name', width=250)
        self.resultListBox.column('Rate', width=140)

        # setting defferent rate to different color
        self.resultListBox.tag_configure('tag_green',
                                         foreground='green')
        self.resultListBox.tag_configure('tag_origin',
                                         foreground='orange')
        self.resultListBox.tag_configure('tag_red',
                                         foreground='red')

        # button for show result and show report
        check = Button(botFrame, bg='#00FF7F', text="Show report", fg="black", width=100,
                       command=lambda: self.clickReport())
        check.pack(side=tk.RIGHT, padx=50)
        result = Button(botFrame, bg="#191970", text="Download all report", fg="white", width=150,
                        command=lambda: self.creatPathSMui())
        result.pack(side=tk.LEFT, padx=50)
        self.path = tk.StringVar()  # store user want path



        thisDict = MainPage.transferList(self=MainPage)  # get the result
        if thisDict is None:
            messagebox.showerror(title='Warning', message="No Result")
        else:
            resultList = thisDict[0]  # get the file and rate(dic)
            i = 0
            my_list = []
            for row in self.resultListBox.get_children():
                # initialization treeview
                self.resultListBox.delete(row)
            for key, val in resultList.items():
                newCalue1 = float(resultList[key])  # get the result rate
                newCalue2 = newCalue1 * 100
                newCalue3 = float('%.2f' % newCalue2)
                newvalue = str(newCalue3) + "%"
                my_list.append((key, newvalue))  # add file name and rate to the new list
            for value in my_list:
                new1 = value[1].strip("%")  # throw the %
                new2 = float(new1)
                # Determine repetition rate and add color
                if new2 <= 20:
                    tag = 'tag_green'
                elif new2 > 50:
                    tag = 'tag_red'
                else:
                    tag = 'tag_origin'
                self.resultListBox.insert(parent='', index=i, iid=i, values=value, tags=tag)
                i += 1

    def show_selected(self):
        # get user selection
        global filename
        # messagebox.showinfo(title="Report Generation", message="Please click Preview on the Report page to view the report")
        for item in self.resultListBox.selection():  # get selection
            item_text = self.resultListBox.item(item, "values")  # get the filename and rate
            filename = item_text[0]  # get the name
        return filename

    def clickReport(self):
        if self.show_selected() is None:
            messagebox.showerror(title='Warning', message="Please a choice file.")
        else:
            self.report()

    def report(self):
        # add a new window
        Top = tk.Toplevel(self)
        Top.resizable(False, False)
        Top.geometry('700x600')

        container = tk.Frame(Top, bg="#F5F5F5")
        container.pack(side="right", fill="both", expand=True)

        topFrame = tk.Frame(container, bg='#F5F5F5', width=container.winfo_width(),
                            height=(container.winfo_height() / 5 * 1))
        topFrame.pack(side=tk.TOP, fill="both", expand=1)
        botFrame = tk.Frame(container, bg='#F5F5F5', width=container.winfo_width(),
                            height=(container.winfo_height() / 5 * 1))
        botFrame.pack(side=tk.BOTTOM, fill="x", expand=1)

        tittleFrame = tk.Frame(topFrame, bg='#F5F5F5', width=100,
                               height=30)
        tittleFrame.pack(side=tk.TOP)
        listBoxFrame = tk.Frame(topFrame, bg='#F5F5F5', width=100,
                                height=100)
        listBoxFrame.pack(side=tk.BOTTOM)

        studentWork_l = tk.Label(tittleFrame, text='\nReport:', bg='#F5F5F5', fg='black', font=(0, 30))
        studentWork_l.grid(column=0, row=0, padx=30)

        # set scrollbar
        scrolly = tk.Scrollbar(listBoxFrame)
        scrolly.pack(side=tk.RIGHT, fill=tk.Y)

        scrollx = tk.Scrollbar(listBoxFrame, orient=tk.HORIZONTAL)
        scrollx.pack(side=tk.BOTTOM, fill=tk.X)

        # set textbox and link scrollbar
        self.listBox = tk.Text(listBoxFrame, wrap='none')
        self.listBox.pack(fill=tk.BOTH, expand=tk.YES)
        self.listBox.config(yscrollcommand=scrolly.set)
        self.listBox.config(xscrollcommand=scrollx.set)
        scrolly.config(command=self.listBox.yview)
        scrollx.config(command=self.listBox.xview)

        singleReportButton = Button(botFrame, bg='#191970', text="Download this report", fg="white", width=150,
                                    command=lambda: self.creatPathSin())
        singleReportButton.pack(side=tk.RIGHT, padx=50)

        mutiReport = Button(botFrame, bg="#191970", text="Download all report", fg="white", width=150,
                            command=lambda: self.creatPathSMui())
        mutiReport.pack(side=tk.LEFT, padx=50)

        self.listBox.bind('<KeyPress>', lambda e: 'break')  # Limit user input
        self.path = tk.StringVar()  # store user want path

        global filename
        thisName = self.show_selected()  # get uesr selection
        reportResult = MainPage.transferList(self=MainPage)  # get result
        folderPath = MainPage.tansFloder(self=MainPage)
        l = downloadFinal.download.trans(folderPath, trans, thisName, reportResult)[0]  # get report content
        self.listBox.delete("1.0", "end")  # clear textbox

        for i in range(0, len(l)):
            # set color
            a = float(i+1)
            self.listBox.tag_add('warning', a)
            self.listBox.tag_configure('warning',
                                       foreground='red')
            self.listBox.tag_add('normal', a)
            self.listBox.tag_configure('normal',
                                       foreground='black')
            self.listBox.tag_add('repeat', a)
            self.listBox.tag_configure('repeat',
                                       foreground='orange')

            # mark the duplicate row
            if "#!#" in l[i]:
                self.listBox.insert(a, l[i], 'warning')
            elif "#@# Repeated mark" in l[i]:
                res = l[i].split("#@# Repeated mark",1)
                self.listBox.insert(a, res[0]+"\n", 'repeat')
            else:
                self.listBox.insert(a, l[i], 'normal')

    # choice report save path and save the report
    def creatPathSin(self):
        path_ = askdirectory()
        self.path.set(path_)
        self.downSinFile()

    def creatPathSMui(self):
        path_ = askdirectory()
        self.path.set(path_)
        self.downMuiFIle()

    def downSinFile(self):
        path = self.path.get()
        reportResult = MainPage.transferList(self=MainPage)
        messagebox.showinfo(title="Report Generation", message="This Plagiarism Result has been generated")
        downloadFinal.download.use(folderPath, trans, self.show_selected(), reportResult, path)

    def downMuiFIle(self):
        path = self.path.get()
        reportResult = MainPage.transferList(self=MainPage)
        messagebox.showinfo(title="Report Generation", message="All Plagiarism Result has been generated")
        downloadFinal.download.alluse(folderPath, trans, reportResult, path)






if __name__ == "__main__":
    app = UserInterface()
    app.mainloop()
