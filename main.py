from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog

def upload_file():
    global img
    f_types = [('Jpeg Files', '*.jpeg*'),('Png Files', '*.png*'),('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = ImageTk.PhotoImage(file=filename)
    imgFrm =Label(topFrm,image=img) # using Button 
    imgFrm.pack()

# MAIN FRAME
root = Tk()
root.wm_title("Mamographic Recognition Patterns")
root.geometry('1280x720')

# TOP BAR
menubar = Menu(root)

# create a sub-menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open", command=upload_file)
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
