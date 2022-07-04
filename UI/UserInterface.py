#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat April  5 23:36:17 2022

@author: Ghee
"""
# importing tkinter gui
import tkinter as tk
from tkinter import messagebox, OptionMenu, Toplevel
from PIL import Image, ImageTk
import sys
import os
import inspect
import parso

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import final
import downloadFinal


# creating window
window = tk.Tk()
# title
window.title("Plagiarism Checker")

# setting tkinter window size
window.geometry("650x600")

# setting switch state:
btnState = False

min_w = 60  # Minimum width of the frame
max_w = 120  # Maximum width of the frame
cur_width = min_w  # Increasing width of the frame
expanded = False  # Check if it is completely expanded
folderPath = ""


def expand():
    global cur_width, expanded
    cur_width += 10  # Increase the width by 10
    rep = window.after(5, expand)  # Repeat this func every 5 ms
    sid_bar_frame.config(width=cur_width)  # Change the width to new increase width
    if cur_width >= max_w:  # If width is greater than maximum width
        expanded = True  # Frame is expended
        window.after_cancel(rep)  # Stop repeating the func
        fill()


def contract():
    global cur_width, expanded
    cur_width -= 10  # Reduce the width by 10
    rep = window.after(5, contract)  # Call this func every 5 ms
    sid_bar_frame.config(width=cur_width)  # Change the width to new reduced width
    if cur_width <= min_w:  # If it is back to normal width
        expanded = False  # Frame is not expanded
        window.after_cancel(rep)  # Stop repeating the func
        fill()


def fill():
    if expanded:  # If the frame is expanded
        # Show a text
        menu_l.config(text="Menu", font=(0, 12))
        home_l.config(text="Home", font=(0, 12))
        result_l.config(text="Result", font=(0, 12))
        download_l.config(text="Download\n Result", font=(0, 10))
        info_l.config(text="Info", font=(0, 12))
    else:
        # Bring the image back
        menu_l.config(text="")
        home_l.config(text="")
        result_l.config(text="")
        download_l.config(text="")
        info_l.config(text="")


# add info/help button function
def infoButtonFunc():
    """
    from subprocess import Popen, PIPE

    process = Popen(["python", "PlaSysCheckerInfo.py"], stdout=PIPE)
    process.stdout.close()
    process.wait()
    """
    from tkinter import Text as txt
    from tkinter import Scrollbar as scroll

    top = Toplevel(
        master=window,
        # bg,
        # fg,
        # bd,
        width=window.winfo_width(),
        height=window.winfo_height(),
        # font,
    )
    top.title("help")

    top_side_frame = tk.Frame(
        top,
        bg="#191970",
        width=200,
        height=window.winfo_height(),
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
        width=window.winfo_width() - 200,
        height=(window.winfo_height()),
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


def openFile():
    global folderPath
    from tkinter import filedialog as fd

    filetypes = (("text files", "*.txt"), ("All files", "*.*"))

    folderPath = fd.askdirectory() + "/"
    updateListBox()


names = []


def updateListBox():
    global names
    names = final.walk_dir(folderPath)
    names = [names[0][1:]]
    print(names)
    for i in names:
        for x in i:
            listBox.insert(tk.END, x)


# Define the icons to be shown and resize it
navIcon = ImageTk.PhotoImage(Image.open("../resource/Menu.png").resize((20, 20)))
home = ImageTk.PhotoImage(Image.open("../resource/Home.png").resize((20, 20)))
result = ImageTk.PhotoImage(Image.open("../resource/Result.png").resize((20, 20)))
download = ImageTk.PhotoImage(Image.open("../resource/Download.png").resize((20, 20)))
Info = ImageTk.PhotoImage(Image.open("../resource/Info.png").resize((20, 20)))

window.update()  # For the width to get updated
sid_bar_frame = tk.Frame(window, bg="#191970", width=50, height=window.winfo_height())


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


# Make the buttons with the icons to be shown
menu_b = tk.Button(
    sid_bar_frame,
    image=navIcon,
    # highlightbackground="#184089",
    # activebackground="#184089",
    relief="flat",
    command=switch,
)
home_b = tk.Button(
    sid_bar_frame,
    image=home,
    # highlightbackground="#184089",
    relief="flat",
    command=lambda: changeFrame(resultFrame, mainFrame),
)
result_b = tk.Button(
    sid_bar_frame,
    image=result,
    # highlightbackground="#184089",
    relief="flat",
    command=lambda: changeFrame(mainFrame, resultFrame),
)
download_b = tk.Button(
    sid_bar_frame,
    image=download,
    # highlightbackground="#184089",
    relief="flat",
    command=lambda: downloadFinal.download.use(folderPath, names),
)
info_b = tk.Button(
    sid_bar_frame,
    image=Info,
    # highlightbackground="#184089",
    relief="flat",
    command=infoButtonFunc,
)

# make label
menu_l = tk.Label(
    sid_bar_frame,
    text="",
    bg="#191970",
    fg="white",
)
home_l = tk.Label(
    sid_bar_frame,
    text="",
    bg="#191970",
    fg="white",
)
result_l = tk.Label(
    sid_bar_frame,
    text="",
    bg="#191970",
    fg="white",
)
download_l = tk.Label(
    sid_bar_frame,
    text="",
    bg="#191970",
    fg="white",
)
info_l = tk.Label(
    sid_bar_frame,
    text="",
    bg="#191970",
    fg="white",
)

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

mainFrame = tk.Frame(
    window, bg="#F5F5F5", width=window.winfo_width(), height=(window.winfo_height())
)
mainFrame.grid_propagate(False)


"""
# sideFrame
topFrame = tk.Frame(
    mainFrame,
    # bg="#c0c0c0",
    width=window.winfo_width(),
    height=(window.winfo_height() / 5 * 4),
)
# topFrame.pack(side=tk.TOP)
botFrame = tk.Frame(
    mainFrame,
    # bg="#f0a1a8",
    width=window.winfo_width(),
    height=(window.winfo_height() / 5 * 1),
)
# botFrame.pack(side=tk.BOTTOM)
"""


# listBox

"""
listBoxFrame = tk.Frame(
    mainFrame,
    # bg="#c0c0c0",
    width=(window.winfo_width() / 5 * 4),
    height=(window.winfo_height() / 5 * 4),
)
# listBoxFrame.pack(side=tk.LEFT)
"""

studentWork_l = tk.Label(mainFrame, text="Student Files:", fg="black", font=(0, 20))
studentWork_l.grid(
    column=0,
    row=0,
    padx=(5, 40),
    pady=(20, 2),
)
listBox = tk.Listbox(mainFrame, bg="white", fg="black", width=30)
listBox.grid(
    column=0,
    row=1,
    padx=(5, 40),
    pady=2,
)
selection_b = tk.Button(
    mainFrame,
    # highlightbackground="#c0c0c0",
    background="#87CEEB",
    fg="#191970",
    text="Folder",
    relief="flat",
    width=12,
    command=lambda: openFile(),
)
selection_b.grid(
    column=0,
    row=2,
    padx=(5, 40),
    pady=2,
    sticky="e",
)

"""
# dropdownbox
dropDownFrame = tk.Frame(
    topFrame,
    # bg="#c0c0c0",
    width=(window.winfo_width() / 5 * 1),
    height=(window.winfo_height() / 5 * 4),
)
# dropDownFrame.pack(side=tk.RIGHT)
"""

selection_l = tk.Label(mainFrame, text="Language Selection:", fg="black", font=(0, 18))
selection_l.grid(
    column=1,
    row=0,
    padx=(20, 5),
    pady=(20, 2),
    # side=tk.TOP,
)
variable = tk.StringVar()
variable.set("Python")  # default value
selectionBox = OptionMenu(mainFrame, variable, "Python", "C++", "Java", "R", "C#")
selectionBox.configure(
    # highlightbackground="black",
    background="#c0c0c0",
    fg="black",
    relief="flat",
    width=20,
)
selectionBox.grid(
    column=1,
    row=1,
    padx=(20, 5),
    pady=2,
    sticky="ne"
    # side=tk.BOTTOM,
)
# topFrame.pack_propagate(False)

# button for start plagiarism check
check_b = tk.Button(
    mainFrame,
    # highlightbackground="#f0a1a8",
    background="#87CEEB",
    fg="#191970",
    text="Plagiarism Check",
    relief="flat",
    width=25,
    height=1,
    command=lambda: final.check(folderPath),
)
check_b.grid(
    column=0,
    row=3,
    columnspan=2,
    padx=5,
    pady=(30, 5),
    sticky="e",
    # side=tk.RIGHT,
)
# botFrame.pack_propagate(False)


# resultFrame
resultFrame = tk.Frame(
    window, bg="#c0c0c0", width=window.winfo_width(), height=window.winfo_height()
)

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

fig = Figure(facecolor="white", figsize=(3.5, 3.5))
ax = fig.add_subplot(111)  # add an Axes to the figure
canvas = FigureCanvasTkAgg(fig, master=resultFrame)
# placing the canvas on the Tkinter window
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

resultFrame.pack_propagate(False)

sid_bar_frame.pack(side=tk.LEFT)
resultFrame.pack_forget()
mainFrame.pack(side=tk.RIGHT)


def changeFrame(windowFrame, toBeshownFrame):
    if id(windowFrame) == id(resultFrame):
        showResult()
    windowFrame.pack_forget()
    toBeshownFrame.pack()


def showResult():
    global resultFrame

    resultList = ["Below\n10%", "Between\n10%~15%", "Between\n15%~25%", "Over\n25%"]
    resultListCount = final.resultListCount

    if len(resultListCount) > 1:
        global canvas, ax
        ax.pie(
            resultListCount,
            radius=1,
            labels=resultList,
            autopct="%0.2f%%",
            shadow=True,
            textprops={"fontsize": 10},
        )
        ax.set_title("Plagiarism Result")
        """
        resultChart = FigureCanvasTkAgg(fig, resultFrame)
        resultChart.get_tk_widget().pack(side=tk.RIGHT, padx=15)
        """

        canvas.draw()


# destroy window and stop the app to run
def on_closing():
    if messagebox.askyesno("Quit", "Do you want to quit?"):
        window.destroy()
        window.quit()


# add function to button
window.protocol("WM_DELETE_WINDOW", on_closing)

window.resizable(False, False)
window.mainloop()
