#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat April  5 23:36:17 2022

@author: Ghee
"""
# importing tkinter gui
import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk


#creating window
window=tk.Tk()
#title
window.title("Plagiarism Checker")


#setting tkinter window size
window.geometry('600x600')

# setting switch state:
btnState = False



min_w = 60 # Minimum width of the frame
max_w = 120 # Maximum width of the frame
cur_width = min_w # Increasing width of the frame
expanded = False # Check if it is completely exanded

def expand():
    global cur_width, expanded
    cur_width += 10 # Increase the width by 10
    rep = window.after(5,expand) # Repeat this func every 5 ms
    sid_bar_frame.config(width=cur_width) # Change the width to new increase width
    if cur_width >= max_w: # If width is greater than maximum width 
        expanded = True # Frame is expended
        window.after_cancel(rep) # Stop repeating the func
        fill()

def contract():
    global cur_width, expanded
    cur_width -= 10 # Reduce the width by 10 
    rep = window.after(5,contract) # Call this func every 5 ms
    sid_bar_frame.config(width=cur_width) # Change the width to new reduced width
    if cur_width <= min_w: # If it is back to normal width
        expanded = False # Frame is not expanded
        window.after_cancel(rep) # Stop repeating the func
        fill()

def fill():
    if expanded: # If the frame is exanded
        # Show a text
        menu_l.config(text="Menu",font=(0,12))
        home_l.config(text='Home',font=(0,12), bg='#01e6fe')
        folder_l.config(text='Folder',font=(0,12))
        result_l.config(text='Result',font=(0,12))
        download_l.config(text='Download\n Result',font=(0,10))
        info_l.config(text='Info',font=(0,12))
    else:
        # Bring the image back
        menu_l.config(text="")
        home_l.config(text="")
        folder_l.config(text="")
        result_l.config(text="")
        download_l.config(text="")
        info_l.config(text='')

# Define the icons to be shown and resize it
navIcon = ImageTk.PhotoImage(Image.open('../resource/Menu.png').resize((20,20),Image.ANTIALIAS))
home = ImageTk.PhotoImage(Image.open('../resource/Home.png').resize((20,20),Image.ANTIALIAS))
folder = ImageTk.PhotoImage(Image.open('../resource/Folder.png').resize((20,20),Image.ANTIALIAS))
result = ImageTk.PhotoImage(Image.open('../resource/Result.png').resize((20,20),Image.ANTIALIAS))
download = ImageTk.PhotoImage(Image.open('../resource/Download.png').resize((20,20),Image.ANTIALIAS))
Info = ImageTk.PhotoImage(Image.open('../resource/Info.png').resize((20,20),Image.ANTIALIAS))

window.update() # For the width to get updated
sid_bar_frame = tk.Frame(window,bg='#01e6fe',width=50,height=window.winfo_height())
sid_bar_frame.grid(row=0,column=0) 


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
menu_b = tk.Button(sid_bar_frame,image=navIcon,bg='#01e6fe', activebackground='#01e6fe',relief='flat', command=switch)
home_b = tk.Button(sid_bar_frame,image=home,bg='#01e6fe',relief='flat')
folder_b = tk.Button(sid_bar_frame,image=folder,bg='#01e6fe',relief='flat')
result_b = tk.Button(sid_bar_frame,image=result,bg='#01e6fe',relief='flat')
download_b = tk.Button(sid_bar_frame,image=download,bg='#01e6fe',relief='flat')
info_b = tk.Button(sid_bar_frame,image=Info,bg='#01e6fe',relief='flat')

#make label
menu_l = tk.Label(sid_bar_frame,text ='',bg='#01e6fe')
home_l = tk.Label(sid_bar_frame,text ='',bg='#01e6fe')
folder_l = tk.Label(sid_bar_frame,text ='',bg='#01e6fe')
result_l = tk.Label(sid_bar_frame,text ='',bg='#01e6fe')
download_l = tk.Label(sid_bar_frame,text ='',bg='#01e6fe')
info_l = tk.Label(sid_bar_frame,text ='',bg='#01e6fe')


# Put them on the frame
menu_b.grid(row=0,column=0,padx=1,pady=10)
menu_l.grid(row=0, column=1)
home_b.grid(row=1,column=0,padx=5,pady=30)
home_l.grid(row=1,column=1,padx=5,pady=30)
folder_b.grid(row=2,column=0,padx=5,pady=30)
folder_l.grid(row=2,column=1,padx=5,pady=30)
result_b.grid(row=3,column=0,padx=5,pady=30)
result_l.grid(row=3,column=1,padx=5,pady=30)
download_b.grid(row=4,column=0,padx=5,pady=30)
download_l.grid(row=4,column=1,padx=5,pady=30)
info_b.grid(row=5,column=0,padx=5,pady=30)
info_l.grid(row=5,column=1,padx=5,pady=30)



# So that it does not depend on the widgets inside the frame
sid_bar_frame.grid_propagate(False)



frame1 = tk.Frame(window,bg='black',width=window.winfo_width(),height=window.winfo_height())
frame1.grid(row=0,column=1) 




#destroy window and stop the app to run
def on_closing():
    if messagebox.askyesno("Quit", "Do you want to quit?"):
        window.destroy()
        window.quit()
        
        

window.protocol("WM_DELETE_WINDOW", on_closing)




window.resizable(False, False)
window.mainloop()



