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
        for F in (MainPage, ResultGraphPage, ResultPage):
            page_name = F.__name__
            frame = F(parent=self.mainContainer)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainPage")

    def show_frame(self, page_name):
        # Show a frame for the given page name
        frame = self.frames[page_name]
        if page_name == 'ResultGraphPage':
            resultListCount = similarity_algorithm.getResultListCount()
            if len(resultListCount) > 1:
                ResultGraphPage.refresh(self.mainContainer)
                ResultGraphPage.update()
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

        def expand():
            global cur_width, expanded
            cur_width += 10  # Increase the width by 10
            rep = self.after(5, expand)  # Repeat this func every 5 ms
            sid_bar_frame.config(width=cur_width)  # Change the width to new increase width
            if cur_width >= max_w:  # If width is greater than maximum width
                expanded = True  # Frame is expended
                self.after_cancel(rep)  # Stop repeating the func
                fill()

        def contract():
            global cur_width, expanded
            cur_width -= 10  # Reduce the width by 10
            rep = self.after(5, contract)  # Call this func every 5 ms
            sid_bar_frame.config(width=cur_width)  # Change the width to new reduced width
            if cur_width <= min_w:  # If it is back to normal width
                expanded = False  # Frame is not expanded
                self.after_cancel(rep)  # Stop repeating the func
                fill()

        def fill():
            if expanded:  # If the frame is expanded
                # Show a text
                menu_l.config(text="Menu", font=(0, 12))
                home_l.config(text='Home', font=(0, 12))
                result_l.config(text='Result', font=(0, 12))
                info_l.config(text='Info', font=(0, 12))
                result_l2.config(text="Result", font=(0,12))
            else:
                # Bring the image back
                menu_l.config(text="")
                home_l.config(text="")
                result_l.config(text="")
                info_l.config(text='')

        def switch():
            global btnState
            if btnState is True:

                contract()
                # turning button OFF:
                btnState = False
            else:

                expand()
                # turing button ON:
                btnState = True

        # define icon
        navIcon = ImageTk.PhotoImage(Image.open('../resource/Menu.png').resize((20, 20)))
        home = ImageTk.PhotoImage(Image.open('../resource/Home.png').resize((20, 20)))
        result = ImageTk.PhotoImage(Image.open('../resource/Result.png').resize((20, 20)))
        download = ImageTk.PhotoImage(Image.open('../resource/Download.png').resize((20, 20)))
        Info = ImageTk.PhotoImage(Image.open('../resource/Info.png').resize((20, 20)))

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
            relief="flat",
                )

        home_b = Button(sid_bar_frame,
            text="Upload",
            bg="#191970",
            fg="white",
            width=90,
            bd=4,
            relief="flat",
            command=lambda: self.show_frame("MainPage"))

        result_b = Button(sid_bar_frame,
            text="Result\ngraph",
            bg="#191970",
            fg="white",
            width=90,
            bd=4,
            relief="flat",
            command=lambda: self.show_frame("ResultGraphPage"))

        # download_b = tk.Button(sid_bar_frame,
        #     text="Reprot",
        #     bg="#191970",
        #     fg="white",
        #     width=12,
        #     relief="flat",
        #     command=lambda: self.show_frame("ReportPage"))
        #downloadFinal.download.use(folderPath, names)

        info_b = Button(sid_bar_frame,
            text="Help",
            bg="#191970",
            fg="white",
            width=90,
            bd=4,
            relief="flat",
            command=lambda: self.infoButtonFunc())

        result_c = Button(sid_bar_frame,
                             text="Result",
                             bg="#191970",
                             fg="white",
                             width=90,
                             bd=4,
                             relief="flat",
                             command=lambda: self.show_frame("ResultPage"))


        # make label
        menu_l = tk.Label(sid_bar_frame, text='', bg='#191970')
        home_l = tk.Label(sid_bar_frame, text='', bg='#191970')
        result_l = tk.Label(sid_bar_frame, text='', bg='#191970')
        download_l = tk.Label(sid_bar_frame, text='', bg='#191970')
        info_l = tk.Label(sid_bar_frame, text='', bg='#191970')
        result_l2 = tk.Label(sid_bar_frame, text='', bg='#191970')

        # Put them on the frame
        menu_b.grid(row=0, column=0, padx=1, pady=10)
        menu_l.grid(row=0, column=1)
        home_b.grid(row=1, column=0, padx=5, pady=30)
        home_l.grid(row=1, column=1, padx=5, pady=30)
        result_b.grid(row=3, column=0, padx=5, pady=30)
        result_l.grid(row=3, column=1, padx=5, pady=30)
        info_b.grid(row=4, column=0, padx=5, pady=30)
        info_l.grid(row=4, column=1, padx=5, pady=30)
        result_c.grid(row=2, column=0, padx=5, pady=30)
        result_l2.grid(row=2, column=1, padx=5, pady=30)

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
            text="Description and introduction",
            bg="#D7E4F0",
            fg="black",
            width=25,
            relief="flat",
            command=lambda: switch_text("description.txt"),
        )

        Function_is_introduced_b = tk.Button(
            top_side_frame,
            text="Function and introduced",
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
            num = stater.get()
            if num == 1:
                messagebox.askyesno(title='Attention', message="Please upload Python files")
            elif num == 2:
                messagebox.askyesno(title='Attention', message="Please upload Java files")
            elif num == 3:
                messagebox.askyesno(title='Attention', message="Pleas upload C++ files")

        dropDownFrame = tk.Frame(middleFrame, bg='#F5F5F5', width=100,
                                 height=5)
        dropDownFrame.pack(side=tk.TOP)
        pyButton1 = tk.Radiobutton(dropDownFrame, text='Python', variable=stater, value=1,
                                   command=changeCode)
        pyButton1.grid(column=0, row=4)
        pyButton2 = tk.Radiobutton(dropDownFrame, text='Java', variable=stater, value=2,
                                   command=changeCode)
        pyButton2.grid(column=1, row=4)
        pyButton3 = tk.Radiobutton(dropDownFrame, text='C++', variable=stater, value=3,
                                   command=changeCode)
        pyButton3.grid(column=2, row=4)




        # listBox

        listBoxFrame = tk.Frame(topFrame, bg='#F5F5F5', width=100,
                                height=60)
        listBoxFrame.grid(column=0, row=3, padx=10, columnspan=2)
        studentWork_l = tk.Label(topFrame, text='\n\nStudent Files:\n\n', bg='#F5F5F5', fg='black', font=(0, 20))
        studentWork_l.grid(column=0, row=1, padx=10, columnspan=2)
        self.listBox = tk.Listbox(listBoxFrame, bg='white', fg='black', width=66)
        self.listBox.grid(column=0, row=1, padx=10, columnspan=2, rowspan=2)
        selection_b = Button(dropDownFrame, highlightbackground='#F5F5F5', text="Folder", width=60, bg='white',
                                command=lambda: self.openFile())
        selection_b.grid(column=1, row=0, rowspan=2)





        # button for start plagiarism check
        check_b = Button(botFrame, bg='#00FF7F', text="Confirm", fg="black", width=90,
                            command=lambda: self.checkFile(stater.get()))
        check_b.pack(side=tk.RIGHT, padx=50)

        cancel_b = Button(botFrame, bg="#FF0000", text="Cancel", fg="black", width=90,
                             command=lambda: self.cancelFile())
        cancel_b.pack(side=tk.LEFT, padx=50,)


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



    def transferList(self):
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
        global  folderPath
        similarity_algorithm.deletFile()
        folderPath = None
        self.listBox.delete(0, tk.END)


    def updateListBox(self):
        global names
        global trans
        self.listBox.delete(0, tk.END)
        names = similarity_algorithm.walk_dir(folderPath)
        print(names)
        names = [names[0][0:]]
        for i in names:
            for x in i:
                if not x.startswith("."):
                    self.listBox.insert(tk.END, x)
                    trans.append(x)



# class ReportPage(tk.Frame):
#
#     def __init__(self, parent):
#
#         tk.Frame.__init__(self, parent)
#
#         container = tk.Frame(self, bg="#F5F5F5")
#         container.pack(side="right", fill="both", expand=True)
#
#         topFrame = tk.Frame(container, bg='#F5F5F5', width=container.winfo_width(),
#                             height=(container.winfo_height() / 5 * 1))
#         topFrame.pack(side=tk.TOP, fill="both", expand=1)
#         botFrame = tk.Frame(container, bg='#F5F5F5', width=container.winfo_width(),
#                             height=(container.winfo_height() / 5 * 1))
#         botFrame.pack(side=tk.BOTTOM, fill="x", expand=1)
#
#
#
#         # listBox
#         tittleFrame = tk.Frame(topFrame, bg='#F5F5F5', width=100,
#                                 height=30)
#         tittleFrame.pack(side=tk.TOP)
#         listBoxFrame = tk.Frame(topFrame, bg='#F5F5F5', width=100,
#                                 height=100)
#         listBoxFrame.pack(side=tk.LEFT)
#
#
#         studentWork_l = tk.Label(tittleFrame, text='\nReport:', bg='#F5F5F5', fg='black', font=(0, 30))
#         studentWork_l.grid(column=0, row=0, padx=30)
#         show_b = tk.Button(tittleFrame, bg='#191970', text="Preview", fg="white", width=10,
#                             command=lambda: self.test())
#         show_b.grid(column=0, row=1,padx=30)
#
#         scrolly = tk.Scrollbar(listBoxFrame)
#         scrolly.pack(side=tk.RIGHT, fill=tk.Y)
#
#         scrollx = tk.Scrollbar(listBoxFrame, orient=tk.HORIZONTAL)
#         scrollx.pack(side=tk.BOTTOM, fill=tk.X)
#
#         self.listBox = tk.Text(listBoxFrame, wrap='none')
#         self.listBox.pack(fill=tk.BOTH, expand=tk.YES)
#         self.listBox.config(yscrollcommand=scrolly.set)
#         self.listBox.config(xscrollcommand=scrollx.set)
#         scrolly.config(command=self.listBox.yview)
#         scrollx.config(command=self.listBox.xview)
#
#
#
#         check_b = Button(botFrame, bg='#191970', text="Download this report", fg="white", width=50,
#                             command=lambda: self.downSinFile())
#         check_b.pack(side=tk.RIGHT, padx=50)
#
#         cancel_b = Button(botFrame, bg="#191970", text="Download all report", fg="white", width=50,
#                              command=lambda: self.downMuiFIle())
#         cancel_b.pack(side=tk.LEFT, padx=50)
#
#         #scrollBary.config(command=listBox.yview)
#         #scrollBarx.config(command=listBox.xview)
#         self.listBox.bind('<KeyPress>',lambda e:'break')
#         # yscrollcommand=scrollBary.set, xscrollcommand=scrollBarx.set
#
#
#
#     def test(self):
#         reportResult=MainPage.transferList(self=MainPage)
#         l=downloadFinal.download.trans(folderPath, trans, ResultPage.wantFile(self=ResultPage), reportResult)[0]
#
#         for i in range (0,len(l)):
#             a = float(i+1)
#             self.listBox.tag_add('warning', a)
#             self.listBox.tag_configure('warning',
#                                        foreground='red')
#             self.listBox.tag_add('normal', a)
#             self.listBox.tag_configure('normal',
#                                        foreground='black')
#             if "#####" in l[i]:
#                 self.listBox.insert(a, l[i], 'warning')
#             else:
#                 self.listBox.insert(a, l[i], 'normal')
#
#     def downSinFile(self):
#         reportResult = MainPage.transferList(self=MainPage)
#         messagebox.showinfo(title="Report Generation", message="This Plagiarism Result has been generated")
#         downloadFinal.download.use(folderPath, trans, ResultPage.wantFile(self=ResultPage), reportResult)
#     def downMuiFIle(self):
#         reportResult = MainPage.transferList(self=MainPage)
#         messagebox.showinfo(title="Report Generation", message="All Plagiarism Result has been generated")
#         downloadFinal.download.alluse(folderPath, trans, reportResult)






class ResultPage(tk.Frame):
    global filename
    filename = None

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        container = tk.Frame(self, bg="#F5F5F5")
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


        # listBox

        listBoxFrame = tk.Frame(topFrame, bg='#F5F5F5', width=80,
                                height=60)
        listBoxFrame.pack(side=tk.TOP)
        colums = ['File Name', 'Rate']
        self.resultListBox = ttk.Treeview(listBoxFrame, columns=colums, show='headings', heigh=10)
        self.resultListBox.grid(column=1, row=1, padx=20, columnspan=2)
        self.resultListBox.heading('File Name', text='File Name', )
        self.resultListBox.heading('Rate', text='Rate', )
        self.resultListBox.column('File Name', width=250)
        self.resultListBox.column('Rate', width=140)
        self.resultListBox.tag_configure('tag_green',
                           foreground='green')
        self.resultListBox.tag_configure('tag_origin',
                           foreground='orange')
        self.resultListBox.tag_configure('tag_red',
                           foreground='red')


        # button for start plagiarism check
        check_b = Button(botFrame, bg='#00FF7F', text="Show report", fg="black", width=100,
                            command=lambda: self.clickReport())
        check_b.pack(side=tk.RIGHT, padx=50)
        result_b = Button(botFrame, bg='#191970', text="Show result", fg="white", width=100,
                             command=lambda: self.updataResult())
        result_b.pack(side=tk.LEFT, padx=50)



    def updataResult(self):
        thisDict = MainPage.transferList(self=MainPage)
        if thisDict is None:
            messagebox.showerror(title='Warning', message="Please a folder / files.")
        else:
            messagebox.showinfo(title="Result Information", message="All information loaded")
            resultList = thisDict[0]
            i = 0
            my_list=[]
            for row in self.resultListBox.get_children():
                self.resultListBox.delete(row)
            for key,val in resultList.items():
                newCalue1=float(resultList[key])
                newCalue2=newCalue1*100
                newCalue3=float('%.2f'%newCalue2)
                newvalue=str(newCalue3)+"%"
                my_list.append((key, newvalue))
            for value in my_list:
                new = value
                new1 = new[1].strip("%")
                new2 = float(new1)
                if new2 <= 20:
                    tag='tag_green'
                elif new2 > 50:
                    tag = 'tag_red'
                else:
                    tag ='tag_origin'
                self.resultListBox.insert(parent='', index=i, iid=i, values=value, tags=tag)
                i+=1


    def show_selected(self):
        global filename
        #messagebox.showinfo(title="Report Generation", message="Please click Preview on the Report page to view the report")
        for item in self.resultListBox.selection():
            item_text = self.resultListBox.item(item, "values")
            filename=item_text[0]
        return filename


    def clickReport(self):
        if self.show_selected() is None:
            messagebox.showerror(title='Warning', message="Please a choice file.")
        else:
            self.report()




    def report(self):
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

        # listBox
        tittleFrame = tk.Frame(topFrame, bg='#F5F5F5', width=100,
                               height=30)
        tittleFrame.pack(side=tk.TOP)
        listBoxFrame = tk.Frame(topFrame, bg='#F5F5F5', width=100,
                                height=100)
        listBoxFrame.pack(side=tk.BOTTOM)

        studentWork_l = tk.Label(tittleFrame, text='\nReport:', bg='#F5F5F5', fg='black', font=(0, 30))
        studentWork_l.grid(column=0, row=0, padx=30)
        # show_b = tk.Button(tittleFrame, bg='#191970', text="Preview", fg="white", width=10,
        #                    command=lambda: self.test())
        # show_b.grid(column=0, row=1, padx=30)

        scrolly = tk.Scrollbar(listBoxFrame)
        scrolly.pack(side=tk.RIGHT, fill=tk.Y)

        scrollx = tk.Scrollbar(listBoxFrame, orient=tk.HORIZONTAL)
        scrollx.pack(side=tk.BOTTOM, fill=tk.X)

        self.listBox = tk.Text(listBoxFrame, wrap='none')
        self.listBox.pack(fill=tk.BOTH, expand=tk.YES)
        self.listBox.config(yscrollcommand=scrolly.set)
        self.listBox.config(xscrollcommand=scrollx.set)
        scrolly.config(command=self.listBox.yview)
        scrollx.config(command=self.listBox.xview)

        check_b = Button(botFrame, bg='#191970', text="Download this report", fg="white", width=150,
                            command=lambda: self.downSinFile())
        check_b.pack(side=tk.RIGHT, padx=50)

        cancel_b = Button(botFrame, bg="#191970", text="Download all report", fg="white", width=150,
                             command=lambda: self.downMuiFIle())
        cancel_b.pack(side=tk.LEFT, padx=50)


        self.listBox.bind('<KeyPress>', lambda e: 'break')


        global filename
        thisName = self.show_selected()
        reportResult=MainPage.transferList(self=MainPage)
        l=downloadFinal.download.trans(folderPath, trans, thisName, reportResult)[0]
        self.listBox.delete("1.0", "end")

        for i in range (0,len(l)):
            a = float(i+1)
            self.listBox.tag_add('warning', a)
            self.listBox.tag_configure('warning',
                                       foreground='red')
            self.listBox.tag_add('normal', a)
            self.listBox.tag_configure('normal',
                                       foreground='black')
            if "#####" in l[i]:
                self.listBox.insert(a, l[i], 'warning')
            else:
                self.listBox.insert(a, l[i], 'normal')

    def downSinFile(self):
        reportResult = MainPage.transferList(self=MainPage)
        messagebox.showinfo(title="Report Generation", message="This Plagiarism Result has been generated")
        downloadFinal.download.use(folderPath, trans, ResultPage.show_selected(self), reportResult)
    def downMuiFIle(self):
        reportResult = MainPage.transferList(self=MainPage)
        messagebox.showinfo(title="Report Generation", message="All Plagiarism Result has been generated")
        downloadFinal.download.alluse(folderPath, trans, reportResult)



class ResultGraphPage(tk.Frame):
    fig = Figure(figsize=(4, 4), dpi=100)

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        resultListCount = similarity_algorithm.getResultListCount()
        ax = ResultGraphPage.fig.add_subplot(111)
        if len(resultListCount) <= 0:
            ax.bar(['0~10%\nSimilarity', '10~20%\nSimilarity', '20~40\nSimilarity', 'More than 40%\nSimilarity'], ['0'], color='lightsteelblue')
            canvas = FigureCanvasTkAgg(ResultGraphPage.fig, self)
            canvas.get_tk_widget().pack(side=tk.TOP, fill="both", expand=1)

    def refresh(self):
        resultListCount = similarity_algorithm.getResultListCount()
        ResultGraphPage.fig.clear()
        ax = ResultGraphPage.fig.add_subplot(111)
        ax.set_ylim(ymin=0, ymax=(sum(resultListCount)))
        ax.bar(['0~10%\nSimilarity', '10~20%\nSimilarity', '20~40\nSimilarity', 'More than 40%\nSimilarity'],
               resultListCount, color='lightsteelblue')
        canvas = FigureCanvasTkAgg(ResultGraphPage.fig, self)
        canvas.get_tk_widget().grid(row=0, column=0)


# main loop
if __name__ == "__main__":
    app = UserInterface()
    app.mainloop()
