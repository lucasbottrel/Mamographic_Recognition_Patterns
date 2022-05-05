from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog
import calc

def upload_file():
    clear_label_image()
    global img
    f_types = (
        ("Image files", "*.png *.jpeg"), ("All files", "*.*")
    )
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = (Image.open(filename))
    resized_image= img.resize((400,400), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(resized_image) 
    imgFrm.config(image=img) 
    imgFrm.place(relx=0.5, rely=0.5)
    imgFrm.pack()

def clear_label_image():
    imgFrm.config(image = '');

# MAIN FRAME
root = Tk()
root.wm_title("Mamographic Recognition Patterns")
root.geometry('1280x720')

# TOP BAR
menubar = Menu(root)

# create a sub-menu
imgMenu = Menu(menubar, tearoff=0)
imgMenu.add_command(label="Nova Imagem", command=upload_file)
imgMenu.add_command(label="Substituir Imagem", command=upload_file)

calcMenu = Menu(menubar, tearoff=0)
calcMenu.add_command(label="Haralick", command=calc.openHaralick)

menubar.add_cascade(label="Imagem", menu=imgMenu)
menubar.add_cascade(label="Calcular", menu=calcMenu)

# display the menu
root.config(menu=menubar)

# ÁREA DA IMAGEM
topSpace = Frame(root)
topSpace.place(relwidth=1, relheight=0.15)
topSpace.configure(background='white')

topFrm = Frame(root)
imgFrm =Label(topFrm,image='')
topFrm.place(relwidth=1, relheight=0.75, rely=0.15)
topFrm.configure(background='white')

# ÁREA DE LOG
bottomFrm = LabelFrame(root, fg='#fff', text='Tempo de Execução')
bottomFrm.place(relwidth=1, relheight=0.1, rely=0.9)
bottomFrm.configure(background='black')

root.mainloop()
