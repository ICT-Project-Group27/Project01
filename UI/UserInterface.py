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
import parso

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import final

# creating window
window = tk.Tk()
# title
window.title("Plagiarism Checker")

# setting tkinter window size
window.geometry('600x600')

# setting switch state:
btnState = False

min_w = 60  # Minimum width of the frame
max_w = 120  # Maximum width of the frame
cur_width = min_w  # Increasing width of the frame
expanded = False  # Check if it is completely expanded
folderPath = ''
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
        home_l.config(text='Home', font=(0, 12))
        folder_l.config(text='Folder', font=(0, 12))
        result_l.config(text='Result', font=(0, 12))
        download_l.config(text='Download\n Result', font=(0, 10))
        info_l.config(text='Info', font=(0, 12))
    else:
        # Bring the image back
        menu_l.config(text="")
        home_l.config(text="")
        folder_l.config(text="")
        result_l.config(text="")
        download_l.config(text="")
        info_l.config(text='')


# add info/help button function
def infoButtonFunc():
    from subprocess import Popen, PIPE
    process = Popen(['python', 'PlaSysCheckerInfo.py'], stdout=PIPE)
    process.stdout.close()
    process.wait()


def changeFrame(windowFrame, toBeshownFrame):
    windowFrame.pack_forget()
    toBeshownFrame.pack()

def openFile():
    global folderPath
    from tkinter import filedialog as fd
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    folderPath = fd.askdirectory()+'/'
    updateListBox()

def updateListBox():
    names = final.walk_dir(folderPath)
    names = [names[0][1:]]
    for i in names:
        for x in i:
            listBox.insert(tk.END,x)




# Define the icons to be shown and resize it
navIcon = ImageTk.PhotoImage(Image.open('../resource/Menu.png').resize((20, 20)))
home = ImageTk.PhotoImage(Image.open('../resource/Home.png').resize((20, 20)))
folder = ImageTk.PhotoImage(Image.open('../resource/Folder.png').resize((20, 20)))
result = ImageTk.PhotoImage(Image.open('../resource/Result.png').resize((20, 20)))
download = ImageTk.PhotoImage(Image.open('../resource/Download.png').resize((20, 20)))
Info = ImageTk.PhotoImage(Image.open('../resource/Info.png').resize((20, 20)))

window.update()  # For the width to get updated
sid_bar_frame = tk.Frame(window, bg='#184089', width=50, height=window.winfo_height())
sid_bar_frame.pack(side=tk.LEFT)


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
menu_b = tk.Button(sid_bar_frame, image=navIcon, highlightbackground='#184089', activebackground='#184089',
                   relief='flat',
                   command=switch)
home_b = tk.Button(sid_bar_frame, image=home, highlightbackground='#184089', relief='flat',
                   command=lambda: changeFrame(resultFrame, mainFrame))
folder_b = tk.Button(sid_bar_frame, image=folder, highlightbackground='#184089', relief='flat')
result_b = tk.Button(sid_bar_frame, image=result, highlightbackground='#184089', relief='flat',
                     command=lambda: changeFrame(mainFrame, resultFrame))
download_b = tk.Button(sid_bar_frame, image=download, highlightbackground='#184089', relief='flat')
info_b = tk.Button(sid_bar_frame, image=Info, highlightbackground='#184089', relief='flat', command=infoButtonFunc)

# make label
menu_l = tk.Label(sid_bar_frame, text='', bg='#184089')
home_l = tk.Label(sid_bar_frame, text='', bg='#184089')
folder_l = tk.Label(sid_bar_frame, text='', bg='#184089')
result_l = tk.Label(sid_bar_frame, text='', bg='#184089')
download_l = tk.Label(sid_bar_frame, text='', bg='#184089')
info_l = tk.Label(sid_bar_frame, text='', bg='#184089')

# Put them on the frame
menu_b.grid(row=0, column=0, padx=1, pady=10)
menu_l.grid(row=0, column=1)
home_b.grid(row=1, column=0, padx=5, pady=30)
home_l.grid(row=1, column=1, padx=5, pady=30)
folder_b.grid(row=2, column=0, padx=5, pady=30)
folder_l.grid(row=2, column=1, padx=5, pady=30)
result_b.grid(row=3, column=0, padx=5, pady=30)
result_l.grid(row=3, column=1, padx=5, pady=30)
download_b.grid(row=4, column=0, padx=5, pady=30)
download_l.grid(row=4, column=1, padx=5, pady=30)
info_b.grid(row=5, column=0, padx=5, pady=30)
info_l.grid(row=5, column=1, padx=5, pady=30)

# So that it does not depend on the widgets inside the frame
sid_bar_frame.grid_propagate(False)

mainFrame = tk.Frame(window, bg='#f0a1a8', width=window.winfo_width(), height=(window.winfo_height()))
mainFrame.pack(side=tk.RIGHT)

# sideFrame
topFrame = tk.Frame(mainFrame, bg='#c0c0c0', width=window.winfo_width(), height=(window.winfo_height() / 5 * 4))
topFrame.pack(side=tk.TOP)
botFrame = tk.Frame(mainFrame, bg='#f0a1a8', width=window.winfo_width(), height=(window.winfo_height() / 5 * 1))
botFrame.pack(side=tk.BOTTOM)

# dropdownbox
dropDownFrame = tk.Frame(topFrame, bg='#c0c0c0', width=(window.winfo_width() / 5 * 1),
                         height=(window.winfo_height() / 5 * 4))
dropDownFrame.pack(side=tk.RIGHT)
selection_l = tk.Label(dropDownFrame, text='Language Selection:', bg='#c0c0c0', fg='black', font=(0, 18))
selection_l.pack(side=tk.TOP, pady=5, padx=15)
variable = tk.StringVar(dropDownFrame)
variable.set("Python")  # default value
selectionBox = OptionMenu(dropDownFrame, variable, "Python", "C++", "Java", "R", "C#")
selectionBox.configure(highlightbackground='black', background='#c0c0c0', fg='black', width=12)
selectionBox.pack(side=tk.BOTTOM, pady=5, padx=25)
topFrame.pack_propagate(False)

# listBox
listBoxFrame = tk.Frame(topFrame, bg='#c0c0c0', width=(window.winfo_width() / 5 * 4),
                        height=(window.winfo_height() / 5 * 4))
listBoxFrame.pack(side=tk.LEFT)
studentWork_l = tk.Label(listBoxFrame, text='Student Files:', bg='#c0c0c0', fg='black', font=(0, 20))
studentWork_l.grid(column=0, row=0, padx=10)
listBox = tk.Listbox(listBoxFrame, bg='white', fg='black', width=30)
listBox.grid(column=0, row=1, padx=10, columnspan=2)
selection_b = tk.Button(listBoxFrame, highlightbackground='#c0c0c0', text="Select Folder", width=12, command=lambda: openFile())
selection_b.grid(column=1, row=2)

# button for start plagiarism check
check_b = tk.Button(botFrame, highlightbackground='#f0a1a8', text="Plagiarism Check", command=lambda: final.check(folderPath))
check_b.pack(side=tk.RIGHT, padx=50)
botFrame.pack_propagate(False)


#resultFrame


resultFrame = tk.Frame(window, bg='#c0c0c0', width=window.winfo_width(), height=window.winfo_height())

def showResult():
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    from matplotlib.figure import Figure
    resultList = ["Below\n10%", "Between\n10%~15%", "Between\n15%~25%", "Over\n25%"]
    resultListCount = final.resultListCount

    if (len(resultListCount) > 1):
        fig = Figure(facecolor='white', figsize=(3.5, 3.5))  # create a figure object
        ax = fig.add_subplot(111)  # add an Axes to the figure
        ax.pie(resultListCount, radius=1, labels=resultList, autopct='%0.2f%%', shadow=True, textprops={'fontsize': 10})
        ax.set_title("Plagiarism Result")
        resultChart = FigureCanvasTkAgg(fig, resultFrame)
        resultChart.get_tk_widget().pack(side=tk.RIGHT, padx=15)


resultFrame.pack_propagate(False)


# destroy window and stop the app to run
def on_closing():
    if messagebox.askyesno("Quit", "Do you want to quit?"):
        window.destroy()
        window.quit()


# add function to button
window.protocol("WM_DELETE_WINDOW", on_closing)

window.resizable(False, False)
window.mainloop()
