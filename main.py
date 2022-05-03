from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog

# Function for opening the
# file explorer window
def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File",
                                          filetypes=(("Text files",
                                                      ["*.png*", "*.jpeg*", "*.jpg*"]),
                                                     ("all files",
                                                      "*.*")))

    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)


# MAIN FRAME
root = Tk()
root.wm_title("Mamographic Recognition Patterns")
root.geometry('1280x720')

# TOP BAR
# Create a File Explorer label
label_file_explorer = Label(root,
                            text="File Explorer using Tkinter",
                            width=100, height=4,
                            fg="blue")
menubar = Menu(root)
# create a sub-menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open", command=browseFiles)
filemenu.add_command(label="Save")

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_command(label="Quit!", command=root.quit)
# display the menu
root.config(menu=menubar)

# ÁREA DA IMAGEM
topFrm = LabelFrame(root, text="imagem")
topFrm.place(relwidth=1, relheight=0.75)
topFrm.configure(background='white')

# ÁREA DE LOG
bottomFrm = LabelFrame(root, text="terminal", fg='#fff')
bottomFrm.place(relwidth=1, relheight=0.25, rely=0.75)
bottomFrm.configure(background='black')

root.mainloop()
