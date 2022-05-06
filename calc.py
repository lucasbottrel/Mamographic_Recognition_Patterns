from tkinter import *
from tkinter import ttk
import skimage

print(skimage.__version__)

def openHaralick():
    haralickScreen = Tk()
    haralickScreen.wm_title("Haralick Calcs")
    haralickScreen.geometry('500x400')
    
    haralickScreen.config(background="white");
    
    homog = Label(haralickScreen, text="Descritores de Haralick", font=('',24))
    homog.config(background="white")
    homog.place(relx=0,y=20)
    
    homog = Label(haralickScreen, text="Homogeneidade")
    homog.config(background="white")
    homog.place(x=40,y=70)
    
    haralickScreen.mainloop()