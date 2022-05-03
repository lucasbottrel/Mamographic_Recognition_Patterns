from tkinter import *
from tkinter import ttk as tk
from tkinter import filedialog

def menuFunc(root):
    menubar = Menu(root)
    # create a sub-menu
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New")
    filemenu.add_command(label="Open", command=browseFiles(label_file_explorer))
    filemenu.add_command(label="Save")

    menubar.add_cascade(label="File", menu=filemenu)
    menubar.add_command(label="Quit!", command=root.quit)
    # display the menu
    root.config(menu=menubar)
    
    # Create a File Explorer label
    label_file_explorer = Label(root,
                                text = "File Explorer using Tkinter",
                                width = 100, height = 4,
                                fg = "blue")
    
# Function for opening the
# file explorer window
def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("all files",
                                                      "*.*")))

    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)