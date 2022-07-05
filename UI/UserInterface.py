#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat April  5 23:36:17 2022

@author: Ghee
"""
# importing tkinter gui
import tkinter as tk
from tkinter import messagebox, OptionMenu
from PIL import Image, ImageTk
import sys
import os
import inspect
import similarity_algorithm
import downloadFinal
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

class UserInterface(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Plagiarism Checker")
        self.geometry('600x600')
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", lambda: UserInterface.on_closing(self))
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="right", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.sideBar()
        self.frames = {}
        for F in (MainPage, ResultPage):
            page_name = F.__name__
            frame = F(parent=container)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainPage")



    def show_frame(self, page_name):
        # Show a frame for the given page name
        if page_name == "ResultPage":
            global resultListCount
            ResultPage.update(self)
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
                download_l.config(text='Download\n Result', font=(0, 10))
                info_l.config(text='Info', font=(0, 12))
            else:
                # Bring the image back
                menu_l.config(text="")
                home_l.config(text="")
                result_l.config(text="")
                download_l.config(text="")
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
        sid_bar_frame = tk.Frame(self, bg='#184089', width=45, height=self.winfo_height())
        sid_bar_frame.pack(side=tk.LEFT)

        # Make the buttons with the icons to be shown
        menu_b = tk.Button(sid_bar_frame, image=navIcon, highlightbackground='#184089', activebackground='#184089',
                           relief='flat', command=lambda: switch())
        menu_b.image = navIcon
        home_b = tk.Button(sid_bar_frame, image=home, highlightbackground='#184089', relief='flat',
                           command=lambda: self.show_frame("MainPage"))
        home_b.image = home
        result_b = tk.Button(sid_bar_frame, image=result, highlightbackground='#184089', relief='flat',
                             command=lambda: self.show_frame("ResultPage"))
        result_b.image = result
        download_b = tk.Button(sid_bar_frame, image=download, highlightbackground='#184089', relief='flat',
                               command=lambda: downloadFinal.download.use(folderPath, names))
        download_b.image = download
        info_b = tk.Button(sid_bar_frame, image=Info, highlightbackground='#184089', relief='flat')
        info_b.image = Info

        # make label
        menu_l = tk.Label(sid_bar_frame, text='', bg='#184089')
        home_l = tk.Label(sid_bar_frame, text='', bg='#184089')
        result_l = tk.Label(sid_bar_frame, text='', bg='#184089')
        download_l = tk.Label(sid_bar_frame, text='', bg='#184089')
        info_l = tk.Label(sid_bar_frame, text='', bg='#184089')

        # Put them on the frame
        menu_b.grid(row=0, column=0, padx=1, pady=10)
        menu_l.grid(row=0, column=1)
        home_b.grid(row=1, column=0, padx=5, pady=30)
        home_l.grid(row=1, column=1, padx=5, pady=30)
        result_b.grid(row=2, column=0, padx=5, pady=30)
        result_l.grid(row=2, column=1, padx=5, pady=30)
        download_b.grid(row=3, column=0, padx=5, pady=30)
        download_l.grid(row=3, column=1, padx=5, pady=30)
        info_b.grid(row=4, column=0, padx=5, pady=30)
        info_l.grid(row=4, column=1, padx=5, pady=30)

        # So that it does not depend on the widgets inside the frame
        sid_bar_frame.grid_propagate(False)


class MainPage(tk.Frame):
    global names
    names = []
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    global parentdir
    parentdir = os.path.dirname(currentdir)
    sys.path.insert(0, parentdir)
    global folderPath
    folderPath = None

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        container = tk.Frame(self, bg="#c0c0c0")
        container.pack(side="right", fill="both", expand=True)

        self.topFrame = tk.Frame(container, bg='#c0c0c0', width=container.winfo_width(),
                                 height=(container.winfo_height() / 5 * 4))
        self.topFrame.pack(side=tk.TOP, fill="both", expand=1)
        self.botFrame = tk.Frame(container, bg='#c0c0c0', width=container.winfo_width(),
                                 height=(container.winfo_height() / 5 * 1))
        self.botFrame.pack(side=tk.BOTTOM, fill="x", expand=1)
        # dropdownbox
        self.dropDownFrame = tk.Frame(self.topFrame, bg='#c0c0c0', width=(container.winfo_width() / 5 * 1),
                                      height=(container.winfo_height() / 5 * 4))
        self.dropDownFrame.pack(side=tk.RIGHT)
        self.selection_l = tk.Label(self.dropDownFrame, text='Language Selection:', bg='#c0c0c0', fg='black',
                                    font=(0, 18))
        self.selection_l.pack(side=tk.TOP, pady=15, padx=15)
        self.variable = tk.StringVar(self.dropDownFrame)
        self.variable.set("Python")  # default value
        self.selectionBox = OptionMenu(self.dropDownFrame, self.variable, "Python", "C++", "Java", "R", "C#")
        self.selectionBox.configure(highlightbackground='black', background='#c0c0c0', fg='black', width=12)
        self.selectionBox.pack(side=tk.BOTTOM, pady=15, padx=25)

        # listBox
        self.listBoxFrame = tk.Frame(self.topFrame, bg='#c0c0c0', width=(container.winfo_width() / 5 * 4),
                                     height=(container.winfo_height() / 5 * 4))
        self.listBoxFrame.pack(side=tk.LEFT)
        self.studentWork_l = tk.Label(self.listBoxFrame, text='Student Files:', bg='#c0c0c0', fg='black', font=(0, 20))
        self.studentWork_l.grid(column=0, row=0, padx=10)
        self.listBox = tk.Listbox(self.listBoxFrame, bg='white', fg='black', width=30)
        self.listBox.grid(column=0, row=1, padx=10, columnspan=2)
        self.selection_b = tk.Button(self.listBoxFrame, highlightbackground='#c0c0c0', text="Folder", width=8,
                                     command=lambda: self.openFile())
        self.selection_b.grid(column=1, row=2)

        # button for start plagiarism check
        self.check_b = tk.Button(self.botFrame, highlightbackground='#c0c0c0', text="Plagiarism Check",
                                 command=lambda: self.checkFile())
        self.check_b.pack(side=tk.RIGHT, padx=50)

    def checkFile(self):
        global folderPath
        if folderPath is None:
            messagebox.showerror(title='Warning', message="Please a folder / files.")
        else:
            similarity_algorithm.check(folderPath)

    def openFile(self):
        global folderPath
        from tkinter import filedialog as fd
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )

        folderPath = fd.askdirectory() + '/'
        self.updateListBox()

    def updateListBox(self):
        global names
        names = similarity_algorithm.walk_dir(folderPath)
        names = [names[0][1:]]
        for i in names:
            for x in i:
                self.listBox.insert(tk.END, x)


class ResultPage(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.resultChart = None
        self.fig = None
        self.ax = None
        container = tk.Frame(self, bg="#c0c0c0")
        container.pack(side="right", fill="both", expand=True)
        self.resultListCount = similarity_algorithm.resultListCount
        # resultFrame
        self.resultFrame = tk.Frame(container, bg='#c0c0c0', width=self.winfo_width(), height=self.winfo_height())
        self.resultFrame.pack(side=tk.BOTTOM, fill="both", expand=1)
        self.drawFigure()

    def drawFigure(self):

        self.resultChart = FigureCanvasTkAgg()
        resultList = ["Below\n10%", "Between\n10%~15%", "Between\n15%~25%", "Over\n25%"]
        if len(self.resultListCount) > 1:
            self.fig = Figure(facecolor='white', figsize=(3.5, 3.5))  # create a figure object
            self.ax = self.fig.add_subplot(111)  # add an Axes to the figure
            self.ax.set_title("Plagiarism Result")
            self.ax.pie(self.resultListCount, radius=1, labels=resultList, autopct='%0.2f%%', shadow=True,
                        textprops={'fontsize': 10})
            self.resultChart = FigureCanvasTkAgg(self.fig, self.resultFrame)
            self.resultChart.draw()
            self.resultChart.get_tk_widget().pack(side=tk.RIGHT, padx=15)




if __name__ == "__main__":
    app = UserInterface()
    app.mainloop()
