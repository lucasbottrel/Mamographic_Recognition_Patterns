from ctypes.wintypes import RGB
import time
from tkinter import *
from tkinter import filedialog
from turtle import left
from imageio import imread
from skimage import data
from skimage.feature import graycomatrix, graycoprops
from skimage.measure import shannon_entropy
from skimage.morphology import disk, ball
from skimage import *
import numpy as np
from PIL import Image, ImageTk

from haralick import *

img_calc = None
execution_time = 0

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
    haralickScreen.geometry('1120x400')
    
    haralickScreen.config(background="white");
    
    title = Label(haralickScreen, text="Descritores de Haralick", font=('',24), anchor=CENTER, background='#5559fd' ,fg='white')
    title.place(x=30,y=20)
    
    start = time.time()
    
    haralick_results = haralick_calcs(img_calc)
    
    c1 = Label(haralickScreen, text="C1 ", font=('',14), background="white", fg='#5559fd')
    c1.place(x=30,y=80)
    
    homog_c1 = Label(haralickScreen, text="Homogeneidade: " + str(round(haralick_results[0].homogeneity,3)), font=('',12), background="white")
    homog_c1.place(x=30,y=120)
    
    energ_c1 = Label(haralickScreen, text="Energia: " + str(round(haralick_results[0].energy,3)), font=('',12), background="white")
    energ_c1.place(x=30,y=160)
    
    entrop_c1 = Label(haralickScreen, text="Entropia: " + str(round(haralick_results[0].entropy,3)), font=('',12), background="white")
    entrop_c1.place(x=30,y=200)
    
    c2 = Label(haralickScreen, text="C2 ", font=('',14), background="white", fg='#5559fd')
    c2.place(x=250,y=80)
    
    homog_c2 = Label(haralickScreen, text="Homogeneidade: " + str(round(haralick_results[1].homogeneity,3)), font=('',12), background='white')
    homog_c2.place(x=250,y=120)
    
    energ_c2 = Label(haralickScreen, text="Energia: " + str(round(haralick_results[1].energy,3)), font=('',12), background="white")
    energ_c2.place(x=250,y=160)
    
    entrop_c2 = Label(haralickScreen, text="Entropia: " + str(round(haralick_results[1].entropy,3)), font=('',12), background="white")
    entrop_c2.place(x=250,y=200)
    
    c4 = Label(haralickScreen, text="C4 ", font=('',14), background="white", fg='#5559fd')
    c4.place(x=470,y=80)
    
    homog_c4 = Label(haralickScreen, text="Homogeneidade: " + str(round(haralick_results[2].homogeneity,3)), font=('',12), background='white')
    homog_c4.place(x=470,y=120)
    
    energ_c4 = Label(haralickScreen, text="Energia: " + str(round(haralick_results[2].energy,3)), font=('',12), background="white")
    energ_c4.place(x=470,y=160)
    
    entrop_c4 = Label(haralickScreen, text="Entropia: " + str(round(haralick_results[2].entropy,3)), font=('',12), background="white")
    entrop_c4.place(x=470,y=200)
    
    c8 = Label(haralickScreen, text="C8 ", font=('',14), background="white", fg='#5559fd')
    c8.place(x=690,y=80)
    
    homog_c8 = Label(haralickScreen, text="Homogeneidade: " + str(round(haralick_results[3].homogeneity,3)), font=('',12), background='white')
    homog_c8.place(x=690,y=120)
    
    energ_c8 = Label(haralickScreen, text="Energia: " + str(round(haralick_results[3].energy,3)), font=('',12), background="white")
    energ_c8.place(x=690,y=160)
    
    entrop_c8 = Label(haralickScreen, text="Entropia: " + str(round(haralick_results[3].entropy,3)), font=('',12), background="white")
    entrop_c8.place(x=690,y=200)
    
    c16 = Label(haralickScreen, text="C16 ", font=('',14), background="white", fg='#5559fd')
    c16.place(x=910,y=80)
    
    homog_c16 = Label(haralickScreen, text="Homogeneidade: " + str(round(haralick_results[4].homogeneity,3)), font=('',12), background='white')
    homog_c16.place(x=910,y=120)
    
    energ_c16 = Label(haralickScreen, text="Energia: " + str(round(haralick_results[4].energy,3)), font=('',12), background="white")
    energ_c16.place(x=910,y=160)
    
    entrop_c16 = Label(haralickScreen, text="Entropia: " + str(round(haralick_results[4].entropy,3)), font=('',12), background="white")
    entrop_c16.place(x=910,y=200)
    
    execution_time = time.time() - start
    
    # ÁREA DE LOG
    bottomFrm = LabelFrame(haralickScreen, fg='#fff', text='Tempo de Execução', background='black')
    execTimeFrm = Label(bottomFrm, text=str(round(execution_time,4)) + ' ms', fg='white', background='black', font=('',11))
    execTimeFrm.place(x=10, y=5)
    bottomFrm.place(relwidth=1, relheight=0.2, rely=0.8)


# MAIN FRAME
root = Tk()
root.wm_title("Mamographic Recognition Patterns")
root.geometry('1280x600')

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
bottomFrm = LabelFrame(root, fg='#fff', text='Classificação da Imagem', background='black')
bottomFrm.place(relwidth=1, relheight=0.1, rely=0.9)

root.mainloop()
