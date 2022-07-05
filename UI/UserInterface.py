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
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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
        self.sideBarContainer = tk.Frame(self)
        self.sideBarContainer.pack(side="left", fill="both", expand=0)
        self.mainContainer = tk.Frame(self)
        self.mainContainer.pack(side="right", fill="both", expand=1)
        self.mainContainer.grid_rowconfigure(0, weight=1)
        self.mainContainer.grid_columnconfigure(0, weight=1)
        self.sideBar()
        self.frames = {}
        for F in (MainPage, ResultPage):
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
        if page_name == 'ResultPage':
            resultListCount = similarity_algorithm.getResultListCount()
            if len(resultListCount) > 1:
                ResultPage.refresh(self.mainContainer)
                ResultPage.update()
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
        sid_bar_frame = tk.Frame(self.sideBarContainer, bg='#184089', width=45, height=self.winfo_height())
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
        info_b = tk.Button(sid_bar_frame, image=Info, highlightbackground='#184089', relief='flat',
                           command=lambda: self.infoButtonFunc())
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

    def infoButtonFunc(self):
        from tkinter import Text as txt
        from tkinter import Scrollbar as scroll

        top = tk.Toplevel(
            master=self,
            # bg,
            # fg,
            # bd,
            width=self.winfo_width(),
            height=self.winfo_height(),
            # font,
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
            # highlightbackground="#184089",
            # activebackground="#184089",
            bg="#D7E4F0",
            fg="black",
            width=25,
            relief="flat",
            command=lambda: switch_text("description.txt"),
        )

        Function_is_introduced_b = tk.Button(
            top_side_frame,
            text="Function and introduced",
            # highlightbackground="#184089",
            # activebackground="#184089",
            bg="#D7E4F0",
            fg="black",
            width=25,
            relief="flat",
            command=lambda: switch_text("func.txt"),
        )
        Support_b = tk.Button(
            top_side_frame,
            text="Support",
            # highlightbackground="#184089",
            # activebackground="#184089",
            bg="#D7E4F0",
            fg="black",
            width=25,
            relief="flat",
            command=lambda: switch_text("support.txt"),
        )
        Other_b = tk.Button(
            top_side_frame,
            text="Other",
            # highlightbackground="#184089",
            # activebackground="#184089",
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

        topFrame = tk.Frame(container, bg='#c0c0c0', width=container.winfo_width(),
                            height=(container.winfo_height() / 5 * 4))
        topFrame.pack(side=tk.TOP, fill="both", expand=1)
        botFrame = tk.Frame(container, bg='#c0c0c0', width=container.winfo_width(),
                            height=(container.winfo_height() / 5 * 1))
        botFrame.pack(side=tk.BOTTOM, fill="x", expand=1)
        # dropdown box
        dropDownFrame = tk.Frame(topFrame, bg='#c0c0c0', width=(container.winfo_width() / 5 * 1),
                                 height=(container.winfo_height() / 5 * 4))
        dropDownFrame.pack(side=tk.RIGHT)
        selection_l = tk.Label(dropDownFrame, text='Language Selection:', bg='#c0c0c0', fg='black',
                               font=(0, 18))
        selection_l.pack(side=tk.TOP, pady=15, padx=15)
        variable = tk.StringVar(dropDownFrame)
        variable.set("Python")  # default value
        selectionBox = OptionMenu(dropDownFrame, variable, "Python", "C++", "Java", "R", "C#")
        selectionBox.configure(highlightbackground='black', background='#c0c0c0', fg='black', width=12)
        selectionBox.pack(side=tk.BOTTOM, pady=15, padx=25)

        # listBox
        listBoxFrame = tk.Frame(topFrame, bg='#c0c0c0', width=(container.winfo_width() / 5 * 4),
                                height=(container.winfo_height() / 5 * 4))
        listBoxFrame.pack(side=tk.LEFT)
        studentWork_l = tk.Label(listBoxFrame, text='Student Files:', bg='#c0c0c0', fg='black', font=(0, 20))
        studentWork_l.grid(column=0, row=0, padx=10)
        self.listBox = tk.Listbox(listBoxFrame, bg='white', fg='black', width=30)
        self.listBox.grid(column=0, row=1, padx=10, columnspan=2)
        selection_b = tk.Button(listBoxFrame, highlightbackground='#c0c0c0', text="Folder", width=8,
                                command=lambda: self.openFile())
        selection_b.grid(column=1, row=2)

        # button for start plagiarism check
        check_b = tk.Button(botFrame, highlightbackground='#c0c0c0', text="Plagiarism Check",
                            command=lambda: self.checkFile())
        check_b.pack(side=tk.RIGHT, padx=50)

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
    fig = Figure(figsize=(4, 4), dpi=100)

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        resultListCount = similarity_algorithm.getResultListCount()
        ax = ResultPage.fig.add_subplot(111)
        if len(resultListCount) <= 0:
            ax.bar(['0~10%\nSimilarity', '10~20%\nSimilarity', '20~40\nSimilarity', 'More than 40%\nSimilarity'], ['0'], color='lightsteelblue')
            canvas = FigureCanvasTkAgg(ResultPage.fig, self)
            canvas.get_tk_widget().pack(side=tk.TOP, fill="both", expand=1)

    def refresh(self):
        resultListCount = similarity_algorithm.getResultListCount()
        ResultPage.fig.clear()
        ax = ResultPage.fig.add_subplot(111)
        ax.bar(['0~10%\nSimilarity', '10~20%\nSimilarity', '20~40\nSimilarity', 'More than 40%\nSimilarity'],
               resultListCount, color='lightsteelblue')
        canvas = FigureCanvasTkAgg(ResultPage.fig, self)
        canvas.get_tk_widget().grid(row=0, column=0)


# main loop
if __name__ == "__main__":
    app = UserInterface()
    app.mainloop()
