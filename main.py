from tkinter import *
from tkinter import filedialog
from imageio import imread
from skimage import data
from skimage.feature import graycomatrix, graycoprops
from skimage.measure import shannon_entropy
from skimage.morphology import disk, ball
from skimage import *
import numpy as np
from PIL import Image, ImageTk

img_calc = None

def clear_label_image():
    imgFrm.config(image = '')

def upload_file():
    clear_label_image()
    
    global img
    global img_calc
    
    f_types = (("Image files", "*.png *.jpeg"), ("All files", "*.*"))
    filename = filedialog.askopenfilename(filetypes=f_types)
    
    img_calc = imread(filename)
    
    img = (Image.open(filename))
    img= ImageTk.PhotoImage(img.resize((400,400), Image.ANTIALIAS))
    imgFrm.config(image=img) 
    imgFrm.place(relx=0.5, rely=0.5)
    
    imgFrm.pack()

def openHaralick():
    haralickScreen = Tk()
    haralickScreen.wm_title("Haralick Calcs")
    haralickScreen.geometry('500x400')
    
    haralickScreen.config(background="white");
    
    title = Label(haralickScreen, text="Descritores de Haralick", font=('',24), anchor=CENTER)
    title.config(background="white")
    title.place(x=30,y=20)
    
    haralick_calcs = haralick_calcs(img_calc)
    
    c1 = Label(haralickScreen, text="C1 ", font=('',14))
    c1.config(background="white")
    c1.place(x=30,y=80)
    
    homog = Label(haralickScreen, text="Homogeneidade: " + str(round(homog_1,2)), font=('',12))
    homog.config(background="white")
    homog.place(x=30,y=120)
    
    energ = Label(haralickScreen, text="Energia: " + str(round(energ_1,2)), font=('',12))
    energ.config(background="white")
    energ.place(x=30,y=160)
    
    entrop = Label(haralickScreen, text="Entropia: " + str(round(entrop_1,2)), font=('',12))
    entrop.config(background="white")
    entrop.place(x=30,y=200)


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
calcMenu.add_command(label="Haralick", command=openHaralick)

menubar.add_cascade(label="Imagem", menu=imgMenu)
menubar.add_cascade(label="Calcular", menu=calcMenu)

# display the menu
root.config(menu=menubar)

# ÁREA DA IMAGEM
topSpace = Frame(root)
topSpace.place(relwidth=1, relheight=0.15)
topSpace.configure(background='white')

topFrm = Frame(root)
imgFrm = Label(topFrm,image='')
topFrm.place(relwidth=1, relheight=0.75, rely=0.15)
topFrm.configure(background='white')

# ÁREA DE LOG
bottomFrm = LabelFrame(root, fg='#fff', text='Tempo de Execução')
bottomFrm.place(relwidth=1, relheight=0.1, rely=0.9)
bottomFrm.configure(background='black')

root.mainloop()
